from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def team_actions_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[[InlineKeyboardButton(text='🟢 Взял в работу', callback_data='take_request'),
                          InlineKeyboardButton(text='✅ Завершено', callback_data='close_request')]]
    )
