from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def main_menu():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text='🤍 Поддержка и молитва')],
            [KeyboardButton(text='🌱 Духовный рост и вера')],
            [KeyboardButton(text='🤝 Знакомство с молодежным')]
        ], resize_keyboard=True
    )
