import pytest
from rock_paper_scissors_bot.games.move_opponents import motion_opponent, figure, get_winner

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