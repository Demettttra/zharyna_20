import telebot
from telebot import types
import requests
import json
token='5608477726:AAH7lZkEsCldoBt7u87Q25E11a36nxINLK0'
bot=telebot.TeleBot(token)

def create_kb():
    kb = types.InlineKeyboardMarkup()
    drink_btn = types.InlineKeyboardButton(text='Хочу пить', callback_data='1')
    eat_btn = types.InlineKeyboardButton(text='Хочу есть', callback_data='2')
    walk_btn = types.InlineKeyboardButton(text='Хочу гулять', callback_data='3')
    sleep_btn = types.InlineKeyboardButton(text='Хочу спать', callback_data='4')
    joke_btn = types.InlineKeyboardButton(text='Хочу шутку', callback_data='5')
    weather_btn = types.InlineKeyboardButton(text='Погода', callback_data='6')
    end_btn = types.InlineKeyboardButton(text='Завершить', callback_data='7')
    kb.add(drink_btn, eat_btn, walk_btn, sleep_btn, joke_btn, weather_btn, end_btn)
    return kb

@bot.message_handler(commands=['start', 'старт', 'поехали'])
def start_bot(mes):
    klava = create_kb()
    bot.send_message(mes.chat.id, 'Приветствую! Сделайте выбор', reply_markup=klava)

@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    if call.message:
        if call.data == '1':
            img=open('water.jpg', 'rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=open('water.jpg', 'rb'),
                caption="картинка воды",
                reply_markup = create_kb()
            )
            img.close()
        if call.data == '2':
            img = open('food.jpg', 'rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                caption="картинка еды",
                reply_markup=create_kb()
            )
            img.close()
        if call.data == '3':
            img = open('walk.jpg', 'rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                caption="картинка прогулки",
                reply_markup=create_kb()
            )
            img.close()
        if call.data == '4':
            img = open('sleep.jpg', 'rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                caption="картинка сна",
                reply_markup=create_kb()
            )
            img.close()
        if call.data == '5':
            img = open('joke.jpg', 'rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                caption="мем",
                reply_markup=create_kb()
            )
            img.close()
        if call.data == '6':
            url = "https://api.weather.yandex.ru/v2/informers?lat=52.4345&lon=30.9754"
            headers = {"X-Yandex-API-Key": "weather token"}
            r = requests.get(url=url, headers=headers)
            if r.status_code == 200:
                data = json.loads(r.text)
                fact = data["fact"]
                bot.send_message(call.message.chat.id,
                                 text=f'Сейчас в Гомеле {fact["temp"]}°, ощущается как {fact["feels_like"]}°')
            else:
                bot.send_message(call.message.chat.id, 'Недоступно в данный момент')
        if call.data == '7':
            bot.send_message(call.message.chat.id, 'Чао-какао')

bot.polling(non_stop=True)
