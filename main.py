from aiogram import Bot, Dispatcher, types, executor
from config import TELEGRAM_TOKEN
from keyboard.keyboards import  get_keyboard_1, get_keyboard_2

bot = Bot(token= TELEGRAM_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands = 'start')
async  def start(message: types.Message):
    await message.answer('Привет!', reply_markup= get_keyboard_1())

@dp.message_handler(lambda message: message.text == 'Отправь фото кота')
async def button_1_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo= 'https://cdnn21.img.ria.ru/images/156087/28/1560872802_0:778:1536:1642_600x0_80_0_0_606c2d47b6d37951adc9eaf750de22f0.jpg', caption= 'Вот тебе кот')

@dp.message_handler(lambda message: message.text == 'Перейти на следующую клавиатуру')
async def button_2_click(message: types.Message):
    await message.answer('Тут ты можешь попросить бота отправить фото собаки', reply_markup= get_keyboard_2())

@dp.message_handler(lambda message: message.text == 'Отправь фото собаки')
async def button_1_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo= 'https://cdnn1.inosmi.ru/img/24985/10/249851004_0:196:2030:1211_1920x0_80_0_0_78318b59d4ce0cde91f76a1b092765e7.jpg', caption= 'Вот тебе собака')

@dp.message_handler(lambda message: message.text == 'Перейти на предыдущую клавиатуру')
async def button_4_click(message: types.Message):
    await message.answer('Тут ты можешь попросить бота отправить фото кота', reply_markup= get_keyboard_1())

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates= True)