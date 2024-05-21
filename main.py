import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
import cfg

TOKEN = cfg.TOKEN
dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message):
    await message.answer(f"Привет, {html.bold(message.from_user.full_name)}."
                         f"\nДобро пожаловать в бот FAST-TARO."
                         f"\n"
                         f"\nЗдесь ты можешь заказать расклад по картам Таро. "
                         f"Это позволит тебе исследовать конкретную проблематику ситуации и определить её наиболее перспективные решения."
                         f"\n\nДля навигации используй меню")

@dp.message(Command('about'))
async def command_about(message: Message):
    await message.answer("О нас, о боте")

@dp.message(Command('pay'))
async def command_about(message: Message):
    await message.answer("Стоимость одного заказа составляет 1000 рублей"
                         "\n"
                         "\n1. Перед заказом вы совершаете перевод"
                         "\n2. Оплата производится по СБП +7********* ТинькоффБанк"
                         "\n3. В описании перевода необходимо указать свой логин телеграм"
                         "\n4. Проверка оплаты занимает до 10 минут"
                         "\n5. После проверки оплаты, баланс будет пополнен и вы сможете оформить заказ")

@dp.message(Command('balance'))
async def command_about(message: Message):
    await message.answer("Ваш баланс:"
                         "\n"
                         "\nхххх рублей - хватает на х заказов"
                         "\nхxx баллов - начисляется 30% баллами от суммы каждого пополнения")

@dp.message(Command('taro'))
async def command_about(message: Message):
    await message.answer("Вы точно готовы начать офорление?"
                         "\nПроцесс может занят некоторое время") #кнопки Начать и Позже + основная логика заведения таска и прокидывания инфы в БД.

@dp.message()
async def echo_handler(message: Message):
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.answer("Nice try!")


async def main():
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())