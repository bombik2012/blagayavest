from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def growth_menu():
    return ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text=f'{i}') ] for i in [
            '1️⃣ Основы христианской веры','2️⃣ С чего начать читать Библию',
            '3️⃣ Хочу укрепиться в вере','4️⃣ Есть вопросы о Боге и жизни',
            '5️⃣ Хочу пройти курс / наставничество'
        ]] + [[KeyboardButton(text='⬅️ Назад')]], resize_keyboard=True
    )
