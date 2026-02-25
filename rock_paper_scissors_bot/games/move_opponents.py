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