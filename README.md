🚀 Juda yaxshi fikr! README fayli loyhani tushunarli va professional qiladi.
Sizning botingiz uchun tayyor README draftini yozib berdim 👇

⸻

📲 Impulse Rasmiy Telegram Bot

Bu Impulse loyihasining rasmiy Telegram botidir.
Bot foydalanuvchilarga telefon raqamlarini yuborib tasdiqlash kodi olish imkonini beradi. Har bir kod faqat 2 daqiqa amal qiladi.

⸻

⚙️ Texnologiyalar
	•	Python 3.11+
	•	Aiogram 3.x – Telegram Bot Framework
	•	SQLAlchemy – ORM (async)
	•	PostgreSQL – ma’lumotlar bazasi
	•	Asyncpg – asinxron PostgreSQL driver
	•	Pydantic – konfiguratsiya va validatsiya
	•	python-dotenv – .env fayl bilan ishlash

⸻

📂 Loyihaning tuzilishi

strucuturasi
bot.py asosiy qismi yozilgan
model.py sqlalchemy da model yozilgan usr uchun
db.py da postgres configuratsiyalari



.env                    # Konfiguratsiya fayli
requirements.txt        # Kerakli kutubxonalar


⸻

🔑 Asosiy imkoniyatlar
	1.	Start bosish → foydalanuvchiga rasmiy salomlashuv chiqadi.
	2.	Kontakt yuborish → foydalanuvchi raqamini ulashadi.
	3.	Kod olish → bot avtomatik tarzda 6 xonali tasdiqlash kodi yuboradi.
	4.	Kod muddati → kod 2 daqiqa davomida amal qiladi.
	5.	Yangi kod olish → foydalanuvchi inline button orqali yangilangan kod oladi.
	•	Agar kod hali aktiv bo‘lsa → bot faqat “✅ Sizning kodingiz hali ham faol!” deb xabar beradi.
	•	Agar muddati tugagan bo‘lsa → yangi kod yaratiladi va yuboriladi.

⸻

📦 O‘rnatish

1. Repozitoriyani klonlash

git clone https://github.com/JasurShermatov/impulse-bot.git
cd impulse-bot

2. Virtual environment yaratish

python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

3. Kutubxonalarni o‘rnatish

pip install -r requirements.txt

4. .env faylini sozlash

.env fayli ichida quyidagilarni to‘ldiring:

BOT_TOKEN=your_telegram_bot_token
DATABASE_URL=postgresql+asyncpg://username:password@localhost:5432/impulse_bot

5. Migratsiya va DB yaratish

python -m app.db.create_db

6. Botni ishga tushirish

python app/bot.py


⸻

👨‍💻 Ishlash jarayoni
	1.	Foydalanuvchi /start yuboradi.
	2.	Bot foydalanuvchidan kontakt so‘raydi.
	3.	Kontakt yuborilgach, bot foydalanuvchiga tasdiqlash kodi yuboradi.
	4.	Kod faqat 2 daqiqa amal qiladi.
	5.	Foydalanuvchi inline tugma orqali kodni yangilashga harakat qilishi mumkin.
	•	Agar kod hali aktiv bo‘lsa → bot xabar beradi.
	•	Agar kod muddati tugagan bo‘lsa → yangi kod yaratadi.

⸻

📌 Kelajakdagi rejalashtirilgan imkoniyatlar
	•	Admin panel orqali foydalanuvchilarni boshqarish.
	•	Statistik ma’lumotlar (qancha kod yuborilgan, aktiv foydalanuvchilar soni va h.k.).
	•	Email orqali kod yuborish integratsiyasi.

⸻

⚡ Muallif: Jasur Shermatov
📬 Aloqa: @jasur_shermatov
