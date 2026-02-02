from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def support_menu():
    return ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text=f'{i}') ] for i in [
            '1️⃣ Я впервые в церкви','2️⃣ Чувствую себя один(одна)','3️⃣ Мне сейчас тяжело',
            '4️⃣ Нужна молитвенная поддержка','5️⃣ Хочу поговорить с душепопечителем',
            '6️⃣ Хочу принять Иисуса Христа','7️⃣ Хочу обновить посвящение Богу',
            '8️⃣ Хочу принять водное крещение','9️⃣ Хочу стать членом церкви'
        ]] + [[KeyboardButton(text='⬅️ Назад')]], resize_keyboard=True
    )
