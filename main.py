import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from rock_paper_scissors_bot.handlers.user import router as rout_user
from rock_paper_scissors_bot.handlers.other import router as rout_other
from rock_paper_scissors_bot.config import config
from rock_paper_scissors_bot.keyboards.set_meny import set_main_menu


async def main():
    bot = Bot(token=config.token(),
              default=DefaultBotProperties(parse_mode=ParseMode.HTML)
              )
    dp = Dispatcher()

    logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(name)s | %(levelname)s | %(message)s"
)

    dp.include_router(router=rout_user)
    dp.include_router(router=rout_other)

    # кнопка menu
    await set_main_menu(bot)

    # пропускаем накопившиеся апдейты из запускаем бота
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, skip_updates=True)

if __name__ == "__main__": # запуск основного модуля
    asyncio.run(main())



