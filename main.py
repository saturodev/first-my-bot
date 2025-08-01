import asyncio
import os
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message


load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
CREATOR_NAME = "@atabackoff"
dp = Dispatcher()


# Command handler
@dp.message(Command("start"))
async def command_start_handler(message: Message) -> None:
    await message.reply(f"Hello ! {message.from_user.first_name}")


@dp.message(Command("help"))
async def help_by_information(message: Message):
    await message.answer(f"Мой хозяин: {CREATOR_NAME}")


# Run the bot
async def main() -> None:
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
