from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


fast_answers = InlineKeyboardMarkup().add(
        InlineKeyboardButton('Пробная ссылка', callback_data='trial_link')
    ).add(
        InlineKeyboardButton('Подтверждение оплаты', callback_data='success_payment')        
    )