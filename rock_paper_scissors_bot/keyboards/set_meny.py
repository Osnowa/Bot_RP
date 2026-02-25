from aiogram import Bot
from aiogram.types import BotCommand


# Функция для настройки кнопки Menu бота
async def set_main_menu(bot: Bot):
    main_menu_commands = [
        BotCommand(command='/start',
                   description='Запуск бота'),
        BotCommand(command='/static',
                   description='Статистика'),
        BotCommand(command='/sbros',
                   description='Сброс статистики')
    ]
    await bot.set_my_commands(main_menu_commands)