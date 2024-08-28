import asyncio
from aiogram import Bot, Dispatcher
from dotenv import find_dotenv, load_dotenv
import os
from handlers.user_private import user_private_router
from handlers.user_group import user_group_router
from common.bot_cmd_list import listOfCommands
from aiogram.types import BotCommandScopeAllPrivateChats
load_dotenv(find_dotenv())
bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher()



async def main():
    dp.include_routers(user_private_router)
    dp.include_routers(user_group_router)
    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_my_commands(commands=listOfCommands, scope=BotCommandScopeAllPrivateChats())
    await dp.start_polling(bot)
    
try: 
    asyncio.run(main())
except KeyboardInterrupt:
    print('End of work')