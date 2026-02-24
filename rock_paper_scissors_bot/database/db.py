import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "bot.db" # путь до базы данных

def connect():
    '''Подключаемся к базе данных'''
    return sqlite3.connect(DB_PATH)
