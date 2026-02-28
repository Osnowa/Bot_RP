def add_wins(telegram_id, conn):
    cur = conn.cursor()
    cur.execute(
        "UPDATE users SET wins = wins + 1, games = games + 1 WHERE telegram_id = ?",
        (telegram_id,)
    )
    conn.commit()


def add_los(telegram_id, conn):
    cur = conn.cursor()
    cur.execute(
        "UPDATE users SET los = los + 1, games = games + 1 WHERE telegram_id = ?",
        (telegram_id,)
    )
    conn.commit()


def add_draw(telegram_id, conn):
    cur = conn.cursor()
    cur.execute(
        "UPDATE users SET games = games + 1 WHERE telegram_id = ?",
        (telegram_id,)
    )
    conn.commit()


def sbros_static(telegram_id, conn):
    cur = conn.cursor()
    cur.execute(
        "UPDATE users SET wins = 0, los = 0, games = 0 WHERE telegram_id = ?",
        (telegram_id,)
    )
    conn.commit()