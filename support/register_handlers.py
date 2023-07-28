from support.handlers import send_to_support, success_payment, trial_link, send_ref_link
from aiogram.dispatcher import Dispatcher as dp
from aiogram.types import ContentTypes

def register_handlers(dp: dp):
    dp.register_message_handler(send_ref_link, commands=['send_ref_link'])
    dp.register_message_handler(send_to_support, content_types=ContentTypes.ANY)
    dp.register_callback_query_handler(success_payment, text='success_payment')
    dp.register_callback_query_handler(trial_link, text='trial_link')