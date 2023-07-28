from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


how_much_kb = InlineKeyboardMarkup().add(
        InlineKeyboardButton('Сколько стоит?💸', callback_data='how_much')
    )

yes_btn = InlineKeyboardMarkup().add(
        InlineKeyboardButton('Да!', callback_data='server')
    )

platforms_kb = InlineKeyboardMarkup().add(
        InlineKeyboardButton('IOS', callback_data='ios')
    ).add(
        InlineKeyboardButton('Android', callback_data='android')
    ).add(
        InlineKeyboardButton('Windows', callback_data='windows')
    ).add(
        InlineKeyboardButton('macOS', callback_data='mac_os')
    ).add(
        InlineKeyboardButton('Linux', callback_data='linux')
    )

platforms_kb2 = InlineKeyboardMarkup().add(
        InlineKeyboardButton('IOS', callback_data='ios2')
    ).add(
        InlineKeyboardButton('Android', callback_data='android2')
    ).add(
        InlineKeyboardButton('Windows', callback_data='windows2')
    ).add(
        InlineKeyboardButton('macOS', callback_data='mac_os2')
    ).add(
        InlineKeyboardButton('Linux', callback_data='linux2')
    )
    

server_kb = InlineKeyboardMarkup().add(
        InlineKeyboardButton('Амстердам', callback_data='platforms_a')
    ).add(
        InlineKeyboardButton('Сингапур', callback_data='platforms_s')
    )