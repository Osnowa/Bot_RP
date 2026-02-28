def add_user(telegram_id, conn):
    cur = conn.cursor()
    cur.execute(
        "INSERT OR IGNORE INTO users (telegram_id) VALUES (?)",
        (telegram_id,)
    )
    conn.commit()


def get_user(telegram_id, conn):
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM users WHERE telegram_id = ?",
        (telegram_id,)
    )
    return cur.fetchone()
