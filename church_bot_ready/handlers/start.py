from aiogram import Router
from aiogram.types import Message
from keyboards.main_menu import main_menu
from texts import WELCOME_TEXT, CONFIDENTIAL_SHORT

router = Router()

@router.message(commands=['start'])
async def start_handler(message: Message):
    await message.answer(WELCOME_TEXT)
    await message.answer(CONFIDENTIAL_SHORT, reply_markup=main_menu())
