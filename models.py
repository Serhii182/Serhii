import requests
import config
from json import decoder
'''
bid - покупка - від більшого до меншого
ask - продаж - від меншого до більшого 
ask > bid
'''


def get_currency(currency):
    try:
        data = requests.get(config.API['Minfin']).json()
        price = data[currency]['ask']
    except KeyError:
        return 'Вибачте, сервер тимчасово недоступний'
    return price


def get_all():
    try:
        data = requests.get(config.API['Banks']).json()
        organizations = data['organizations']
    except (KeyError, decoder.JSONDecodeError):
        return 'Вибачте, сервер тимчасово недоступний'
    price = {}
    for organization in organizations:
        title = organization['title']
        try:
            price[title] = float(organization['currencies']['EUR']['bid'])
        except KeyError:
            pass
    return price


def get_date():
    try:
        data = requests.get(config.API['Banks']).json()
        date = data['date'][:10] + ':'
    except (KeyError, decoder.JSONDecodeError):
        return 'Вибачте, сервер тимчасово недоступний'
    return date


def get_bid_eur_abs():
    try:
        data = requests.get(config.API['Banks']).json()
        organizations = data['organizations']
    except (KeyError, decoder.JSONDecodeError):
        return 'Вибачте, сервер тимчасово недоступний'
    price = {}
    for organization in organizations:
        title = organization['title']
        if title not in config.LIST_OF_BAD_BANK:
            try:
                price[title] = float(organization['currencies']['EUR']['bid'])
            except KeyError:
                pass
    return sorted(price.items(), key=lambda x: x[1], reverse=True)[0]


def get_ask_eur_abs():
    try:
        data = requests.get(config.API['Banks']).json()
        organizations = data['organizations']
    except (KeyError, decoder.JSONDecodeError):
        return 'Вибачте, сервер тимчасово недоступний'
    price = {}
    for organization in organizations:
        title = organization['title']
        if title not in config.LIST_OF_BAD_BANK:
            try:
                price[title] = float(organization['currencies']['EUR']['ask'])
            except KeyError:
                pass
    return sorted(price.items(), key=lambda x: x[1], reverse=False)[0]


def get_bid_usd_abs():
    try:
        data = requests.get(config.API['Banks']).json()
        organizations = data['organizations']
    except (KeyError, decoder.JSONDecodeError):
        return 'Вибачте, сервер тимчасово недоступний'
    price = {}
    for organization in organizations:
        title = organization['title']
        if title not in config.LIST_OF_BAD_BANK:
            try:
                price[title] = float(organization['currencies']['USD']['bid'])
            except KeyError:
                pass
    return sorted(price.items(), key=lambda x: x[1], reverse=True)[0]


def get_ask_usd_abs():
    try:
        data = requests.get(config.API['Banks']).json()
        organizations = data['organizations']
    except (KeyError, decoder.JSONDecodeError):
        return 'Вибачте, сервер тимчасово недоступний'
    price = {}
    for organization in organizations:
        title = organization['title']
        if title not in config.LIST_OF_BAD_BANK:
            try:
                price[title] = float(organization['currencies']['USD']['ask'])
            except KeyError:
                pass
    return sorted(price.items(), key=lambda x: x[1], reverse=False)[0]


def get_bid_eur():
    try:
        data = requests.get(config.API['Banks']).json()
        organizations = data['organizations']
    except (KeyError, decoder.JSONDecodeError):
        return 'Вибачте, сервер тимчасово недоступний'
    price = {}
    for organization in organizations:
        title = organization['title']
        if title in config.LIST_OF_GREATEST_BANK:
            try:
                price[title] = float(organization['currencies']['EUR']['bid'])
            except KeyError:
                pass
    price = sorted(price.items(), key=lambda x: x[1], reverse=True)
    message = ''
    for i in range(len(price)):
        if i != len(price) - 1:
            message += "\U000027A1 " + '<b>{0}</b>:'.format(str(price[i][0])) + '\n'
            message += '<b>{0}</b>'.format(str(price[i][1])) + '<i> UAH / EUR</i>' + '\n\n'
        else:
            message += '__________\n<b>Найдорожче у банку:\n</b>'
            message += "\U000027A1 "+'<b>{0}:\n</b>'.format(str(get_bid_eur_abs()[0]))
            message += '<b>{0} </b>'.format(str(get_bid_eur_abs()[1]))+'<i>UAH / EUR</i> \n\n'
    message += '''<b>Дані надані: \n</b><a href='https://finance.ua/ru/currency'>https://finance.ua/ru/currency</a>'''
    return message


