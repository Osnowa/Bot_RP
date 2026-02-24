from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
import random
from rock_paper_scissors_bot.keyboards.keyboards import keyboard_knb as keyboard1, keyboard_yes_not as keyboard
from aiogram.types import ReplyKeyboardRemove

from rock_paper_scissors_bot.database import users

router = Router()

figure = ["Камень", "Ножницы", "Бумага"]


@router.message(Command(commands="start"))
async def process_command_start(message: Message):
    await message.answer(
        "Давай сыграем в игру: камень, ножницы, бумага ?",
        reply_markup=keyboard(),
    )
    telegram_id = message.from_user.id
    user = users.get_user(telegram_id)
    if not user:
        users.app_user(telegram_id)


@router.message(Command(commands="help"))
async def process_command_help(message: Message):
    await message.answer("Тут должны быть правила, но их и так все знают \n"
                         "Хочешь сыграть ? ",
                         reply_markup=keyboard())


@router.message(Command(commands="static"))
async def process_command_help(message: Message):
    user_data = users.get_user(message.from_user.id)
    a,b,c,d,e = user_data
    await message.answer(f"Вот Ваша Статистика игр \n"
                         f"Твой ID {b}")


@router.message(lambda x: x.text == "Давай")
async def answer_yes(message: Message):
    await message.answer(
        "Отлично \n"
        "Делай свой выбор",
        reply_markup=keyboard1())


@router.message(lambda x: x.text == "Не хочу")
async def answer_noy(message: Message):
    await message.answer("Жаль (",
                         reply_markup=ReplyKeyboardRemove())


@router.message(lambda x: x.text in figure)
async def answer(message: Message):
    otv_fig = random.choice(figure)
    if otv_fig == message.text:
        await message.answer("Ничья ! \n"
                             "Хочешь сыграть еще раз ?",
                             reply_markup=keyboard())
    elif otv_fig == 'Камень' and message.text == 'Ножницы':
        await message.answer("Проиграл ! \n"
                             "Хочешь сыграть еще раз ?",
                             reply_markup=keyboard())

    elif otv_fig == 'Бумага' and message.text == "Камень":
        await message.answer("Проиграл !\n"
                             "Хочешь сыграть еще раз ?",
                             reply_markup=keyboard())

    elif otv_fig == "Ножницы" and message.text == "Бумага":
        await message.answer("Проиграл \n"
                             "Хочешь сыграть еще раз ?",
                             reply_markup=keyboard())

    else:
        await message.answer(f"Я выбросил {otv_fig} \n"
                             f"Поздравляю, ты Победил ! \n"
                             "Хочешь сыграть еще раз ?",
                             reply_markup=keyboard())
