import datetime
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from config import TOKEN
from consts import *


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_command(msg: types.Message):
    await bot.send_message(msg.from_user.id, START_MSG)


@dp.message_handler(commands=['help'])
async def help_command(msg: types.Message):
    text = HELP_MSG + "\n"
    for command, description in HELP_COMMANDS.items():
        text += f"/{command} - {description}\n"
    await bot.send_message(msg.from_user.id, text)


@dp.message_handler(commands=['time'])
async def time_command(msg: types.Message):
    text = str(datetime.datetime.now().time())
    await bot.send_message(msg.from_user.id, text)


@dp.message_handler(commands=['calc'])
async def calc_command(msg: types.Message):
    problem = msg.get_args()
    try:
        ans = str(eval(problem))
    except Exception:
        ans = CALC_EVAL_ERROR
    await bot.send_message(msg.from_user.id, ans)


@dp.message_handler(commands=['ping'])
async def pong(msg: types.Message):
    print(msg.get_args())
    await bot.send_message(msg.from_user.id, "pong")


@dp.message_handler()
async def echo_message(msg: types.Message):
    text = msg.from_user.full_name + " say: " + msg.text
    await bot.send_message(msg.from_user.id, text)


if __name__ == "__main__":
    executor.start_polling(dp)