def get_ask_eur():
    try:
        data = requests.get(config.API['Banks']).json()
        organizations = data['organizations']
    except (KeyError, decoder.JSONDecodeError):
        return 'Вибачте, сервер тимчасово недоступний'
    price = {}
    for organization in organizations:
        title = organization['title']
        if title in config.LIST_OF_GREATEST_BANK:
            try:
                price[title] = float(organization['currencies']['EUR']['ask'])
            except KeyError:
                pass
    price = sorted(price.items(), key=lambda x: x[1], reverse=False)
    message = ''
    for i in range(len(price)):
        if i != len(price) - 1:
            message += "\U000027A1 " + '<b>{0}</b>:'.format(str(price[i][0])) + '\n'
            message += '<b>{0}</b>'.format(str(price[i][1])) + '<i> UAH / EUR</i>' + '\n\n'
        else:
            message += '__________\n<b>Найдешевше у банку:\n</b>'
            message += "\U000027A1 "+'<b>{0}:\n</b>'.format(str(get_ask_eur_abs()[0]))
            message += '<b>{0} </b>'.format(str(get_ask_eur_abs()[1]))+'<i>UAH / EUR</i> \n\n'
    message += '''<b>Дані надані: \n</b><a href='https://finance.ua/ru/currency'>https://finance.ua/ru/currency</a>'''
    return message


def get_bid_usd():
    try:
        data = requests.get(config.API['Banks']).json()
        organizations = data['organizations']
    except (KeyError, decoder.JSONDecodeError):
        return 'Вибачте, сервер тимчасово недоступний'
    price = {}
    for organization in organizations:
        title = organization['title']
        if title in config.LIST_OF_GREATEST_BANK:
            try:
                price[title] = float(organization['currencies']['USD']['bid'])
            except KeyError:
                pass
    price = sorted(price.items(), key=lambda x: x[1], reverse=True)
    message = ''
    for i in range(len(price)):
        if i != len(price) - 1:
            message += "\U000027A1 " + '<b>{0}</b>:'.format(str(price[i][0])) + '\n'
            message += '<b>{0}</b>'.format(str(price[i][1])) + '<i> UAH / USD</i>' + '\n\n'
        else:
            message += '__________\n<b>Найдорожче у банку:\n</b>'
            message += "\U000027A1 "+'<b>{0}:\n</b>'.format(str(get_bid_usd_abs()[0]))
            message += '<b>{0} </b>'.format(str(get_bid_usd_abs()[1]))+'<i>UAH / USD</i> \n\n'
    message += '''<b>Дані надані: \n</b><a href='https://finance.ua/ru/currency'>https://finance.ua/ru/currency</a>'''
    return message


def get_ask_usd():
    try:
        data = requests.get(config.API['Banks']).json()
        organizations = data['organizations']
    except (KeyError, decoder.JSONDecodeError):
        return 'Вибачте, сервер тимчасово недоступний'
    price = {}
    for organization in organizations:
        title = organization['title']
        if title in config.LIST_OF_GREATEST_BANK:
            try:
                price[title] = float(organization['currencies']['USD']['ask'])
            except KeyError:
                pass
    price = sorted(price.items(), key=lambda x: x[1], reverse=False)
    message = ''
    for i in range(len(price)):
        if i != len(price) - 1:
            message += "\U000027A1 " + '<b>{0}</b>:'.format(str(price[i][0])) + '\n'
            message += '<b>{0}</b>'.format(str(price[i][1])) + '<i> UAH / USD</i>' + '\n\n'
        else:
            message += '__________\n<b>Найдешевше у банку:\n</b>'
            message += "\U000027A1 "+'<b>{0}:\n</b>'.format(str(get_ask_usd_abs()[0]))
            message += '<b>{0} </b>'.format(str(get_ask_usd_abs()[1]))+'<i>UAH / USD</i>' + '\n\n'
    message += '''<b>Дані надані: \n</b><a href='https://finance.ua/ru/currency'>https://finance.ua/ru/currency</a>'''
    return message
