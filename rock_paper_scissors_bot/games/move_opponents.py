import random
import logging

figure = ["Камень 🪨", "Ножницы ✂️", "Бумага 📄"]

logger = logging.getLogger(__name__)

def motion_opponent():
    b = random.randint(1, 40)
    logger.info(f'Супер число {b}')
    if b == 1:
        return "ONE PUNCH MAN"
    return random.choice(figure)


def get_winner(user_choice: str, opponent_choice: str) -> str:
    """
    Определяет победителя раунда.
    Возвращает:
    - "win" - победа пользователя
    - "lose" - поражение пользователя
    - "draw" - ничья
    """
    if user_choice == opponent_choice:
        return "draw"

    if opponent_choice == "ONE PUNCH MAN":
        return "OPM"

    win_conditions = {
        "Камень 🪨": "Ножницы ✂️",
        "Ножницы ✂️": "Бумага 📄",
        "Бумага 📄": "Камень 🪨"
    }

    if win_conditions[user_choice] == opponent_choice:
        return "win"
    else:
        return "lose"