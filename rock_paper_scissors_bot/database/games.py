from rock_paper_scissors_bot.database.db import connect


def add_wins(telegram_id):
    '''Запись в случае победы'''
    conn = connect()
    cur = conn.cursor()

    cur.execute('UPDATE users SET wins = wins + 1, games = games + 1 WHERE telegram_id = ?', (telegram_id,))

    conn.commit()
    conn.close()


def add_los(telegram_id):
    """Запись в случае поражения"""
    conn = connect()
    cur = conn.cursor()

    cur.execute('UPDATE users SET los = los + 1, games = games + 1 WHERE telegram_id = ?', (telegram_id,))

    conn.commit()
    conn.close()

def add_draw(telegram_id):
    """Запись в случае нечьи"""
    conn = connect()
    cur = conn.cursor()

    cur.execute('UPDATE users SET games = games + 1 WHERE telegram_id = ?', (telegram_id,))

    conn.commit()
    conn.close()

def sbros_static(telegram_id):
    """Сброс статистики"""
    conn = connect()
    cur = conn.cursor()

    cur.execute('UPDATE users SET wins = 0, games = 0, los = 0 WHERE telegram_id = ?', (telegram_id,))
    conn.commit()
    conn.close()
