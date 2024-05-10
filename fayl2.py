from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup



def kanalbutton():
    markup = InlineKeyboardMarkup()
    markup.add(
        InlineKeyboardButton(text='Faberlik', url='https://t.me/feberlik84')
    )
    return markup








