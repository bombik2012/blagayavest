import asyncio
from aiogram import Bot, Dispatcher
from config import config
from handlers.start import router as start_router
from handlers.menus import router as menus_router
from handlers.request import router as request_router
from handlers.team_actions import router as team_router

async def main():
    bot = Bot(token=config.BOT_TOKEN)
    dp = Dispatcher()
    dp.include_router(start_router)
    dp.include_router(menus_router)
    dp.include_router(request_router)
    dp.include_router(team_router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
