from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def youth_menu():
    return ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text=i)] for i in [
            'Команда духовной поддержки','Команда молитвенников','Команда прославления',
            'Команда медиа и продакшена','Команда ашеров','Команда организаторов мероприятий',
            'Команда координации молодежи'
        ]] + [[KeyboardButton(text='⬅️ Назад')]], resize_keyboard=True
    )
