from aiogram import Router, F
from aiogram.types import Message
from keyboards.main_menu import main_menu
from keyboards.support_menu import support_menu
from keyboards.growth_menu import growth_menu
from keyboards.youth_menu import youth_menu

router = Router()

@router.message(F.text == '🤍 Поддержка и молитва')
async def support(message: Message):
    await message.answer('Выберите пункт:', reply_markup=support_menu())

@router.message(F.text == '🌱 Духовный рост и вера')
async def growth(message: Message):
    await message.answer('Выберите пункт:', reply_markup=growth_menu())

@router.message(F.text == '🤝 Знакомство с молодежным')
async def youth(message: Message):
    await message.answer('Выберите пункт:', reply_markup=youth_menu())

@router.message(F.text == '⬅️ Назад')
async def back(message: Message):
    await message.answer('Главное меню', reply_markup=main_menu())
