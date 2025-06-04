import asyncio
import os

from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram import Bot, Dispatcher
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from aiogram.types import BotCommandScopeAllPrivateChats
from dotenv import load_dotenv


from database.engine import session_marker, crate_db
from handlers.admin import admin_router
from handlers.user.user_handlers import user_router
from middlewares.db import DataBaseSession
from middlewares.shelder import SchedulersMiddleware
from my_command.command_start import privat

import sys
sys.stdout.reconfigure(encoding='utf-8')
load_dotenv()
bot = Bot(os.getenv('TOKEN'), default=DefaultBotProperties(parse_mode=ParseMode.HTML))
bot.my_admins_list = [6034157085, 156215306, 743055895, 322690337]
dp = Dispatcher()

dp.include_router(user_router)
dp.include_router(admin_router)


async def on_startup():
    print('Бот включен')
    await crate_db()
    print('База данных создана')


async def on_shutdown():
    print('Бот упал')



async def start():
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)
    await bot.set_my_commands(commands=privat, scope=BotCommandScopeAllPrivateChats())
    dp.update.middleware(DataBaseSession(session_pool=session_marker))
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(start())
    except KeyboardInterrupt as ex:
        print(ex)
