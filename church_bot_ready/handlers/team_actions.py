from aiogram import Router
from aiogram.types import CallbackQuery

router = Router()

@router.callback_query(lambda c: c.data == 'take_request')
async def take(callback: CallbackQuery):
    await callback.message.edit_text(callback.message.text + f"\n\n🟢 В работе: {callback.from_user.full_name}")
    await callback.answer('Вы взяли заявку')

@router.callback_query(lambda c: c.data == 'close_request')
async def close(callback: CallbackQuery):
    await callback.message.edit_text(callback.message.text + f"\n\n✅ Завершено: {callback.from_user.full_name}")
    await callback.answer('Заявка закрыта')
