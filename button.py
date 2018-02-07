import telebot


def main_markup():
    markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=False, resize_keyboard=True)
    button_one = telebot.types.KeyboardButton(text='Курс EUR')
    button_two = telebot.types.KeyboardButton(text='Курс USD')
    button_three = telebot.types.KeyboardButton(text='Додатково')
    markup.add(button_one, button_two, button_three)
    return markup


def inline_markup(values):
    markup = telebot.types.InlineKeyboardMarkup()
    for value in values:
        button = telebot.types.InlineKeyboardButton(text=value, callback_data=value)
        markup.add(button)
    return markup
