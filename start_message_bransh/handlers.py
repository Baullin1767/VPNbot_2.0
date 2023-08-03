from aiogram.types import Message, CallbackQuery
from data_base.db import get_user_exist, add_user

from start_message_bransh.kb import yes_btn, platforms_kb, how_much_kb, server_kb, platforms_kb2
from config import ADMINS, bot
from data_base import db
from servises import google_sheets_servis

async def start(mes: Message):
    if not get_user_exist(mes.from_user.id) \
            and mes.from_user.id not in ADMINS:
        add_user(mes.from_user.id, mes.from_user.full_name)
        if ' ' in mes.text:
            try:
                id_refer = int(mes.text.split()[1])
                db.add_refer(mes.from_user.id, id_refer)
            except ValueError:
                pass
            
    await mes.answer(f'''Привет, {mes.from_user.full_name}, я - бот, с помощью которого ты сможешь подключить классный VPN. Почему он классный? Рассказываю:

1. Его не заблокируют - принцип работы нашего сервиса отличается от стандартных VPN, которые до этого были у тебя

2. Скорость интернета с включённым VPN такая же, как раньше, до эпохи VPN

3. Ты можешь подключить несколько устройств одновременно, а ещё наш VPN работает на ios, android и windows 

4. Лимит трафика есть, и это 100 гб в месяц. Это много, но если вдруг тебе понадобиться больше - напиши мне, я все решу

5. Мой VPN безопасный: я не украду данные твоих карт или пароли, ваши данные только проходят через сервер, но нигде не хранятся

7. У меня доступная поддержка - ты просто пишешь в бот, и я решаю проблему)''', reply_markup=how_much_kb)

async def how_much(call: CallbackQuery):
    await call.answer()
    await call.message.answer('''Первые три дня для тебя действует бесплатный период, чтобы ты убедился, что все отлично работает. А после мы пришлём тебе напоминалку, что пора платить) Оплата доступа на 30 дней - 200₽
Подключаем?''', reply_markup=yes_btn)
    
async def chose_server(call: CallbackQuery):
    await call.answer()
    await call.message.answer('Выбери страну, где будет находиться VPN:', reply_markup=server_kb)
    
async def platforms(call: CallbackQuery):
    await call.answer()
    user_id = call.from_user.id
    if call.data == "platforms_a":
        server = 'A'
    if call.data == "platforms_s":
        server = 'S'
    db.add_server(user_id, server)
    await google_sheets_servis.update_table()
    await bot.send_message(ADMINS[0], f'{server}\n\n' +
                            f'#ID{user_id} ')
    await call.message.answer('Сейчас тебе нужно выбрать платформу:', reply_markup=platforms_kb)
    
async def platforms_mes(mes: Message):
    await mes.answer('Для подключения другого устройства выбери платформу и используй свой файл согласно инструкции:', reply_markup=platforms_kb2)
    
async def windows(call: CallbackQuery):
    await call.answer()
    if call.data == 'windows':
        text = 'Держи ссылку и скачивай приложение для использования. Напиши "Готово", как установишь.'
    elif call.data == 'windows2':
        text = 'Держи ссылку и скачивай приложение для использования.'
    await call.message.answer(f'{text}\n\n \
https://download.wireguard.com/windows-client/wireguard-installer.exe')
    
async def mac_os(call: CallbackQuery):
    await call.answer()
    if call.data == 'mac_os':
        text = 'Держи ссылку и скачивай приложение для использования. Напиши "Готово", как установишь.'
    elif call.data == 'mac_os2':
        text = 'Держи ссылку и скачивай приложение для использования.'
    await call.message.answer(f'{text}\n\n \
https://itunes.apple.com/us/app/wireguard/id1451685025?ls=1&mt=12')
    
async def android(call: CallbackQuery):
    await call.answer()
    if call.data == 'android':
        text = 'Держи ссылку и скачивай приложение для использования. Напиши "Готово", как установишь.'
    elif call.data == 'android2':
        text = 'Держи ссылку и скачивай приложение для использования.'
    await call.message.answer(f'{text}\n\n \
https://play.google.com/store/apps/details?id=com.wireguard.android')
    
async def ios(call: CallbackQuery):
    await call.answer()
    if call.data == 'ios':
        text = 'Держи ссылку и скачивай приложение для использования. Напиши "Готово", как установишь.'
    elif call.data == 'ios2':
        text = 'Держи ссылку и скачивай приложение для использования.'
    await call.message.answer(f'{text}\n\n \
https://itunes.apple.com/us/app/wireguard/id1441195209?ls=1&mt=8')
    
async def linux(call: CallbackQuery):
    await call.answer()
    if call.data == 'linux':
        text = 'Держи ссылку и скачивай приложение для использования. Напиши "Готово", как установишь.'
    elif call.data == 'linux2':
        text = 'Держи ссылку и скачивай приложение для использования.'
    await call.message.answer(f'{text}\n\n\
        Ubuntu: sudo apt install wireguard\n\
        Debian: apt install wireguard\n\n\
        Другие можно посмотреть здесь: https://www.wireguard.com/install/')
    

async def suggestion(mes: Message):
    await mes.answer('Опиши свою проблему и, пожалуйста, дождись ответа. Мы работаем с 13:00 до 04:00 по мск')