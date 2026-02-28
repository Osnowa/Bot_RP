import pytest
import sqlite3

@pytest.fixture()
def temp_db(tmp_path):
    db_file = tmp_path / "test_bot.db"
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            telegram_id INTEGER UNIQUE,
            wins INTEGER DEFAULT 0,
            los INTEGER DEFAULT 0,
            games INTEGER DEFAULT 0
        )
    """)
    conn.commit()

    yield conn
    conn.close()