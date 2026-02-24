from aiogram import Router
from aiogram.types import Message

router = Router()

@router.message()
async def what(m: Message):
    await m.answer("Эй, я простой бот, я больше ничего не умею ( ")
