from aiogram import types, Dispatcher


async def set_default_commands(dp: Dispatcher):
    await dp.bot.set_my_commands([
        types.BotCommand("send_ref_link", "Реферальная ссылка"),
        types.BotCommand("suggestion", "Написать в поддержку"),
        types.BotCommand("planforms", "Выбрать другую платформу"),
    ])