import datetime
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

from config import TOKEN
from keyboards import *
from consts import *
from image_search import *


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_command(msg: types.Message):
    await bot.send_message(msg.from_user.id, START_MSG,
                           reply_markup=second_kb)


@dp.message_handler(commands=['photo'])
async def photo_command(msg: types.Message):
    await bot.send_photo(msg.from_user.id,
                         open("images/1.jpg", "rb"),
                         caption="мой заголовок")


@dp.message_handler(commands=['url_photo'])
async def url_photo_command(msg: types.Message):
    await bot.send_photo(msg.from_user.id,
                         "https://s0.rbk.ru/v6_top_pics/media/img/1/05/756637621281051.jpg")


@dp.message_handler(commands=['cat_photo'])
async def cat_photo_command(msg: types.Message):
    try:
        url = get_cat_image_url()
        await bot.send_photo(msg.from_user.id, url)
    except Exception:
        await bot.send_message(msg.from_user.id, CAT_URL_DOWNLOAD_ERROR)


@dp.message_handler(commands=['number_fact'])
async def number_fact_command(msg: types.Message):
    try:
        num = msg.get_args()
        await bot.send_message(msg.from_user.id, get_number_information(num))
    except Exception:
        await bot.send_message(msg.from_user.id, NUMBER_INFO_ERROR)

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


@dp.callback_query_handler(lambda x: x.data == BUTTON1)
async def press_button1(callback: types.CallbackQuery):
    await bot.answer_callback_query(callback.id)
    await bot.send_message(callback.from_user.id, "Я знаю, что вы делали прошлым летом")


if __name__ == "__main__":
    executor.start_polling(dp)
