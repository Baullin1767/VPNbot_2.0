from aiogram import executor
from config import dp
from data_base.db import connect_db
import set_commands
import asyncio

from start_message_bransh.register_handlers import register_handlers as start_branch
from support.register_handlers import register_handlers as support_branch
from check import check_sub

def register_all_handlers(dp):
    start_branch(dp)
    
    
    support_branch(dp)


async def on_startup(dispatcher):
    connect_db()
    await set_commands.set_default_commands(dispatcher)
    asyncio.create_task(check_sub.check())
    register_all_handlers(dispatcher)
    print('Запустился')

#Для тестов

from aiogram import types
from data_base import db
from datetime import datetime as dt

@dp.message_handler(commands=['check'])
async def check(mes: types.Message):
    db.add_date_sub(mes.from_user.id, dt.now().date())

# @dp.message_handler(commands=['add_sale'])
# async def add_sale(mes: types.Message):
#     db.add_invited(mes.from_user.id)
#     await mes.answer("+1")

# @dp.message_handler(commands=['get_invites'])
# async def get_invites(mes: types.Message):
#     await mes.answer(db.get_invited(mes.from_user.id))

# @dp.message_handler(commands=['get_refer'])
# async def get_refer(mes: types.Message):
#     await mes.answer(db.get_ref(mes.from_user.id))

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)