from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.types import CallbackQuery
from rock_paper_scissors_bot.keyboards import keyboards
from rock_paper_scissors_bot.games import move_opponents

from rock_paper_scissors_bot.database import users, games

router = Router()

# Словарь для соответствия callback_data и отображаемого текста
figure_map = {
    "rock": "Камень 🪨",
    "paper": "Бумага 📄",
    "scissors": "Ножницы ✂️"
}


@router.message(Command(commands="start"))
async def process_command_start(message: Message):
    await message.answer(
        f"Привет \n\n"
        f"Я простенький бот для игры в камень, ножницы, бумага \n Что тебя интересует ?",
        reply_markup=keyboards.keyboard_menu(),
    )
    telegram_id = message.from_user.id
    user = users.get_user(telegram_id)
    if not user:
        users.app_user(telegram_id)


@router.callback_query(lambda c: c.data == "rul")
async def callback_no(callback: CallbackQuery):
    await callback.message.answer("Правила: их нет )")
    await callback.answer()


@router.callback_query(lambda c: c.data == "static")
async def process_command_help(callback: CallbackQuery):
    user_data = users.get_user(callback.from_user.id)
    i, te_id, win, los, tot_games = user_data
    await callback.message.answer(
        f"📊 Вот Ваша Статистика игр:\n\n"
        f"🏆 Побед: {win}\n"
        f"💔 Поражений: {los}\n"
        f"🎮 Всего игр: {tot_games}"
    )
    await callback.answer()


@router.callback_query(lambda c: c.data == "game")
async def callback_yes(callback: CallbackQuery):
    await callback.message.answer(
        "Круто ! \nДелай свой ход",
        reply_markup=keyboards.keyboard_motion()
    )
    await callback.answer()


@router.callback_query(lambda x: x.data in ["rock", "paper", "scissors"])
async def callback_figure(callback: CallbackQuery):
    telegram_id = callback.from_user.id
    otv_fig = move_opponents.motion_opponent()  # возвращает "Камень 🪨", "Ножницы ✂️" или "Бумага 📄"
    user_choice = figure_map[callback.data]  # преобразуем "rock" в "Камень 🪨"

    if otv_fig == user_choice:
        await callback.message.answer(f"Ничья! Я тоже выбросил {otv_fig}")
        games.add_los(telegram_id)  # или games.add_draw если есть такая функция

    elif (
            (otv_fig == 'Камень 🪨' and user_choice == 'Ножницы ✂️') or
            (otv_fig == 'Бумага 📄' and user_choice == 'Камень 🪨') or
            (otv_fig == 'Ножницы ✂️' and user_choice == 'Бумага 📄')
    ):
        await callback.message.answer(f"Я выбросил {otv_fig}\nТы проиграл!")
        games.add_los(telegram_id)

    else:
        await callback.message.answer(f"Я выбросил {otv_fig}\nПоздравляю, ты победил!")
        games.add_wins(telegram_id)

    await callback.answer()