from start_message_bransh.handlers import start, platforms, windows, mac_os, android, ios, linux, how_much, suggestion, chose_server, platforms_mes
from aiogram.dispatcher import Dispatcher as dp

def register_handlers(dp: dp):
    dp.register_message_handler(start, commands=['start'])
    dp.register_message_handler(platforms_mes, commands=['planforms'])
    dp.register_message_handler(suggestion, commands=['suggestion'])
    dp.register_callback_query_handler(how_much, text='how_much')
    dp.register_callback_query_handler(chose_server, text='server')
    dp.register_callback_query_handler(chose_server, text='server')
    dp.register_callback_query_handler(platforms, text='platforms_s')
    dp.register_callback_query_handler(platforms, text='platforms_a')
    dp.register_callback_query_handler(windows, text='windows')
    dp.register_callback_query_handler(windows, text='windows2')
    dp.register_callback_query_handler(mac_os, text='mac_os')
    dp.register_callback_query_handler(mac_os, text='mac_os2')
    dp.register_callback_query_handler(android, text='android')
    dp.register_callback_query_handler(android, text='android2')
    dp.register_callback_query_handler(ios, text='ios')
    dp.register_callback_query_handler(ios, text='ios2')
    dp.register_callback_query_handler(linux, text='linux2')
    dp.register_callback_query_handler(linux, text='linux')