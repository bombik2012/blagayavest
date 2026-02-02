from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from states import RequestState
from keyboards.gender import gender_keyboard
from keyboards.team_actions import team_actions_keyboard
from utils import can_send_request
from config import config

router = Router()

SUBMENU_BUTTONS = [
    '1️⃣ Я впервые в церкви','2️⃣ Чувствую себя один(одна)','3️⃣ Мне сейчас тяжело',
    '4️⃣ Нужна молитвенная поддержка','5️⃣ Хочу поговорить с душепопечителем',
    '6️⃣ Хочу принять Иисуса Христа','7️⃣ Хочу обновить посвящение Богу',
    '8️⃣ Хочу принять водное крещение','9️⃣ Хочу стать членом церкви',
    '1️⃣ Основы христианской веры','2️⃣ С чего начать читать Библию',
    '3️⃣ Хочу укрепиться в вере','4️⃣ Есть вопросы о Боге и жизни',
    '5️⃣ Хочу пройти курс / наставничество',
    'Команда духовной поддержки','Команда молитвенников','Команда прославления',
    'Команда медиа и продакшена','Команда ашеров','Команда организаторов мероприятий',
    'Команда координации молодежи'
]

@router.message(F.text.in_(SUBMENU_BUTTONS))
async def start_request(message: Message, state: FSMContext):
    if not can_send_request(message.from_user.id):
        await message.answer('Можно отправлять заявки раз в 10 минут 🙏')
        return
    await state.update_data(point=message.text)
    await message.answer('Как вас можно назвать?')
    await state.set_state(RequestState.waiting_for_name)

@router.message(RequestState.waiting_for_name)
async def get_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer('Выберите пол:', reply_markup=gender_keyboard())
    await state.set_state(RequestState.waiting_for_gender)

@router.message(RequestState.waiting_for_gender)
async def get_gender(message: Message, state: FSMContext):
    data = await state.get_data()
    username = message.from_user.username
    if not username:
        await message.answer('Добавьте Telegram-ник и начните заново /start')
        await state.clear()
        return
    text = (
        '📩 Новая заявка\n\n'
        f"Запрос: {data['point']}\n"
        f"Имя: {data['name']}\n"
        f"Пол: {message.text}\n"
        f"Telegram: @{username}"
    )
    await message.bot.send_message(config.CARE_CHAT_ID, text, reply_markup=team_actions_keyboard())
    await message.answer('Спасибо 🤍 С вами свяжется служитель')
    await state.clear()
