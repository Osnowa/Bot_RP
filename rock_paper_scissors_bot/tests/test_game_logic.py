import pytest
from rock_paper_scissors_bot.games.move_opponents import motion_opponent, figure, get_winner
from rock_paper_scissors_bot.database import games, users

def test_motion_opponent():
    '''Проверяем, что возвращается одно из значений'''
    result = motion_opponent()
    assert result in [*figure, "ONE PUNCH MAN"]


def test_super_move(mocker):
    '''Проверка, что при 1 выпадает супер удар !'''
    mocker.patch("rock_paper_scissors_bot.games.move_opponents.random.randint", return_value=1)
    assert motion_opponent() == "ONE PUNCH MAN"

def test_normal_move(mocker):
    '''Проверка, что при !1 выпадает обычный ход !'''
    mocker.patch("rock_paper_scissors_bot.games.move_opponents.random.randint", return_value=2)
    assert motion_opponent() in figure

@pytest.mark.parametrize(
    "a, b, expected",  # имена параметров
    [
        (figure[0], figure[1], 'win'),
        (figure[0], figure[0], 'draw'),
        (figure[0], figure[2], 'lose'),
    ]
)
def test_get_winer(a,b,expected):
    assert get_winner(a,b) == expected

def test_insert_user(temp_db):
    cursor = temp_db.cursor()
    cursor.execute("INSERT INTO users (telegram_id, wins, los, games) VALUES (?, ?, ?, ?)",
                   (12345, 1, 0, 1))
    temp_db.commit()

    cursor.execute("SELECT * FROM users WHERE telegram_id = ?", (12345,))
    user = cursor.fetchone()
    assert user is not None
    assert user[1] == 12345
    assert user[2] == 1

def test_select_user(temp_db):
    cursor = temp_db.cursor()
    # вставим пару пользователей
    cursor.executemany(
        "INSERT INTO users (telegram_id, wins, los, games) VALUES (?, ?, ?, ?)",
        [(111, 2, 1, 3), (222, 0, 2, 2)]
    )
    temp_db.commit()

    # выбираем победителей
    cursor.execute("SELECT telegram_id FROM users WHERE wins > ?", (1,))
    winners = [row[0] for row in cursor.fetchall()]
    assert winners == [111]

def test_update_user(temp_db):
    cursor = temp_db.cursor()
    cursor.execute("INSERT INTO users (telegram_id, wins) VALUES (?, ?)", (333, 0))
    temp_db.commit()

    # обновляем победы
    cursor.execute("UPDATE users SET wins = ? WHERE telegram_id = ?", (1, 333))
    temp_db.commit()

    cursor.execute("SELECT wins FROM users WHERE telegram_id = ?", (333,))
    wins = cursor.fetchone()[0]
    assert wins == 1

def test_delete_user(temp_db):
    cursor = temp_db.cursor()
    cursor.execute("INSERT INTO users (telegram_id, wins) VALUES (?, ?)", (444, 2))
    temp_db.commit()

    cursor.execute("DELETE FROM users WHERE telegram_id = ?", (444,))
    temp_db.commit()

    cursor.execute("SELECT * FROM users WHERE telegram_id = ?", (444,))
    user = cursor.fetchone()
    assert user is None