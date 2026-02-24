from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove


def keyboard_yes_not():
    # создаём кнопки
    button_1 = KeyboardButton(text="Давай")
    button_2 = KeyboardButton(text="Не хочу")

    # создаём клавиатуру
    keyboard = ReplyKeyboardMarkup(
        keyboard=[[button_1, button_2]],  # один ряд
        resize_keyboard=True,  # делаем кнопки компактнее
        one_time_keyboard=True  # клавиатура скрывается после нажатия
    )
    return keyboard


def keyboard_knb():
    # создаём кнопки
    button_10 = KeyboardButton(text="Камень")
    button_20 = KeyboardButton(text="Ножницы")
    button_30 = KeyboardButton(text="Бумага")

    # создаём клавиатуру
    keyboard1 = ReplyKeyboardMarkup(
        keyboard=[[button_10, button_20, button_30]],  # один ряд
        resize_keyboard=True,  # делаем кнопки компактнее
        one_time_keyboard=True  # клавиатура скрывается после нажатия
    )
    return keyboard1
