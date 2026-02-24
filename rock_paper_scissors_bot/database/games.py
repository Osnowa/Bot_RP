from rock_paper_scissors_bot.database.db import connect

def add_wins(telegram_id):
    conn = connect()
    cur = conn.cursor()

    cur.execute('UPDATE users SET wins = wins + 1, games = games + 1 WHERE telegram_id = ?', (telegram_id,))

    conn.commit()
    conn.close()

def add_los(telegram_id):
    conn = connect()
    cur = conn.cursor()

    cur.execute('UPDATE users SET los = los + 1, games = games + 1 WHERE telegram_id = ?', (telegram_id,))

    conn.commit()
    conn.close()
