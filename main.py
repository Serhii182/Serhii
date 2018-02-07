import flask
import flask_sslify
import telebot
from flask import request, jsonify
import models
import button
import config
import data


app = flask.Flask(__name__)
sslify = flask_sslify.SSLify(app)

bot = telebot.TeleBot(config.TOKEN)

'''
конвертер, наразі, рахує лиш за сережнім курсом
'''


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        r = request.get_json()
        try:
            chat_id = r['message']['chat']['id']
            text = r['message']['text']

            data.set_chat_id(chat_id, 0)
            state = data.get_state(chat_id)

            if text == '/start' and state == 0:
                markup = button.main_markup()
                text = '\U0001F4CC<b> Доброго дня!\nВас вітає uaBanksBot\nДаний бот має наступні функціїї:' \
                       '\n\U00002705 Поточний курс валют у найбільших банках України\n\U00002705 Конвертер валют' \
                       '\n\U00002705 Пошук найближчого відділення заданого банку України</b>'
                bot.send_message(chat_id, text=text, reply_markup=markup, parse_mode='HTML')
            elif text == 'Курс EUR' and state == 0:
                markup = button.inline_markup(config.BUTTON['EUR'])
                text = '\U00002705'+'<b> Оберіть послугу банка:</b>'
                bot.send_message(chat_id, text=text, reply_markup=markup, parse_mode='HTML')
            elif text == 'Курс USD' and state == 0:
                markup = button.inline_markup(config.BUTTON['USD'])
                text = '\U00002705'+'<b> Оберіть послугу банка:</b>'
                bot.send_message(chat_id, text=text, reply_markup=markup, parse_mode='HTML')
            elif text == 'Додатково' and state == 0:
                text = '\U00002705'+'<b> Оберіть додаткову функцію</b>'
                markup = button.inline_markup(config.BUTTON['ADD'])
                bot.send_message(chat_id, text=text, reply_markup=markup, parse_mode='HTML')
            elif state == 1:
                converter_type = data.get_converter_type(chat_id)
                if converter_type == 'EUR - UAH':
                    try:
                        result = float(text) * float(models.get_currency('eur'))
                        text = '\U00002705' + '<b> {0} UAH\nОбраховано за курсом НБУ</b>'.format(str(result))
                        markup = button.inline_markup(['Конвертер валют'])
                        bot.send_message(chat_id, text=text, reply_markup=markup, parse_mode='HTML')
                        data.set_state(chat_id, 0)
                    except ValueError:
                        text = '\U000026D4'+'<b> Введіть, будь ласка, число</b>'
                        bot.send_message(chat_id, text=text, parse_mode='HTML')

                elif converter_type == 'UAH - EUR':
                    try:
                        result = float(text) / float(models.get_currency('eur'))
                        text = '\U00002705' + '<b> {0} EUR\nОбраховано за курсом НБУ</b>'.format(str(result))
                        markup = button.inline_markup(['Конвертер валют'])
                        bot.send_message(chat_id, text=text, reply_markup=markup, parse_mode='HTML')
                        data.set_state(chat_id, 0)
                    except ValueError:
                        text = '\U000026D4'+'<b> Введіть, будь ласка, число</b>'
                        bot.send_message(chat_id, text=text, parse_mode='HTML')
                elif converter_type == 'USD - UAH':
                    try:
                        result = float(text) * float(models.get_currency('usd'))
                        text = '\U00002705' + '<b> {0} UAH\nОбраховано за курсом НБУ</b>'.format(str(result))
                        markup = button.inline_markup(['Конвертер валют'])
                        bot.send_message(chat_id, text=text, reply_markup=markup, parse_mode='HTML')
                        data.set_state(chat_id, 0)
                    except ValueError:
                        text = '\U000026D4'+'<b> Введіть, будь ласка, число</b>'
                        bot.send_message(chat_id, text=text, parse_mode='HTML')
                elif converter_type == 'UAH - USD':
                    try:
                        result = float(text) / float(models.get_currency('usd'))
                        text = '\U00002705' + '<b> {0} USD\nОбраховано за курсом НБУ</b>'.format(str(result))
                        markup = button.inline_markup(['Конвертер валют'])
                        bot.send_message(chat_id, text=text, reply_markup=markup, parse_mode='HTML')
                        data.set_state(chat_id, 0)
                    except ValueError:
                        text = '\U000026D4'+'<b> Введіть, будь ласка, число</b>'
                        bot.send_message(chat_id, text=text, parse_mode='HTML')
            else:
                markup = button.main_markup()
                text = '<b>uaBanksBot</b>'
                bot.send_message(chat_id, text=text, reply_markup=markup, parse_mode='HTML')

        except KeyError:
            try:
                chat_id = r['callback_query']['from']['id']
                text = r['callback_query']['data']

                if text == 'Покупка EUR':
                    markup = button.inline_markup(['Продаж EUR'])
                    text = "\U0001F4CC"+'<b> Покупка EUR в банках України</b>\n' + '<b>станом на </b>' + '<b>{0}</b>'\
                        .format(models.get_date()) + '\n\n' + models.get_bid_eur()
                    bot.send_message(chat_id, text, parse_mode='HTML', reply_markup=markup,
                                     disable_web_page_preview=True)
                elif text == 'Продаж EUR':
                    markup = button.inline_markup(['Покупка EUR'])
                    text = "\U0001F4CC"+'<b> Продаж EUR в банках України</b>\n' + '<b>станом на </b>' + '<b>{0}</b>'\
                        .format(models.get_date()) + '\n\n' + models.get_ask_eur()
                    bot.send_message(chat_id, text, parse_mode='HTML', reply_markup=markup,
                                     disable_web_page_preview=True)

                elif text == 'Покупка USD':
                    markup = button.inline_markup(['Продаж USD'])
                    text = "\U0001F4CC"+'<b> Покупка USD в банках України</b>\n' + '<b>станом на </b>' + '<b>{0}</b>'\
                        .format(models.get_date()) + '\n\n' + models.get_bid_usd()
                    bot.send_message(chat_id, text, parse_mode='HTML', reply_markup=markup,
                                     disable_web_page_preview=True)
                elif text == 'Продаж USD':
                    markup = button.inline_markup(['Покупка USD'])
                    text = "\U0001F4CC"+'<b> Продаж USD в банках України</b>\n' + '<b>станом на </b>' + '<b>{0}</b>'\
                        .format(models.get_date()) + '\n\n' + models.get_ask_usd()
                    bot.send_message(chat_id, text, parse_mode='HTML', reply_markup=markup,
                                     disable_web_page_preview=True)

                elif text == 'Конвертер валют':
                    text = '\U00002705'+'<b>Оберіть тип конвертування</b>'
                    markup = button.inline_markup(config.BUTTON['CONVERTER'])
                    bot.send_message(chat_id, text=text, reply_markup=markup, parse_mode='HTML')

                elif text == 'EUR - UAH':
                    data.set_state(chat_id, state=1)
                    data.set_converter_type(chat_id=chat_id, converter_type=text)
                    text = '<b>Введіть суму EUR для обміну</b>'
                    bot.send_message(chat_id, text=text, parse_mode='HTML')
                elif text == 'UAH - EUR':
                    data.set_state(chat_id, state=1)
                    data.set_converter_type(chat_id=chat_id, converter_type=text)
                    text = '<b>Введіть суму UAH для обміну</b>'
                    bot.send_message(chat_id, text=text, parse_mode='HTML')
                elif text == 'USD - UAH':
                    data.set_state(chat_id, state=1)
                    data.set_converter_type(chat_id=chat_id, converter_type=text)
                    text = '<b>Введіть суму USD для обміну</b>'
                    bot.send_message(chat_id, text=text, parse_mode='HTML')
                elif text == 'UAH - USD':
                    data.set_state(chat_id, state=1)
                    data.set_converter_type(chat_id=chat_id, converter_type=text)
                    text = '<b>Введіть суму UAH для обміну</b>'
                    bot.send_message(chat_id, text=text, parse_mode='HTML')
                elif text == '''Зв'язатися із розробниками''':
                    text = '\U0001F4E7'+"<b> Зв'язатися із розробниками можна наступним чином:</b>\n" \
                           "<a href='serhiipolishchyk182@gmail.com'>serhiipolishchyk182@gmail.com</a>"
                    bot.send_message(chat_id, text=text, parse_mode='HTML')
                elif text == 'Найближче відділення':
                    text = '\U000023F3'+'<b> Перепрошуємо, але дана функція знаходиться у розробці</b>'
                    bot.send_message(chat_id, text=text, parse_mode='HTML')

            except KeyError:
                pass

        return jsonify(r)
    return '<h1>fitness bot</h1>'


if __name__ == '__main__':
    app.run()
