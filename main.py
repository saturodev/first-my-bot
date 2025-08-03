import asyncio
import os
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message


load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
dp = Dispatcher()


# Command handler
@dp.message(Command("start"))
async def command_start_handler(message: Message):
    user = message.from_user
    info = (
        f"Информация о вас:\n"
        f"🆔 ID: {user.id}\n"
        f"👤 Имя: {user.first_name}\n"
        f"👥 Фамилия: {user.last_name or '—'}\n"
        f"📛 Username: @{user.username or '—'}\n"
        f"🌐 Язык: {user.language_code or '—'}\n"
        f"💎 Premium: {'Да' if user.is_premium else 'Нет'}\n"
        f"🤖 Бот? {'Да' if user.is_bot else 'Нет'}"
    )
    await message.answer(info)


@dp.message(Command("help"))
async def info_about_bot(message: Message):
    bot_info = await message.bot.get_me()
    await message.answer(
        f"🤖 О боте:\n"
        f"Имя: {bot_info.first_name}\n"
        f"Username: @{bot_info.username}\n"
    )


@dp.message(F.text)
async def seperation_text(message: Message):
    new_text = message.text.split(" ")
    for i in new_text:
        await message.reply(i)


# Run the bot
async def main() -> None:
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
