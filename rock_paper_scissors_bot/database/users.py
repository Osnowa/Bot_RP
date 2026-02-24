from rock_paper_scissors_bot.database.db import connect

def app_user(telegram_id):
    '''Добавляем пользователя в таблицу'''
    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "INSERT OR IGNORE INTO users (telegram_id) VALUES (?)",
        (telegram_id,)
    )

    conn.commit()
    conn.close()

def get_user(telegram_id):
    '''Получаем все данные пользователя'''
    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM users WHERE telegram_id = ?",
        (telegram_id,)
    )

    us = cur.fetchone()
    conn.close()

    return us
