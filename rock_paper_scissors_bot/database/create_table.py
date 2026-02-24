from rock_paper_scissors_bot.database.db import connect


def create_table():
    '''Создание таблицы'''
    conn = connect()
    cur = conn.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        telegram_id INTEGER UNIQUE,
        wins INTEGER DEFAULT 0,
        los INTEGER DEFAULT 0,
        games INTEGER DEFAULT 0
    )
    ''')


    conn.commit()  # закомитить изменения (что бы вступили в силу)
    conn.close()
