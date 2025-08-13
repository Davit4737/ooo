from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import csv
from dotenv import load_dotenv
import os

# ====== НАСТРОЙКИ ======
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
CASINO_URL = os.getenv("CASINO_URL")

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Логируем пользователей
def log_user(user_id, username):
    with open("users.csv", "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([user_id, username])

# Команда /start
@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    log_user(message.from_user.id, message.from_user.username)
    
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Перейти в казик 🎰", url=https://1wwbud.life/?p=3k1u))
    
    await message.answer(
        f"Привет, {message.from_user.first_name}! 🎰\n"
        "Нажми на кнопку ниже, чтобы перейти в наш казик и получить бонус!",
        reply_markup=keyboard
    )

# Команда /stats — сколько пользователей пришло
@dp.message_handler(commands=["stats"])
async def stats(message: types.Message):
    try:
        with open("users.csv", "r", encoding="utf-8") as file:
            count = sum(1 for line in file)
        await message.answer(f"Всего пользователей: {count}")
    except FileNotFoundError:
        await message.answer("Пока нет данных о пользователях.")
        
if name == "main":
    print("Бот запущен...")
    executor.start_polling(dp, skip_updates=True)