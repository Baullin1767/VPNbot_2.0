import asyncio

from config import bot, ADMINS
from data_base import db
from datetime import datetime as dt

async def check():
    invited=0
    coust = 200
    trial_text = '''Привет!

Бесплатный период пользования закончился, и если ты хочешь продолжать пользоваться моим VPN,\
то, пожалуйста, оплати следующий месяц

Для этого тебе нужно перевести 200₽ на карту *Тинкофф* по номеру телефона 877777777 Иван И. и отправить мне скрин оплаты'''
    sub_text = '''Привет!

Оплаченный период пользования закончится завтра, и если ты хочешь продолжать пользоваться моим VPN, то, пожалуйста, оплати следующий месяц. 

Иначе доступ будет автоматически ограничен и ты не сможешь пользоваться моим сервисом)

Для этого тебе нужно перевести 200₽ на карту *Тинкофф* по номеру телефона 877777777 Иван И. и отправить мне скрин оплаты.'''

    sub_text_sale = lambda invited, coust :f'''Привет!

Оплаченный период пользования закончится завтра, и если ты хочешь продолжать пользоваться моим VPN, то, пожалуйста, оплати следующий месяц. 

Иначе доступ будет автоматически ограничен и ты не сможешь пользоваться моим сервисом)

В этом месяце по твоей реферальной ссылке подключилось {invited} человек, и поэтому, с учетом скидки, \
тебе нужно перевести {coust}₽ на карту *Тинкофф* по номеру
телефона 877777777 Иван И. и отправить мне скрин оплаты. 

Спасибо, что рекомендуешь нас💙'''

    sub_text_free = f'''Привет!

В этом месяце по твоей реферальной ссылке зарегистрировалось 5 человек, поэтому ты получаешь бесплатный месяц использования VPN.\
Спасибо, что рекомендуешь нас💙

Я напомню когда нужно будет заплатить в следующий раз.

Твой Stark's VPN'''
    

    while True:
        users = db.get_users()
        for user in users:
            user_id = user[0]
            date_sub = user[3]
            trial = user[-3]
            invited = user[-2]
            referal_id = user[-1]
            if date_sub != None:
                date_sub = dt.strptime(date_sub, "%Y-%m-%d").date()
            else:
                continue
            if date_sub <= dt.now().date():
                if trial:
                    text = trial_text
                    db.add_trial(user_id, False)
                    db.add_date_sub(user_id, None)
                else:
                    if invited == 0:
                        text = sub_text
                    elif 1 <= invited < 5:
                        coust = 200 - 40 * invited
                        text = sub_text_sale(invited, coust)
                    elif invited == 5:
                        text = sub_text_free
                    db.add_date_sub(user_id, None)
                    db.drop_invited(user_id)
                await bot.send_message(user_id, text, parse_mode='Markdown')
                await bot.send_message(ADMINS[0], f'{text}\n\n' +
                            f'#ID{user_id} ', parse_mode='Markdown')
        await asyncio.sleep(10*60)