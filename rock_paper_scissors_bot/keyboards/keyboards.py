from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def keyboard_menu():
    button_game = InlineKeyboardButton(text="Играть", callback_data="game")
    button_rules = InlineKeyboardButton(text="Правила", callback_data="rul")
    button_static = InlineKeyboardButton(text="Статистика", callback_data="static")
    # создаём клавиатуру с одним рядом
    inline_kb_men = InlineKeyboardMarkup(
        inline_keyboard=[[button_game, button_rules, button_static]]
    )

    return inline_kb_men


def keyboard_motion():
    buts = {"Камень": "Камень 🪨", "Ножницы": "Ножницы ✂️", "Бумага": "Бумага 📄"}
    button_rock = InlineKeyboardButton(text=buts['Камень'], callback_data="rock")
    button_paper = InlineKeyboardButton(text=buts['Бумага'], callback_data="paper")
    button_scissors = InlineKeyboardButton(text=buts['Ножницы'], callback_data="scissors")

    inline_kb_mot = InlineKeyboardMarkup(
        inline_keyboard=[[button_rock, button_paper, button_scissors]]
    )

    return inline_kb_mot

