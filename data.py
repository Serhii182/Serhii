import sqlite3


def set_chat_id(chat_id, state):
    conn = sqlite3.connect('DATA.db')
    try:
        cursor = conn.cursor()
        cursor.execute('insert into info (chat_id, state) values ({0}, {1})'.format(chat_id, state))
        conn.commit()
    except sqlite3.Error as err:
        print(err)
    conn.close()


def set_state(chat_id, state):
    conn = sqlite3.connect('DATA.db')
    try:
        cursor = conn.cursor()
        cursor.execute('update info set state = {0} where chat_id = {1}'.format(state, chat_id))
        conn.commit()
    except sqlite3.Error as err:
        print(err)
    conn.close()


def get_state(chat_id):
    conn = sqlite3.connect('DATA.db')
    try:
        cursor = conn.cursor()
        cursor.execute('''select state from info where chat_id = {0}'''.format(chat_id))
        result = cursor.fetchone()[0]
        return result
    except sqlite3.Error as err:
        print(err)
    conn.close()


def set_converter_type(chat_id, converter_type):
    conn = sqlite3.connect('DATA.db')
    try:
        cursor = conn.cursor()
        cursor.execute('''update info set converter_type = '{0}' where chat_id = {1}'''.format(converter_type, chat_id))
        conn.commit()
    except sqlite3.Error as err:
        print(err)
    conn.close()


def get_converter_type(chat_id):
    conn = sqlite3.connect('DATA.db')
    try:
        cursor = conn.cursor()
        cursor.execute('''select converter_type from info where chat_id = {0}'''.format(chat_id))
        result = cursor.fetchone()[0]
        return result
    except sqlite3.Error as err:
        print(err)
    conn.close()
