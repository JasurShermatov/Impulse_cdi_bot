# bot.py
import asyncio
import os
import random
import datetime
from aiogram import Bot, Dispatcher, F
from aiogram.types import (
    Message, KeyboardButton, ReplyKeyboardMarkup,
    InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
)
from aiogram.filters import Command


from aiogram.client.default import DefaultBotProperties
from dotenv import load_dotenv
from sqlalchemy import select
from db import AsyncSessionLocal, engine, Base
from models import User, VerificationCode

import pytz

uzb_tz = pytz.timezone("Asia/Tashkent")


load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode="HTML"))
dp = Dispatcher()


def contact_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text="☎️ Yuborish / Send", request_contact=True)]],
        resize_keyboard=True,
        one_time_keyboard=True
    )


def code_buttons():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🔄 Kodni yangilash", callback_data="refresh_code")]
        ]
    )


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


def generate_code():
    return str(random.randint(100000, 999999))


@dp.message(Command("start"))
async def start_handler(message: Message):
    full_name = message.from_user.full_name
    await message.answer(
        f"👋 <b>Salom, {full_name}!</b>\n\n"
        f"🔗 <b>@impulse_cdi</b>’ning <i>rasmiy botiga</i> xush kelibsiz.\n\n"
        f" Iltimos telefon raqamingizni yuboring:",
        reply_markup=contact_keyboard()
    )


@dp.message(F.contact)
async def handle_contact(message: Message):
    phone = message.contact.phone_number
    telegram_id = str(message.from_user.id)
    full_name = message.from_user.full_name

    async with AsyncSessionLocal() as session:
        result = await session.execute(select(User).where(User.telegram_id == telegram_id))
        user = result.scalar_one_or_none()

        if not user:
            user = User(
                telegram_id=telegram_id,
                full_name=full_name,
                phone_number=phone
            )
            session.add(user)
            await session.commit()
            await session.refresh(user)

        new_code = generate_code()
        expires_at = datetime.datetime.utcnow() + datetime.timedelta(minutes=2)

        code_entry = VerificationCode(user_id=user.id, code=new_code, expires_at=expires_at)
        session.add(code_entry)
        await session.commit()

        await message.answer(
            f"🔒 Code: <b>{new_code}</b>\n\n"
            f"⏳ Bu kod faqat 2 daqiqa amal qiladi.",
            reply_markup=code_buttons()
        )


@dp.callback_query(F.data == "refresh_code")
async def refresh_code_handler(callback: CallbackQuery):
    async with AsyncSessionLocal() as session:
        result = await session.execute(
            select(VerificationCode)
            .join(User)
            .where(User.telegram_id == str(callback.from_user.id))
            .order_by(VerificationCode.id.desc())
        )
        last_code = result.scalars().first()

        if last_code and last_code.expires_at > datetime.datetime.utcnow():
            # Kod hali aktiv → faqat notification yuboramiz (vaqtsiz)
            return await callback.answer(
                "✅ Sizning kodingiz hali ham faol!",
                show_alert=True
            )

        # Agar muddati tugagan bo‘lsa → yangi kod yaratamiz
        new_code = generate_code()
        expires_at = datetime.datetime.utcnow() + datetime.timedelta(minutes=2)

        verification_code = VerificationCode(
            user_id=last_code.user_id if last_code else None,
            code=new_code,
            expires_at=expires_at
        )
        session.add(verification_code)
        await session.commit()

        await callback.message.edit_text(
            f"♻️ Yangi kod yaratildi!\n\n"
            f"<b>{new_code}</b>",
            reply_markup=code_buttons()
        )


async def main():
    await init_db()
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())