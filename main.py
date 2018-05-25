# -*- coding: utf-8 -*-
from constants import TOKEN
import messages
# pytelegrambotapi
import telebot
import requests
import os
from telebot import types


bot = telebot.TeleBot(TOKEN)
markup = types.ReplyKeyboardMarkup(row_width=2)
itembtn1 = types.KeyboardButton('Almaty')
itembtn2 = types.KeyboardButton('Astana')
itembtn3 = types.KeyboardButton('Karaganda')
itembtn4 = types.KeyboardButton('Pavlodar')
itembtn5 = types.KeyboardButton('Aktobe')
itembtn6 = types.KeyboardButton('Atyrau')
itembtn7 = types.KeyboardButton('Petropavlsk')
itembtn8 = types.KeyboardButton('Taraz')
itembtn9 = types.KeyboardButton('Uralsk')
itembtn10 = types.KeyboardButton('Oskemen')
itembtn11 = types.KeyboardButton('Kyzylorda')
itembtn12 = types.KeyboardButton('Shymkent')
itembtn13 = types.KeyboardButton('Semey')
itembtn14 = types.KeyboardButton('Aktau')
markup.row(itembtn1, itembtn2, itembtn3, itembtn4)
markup.row(itembtn5, itembtn6, itembtn7, itembtn8)
markup.row(itembtn9, itembtn10, itembtn11, itembtn12)
markup.row(itembtn13, itembtn14)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, messages.HELLO)

@bot.message_handler(commands = ['weather'])
def get_weather(message):
    bot.send_message(message.chat.id, "Choose City:", reply_markup=markup)

def send_music(message,formatted_data):
    if formatted_data.find('clear'):
        path = '/home/ubuntu/yerdaulet_assyl/weathic_bot1/sunny/'
        files = os.listdir(path)
        for i in files:
            audio = open(path+i, 'rb')
            bot.send_audio(message.chat.id, audio)
            audio.close()
    if formatted_data.find('sun'):
        path = '/home/ubuntu/yerdaulet_assyl/weathic_bot1/sunny/'
        files = os.listdir(path)
        for i in files:
            audio = open(path+i, 'rb')
            bot.send_audio(message.chat.id, audio)
            audio.close()
    elif formatted_data.find('cloud'):
        path = '/home/ubuntu/yerdaulet_assyl/weathic_bot1/cloudy/'
        files = os.listdir(path)
        for i in files:
            audio = open(path+i, 'rb')
            bot.send_audio(message.chat.id, audio)
            audio.close()
    elif formatted_data.find('rain'):
        path = '/home/ubuntu/yerdaulet_assyl/weathic_bot1/rainy/'
        files = os.listdir(path)
        for i in files:
            audio = open(path+i, 'rb')
            bot.send_audio(message.chat.id, audio)
            audio.close()
    elif formatted_data.find('wind'):
        path = '/home/ubuntu/yerdaulet_assyl/weathic_bot1/rainy/'
        files = os.listdir(path)
        for i in files:
            audio = open(path+i, 'rb')
            bot.send_audio(message.chat.id, audio)
            audio.close()
    

@bot.message_handler(regexp = 'Almaty')
def almaty(message):
    url = 'http://api.openweathermap.org/data/2.5/weather?appid=a7944b9d9d9abfc17b63880905110c8e&q=Almaty'
    json_data = requests.get(url).json()
    formatted_data = json_data['weather'][0]['description']
    temp = json_data['main']['temp']
    temp_max = json_data['main']['temp_max']
    temp_min = json_data['main']['temp_min']
    bot.send_message(message.chat.id,"Weather in Almaty: {}\nTemperature: {}\nMax temperature: {}\nMin temperature: {}\n".format(formatted_data, int(temp)-273, int(temp_max)-273, int(temp_min)-273))
    send_music(message,formatted_data)

@bot.message_handler(regexp = 'Astana')
def astana(message):
    url = 'http://api.openweathermap.org/data/2.5/weather?appid=a7944b9d9d9abfc17b63880905110c8e&q=Astana'
    json_data = requests.get(url).json()
    formatted_data = json_data['weather'][0]['description']
    temp = json_data['main']['temp']
    temp_max = json_data['main']['temp_max']
    temp_min = json_data['main']['temp_min']
    bot.send_message(message.chat.id,"Weather in Astana: {}\nTemperature: {}\nMax temperature: {}\nMin temperature: {}\n".format(formatted_data, int(temp)-273, int(temp_max)-273, int(temp_min)-273))
    send_music(message,formatted_data)

@bot.message_handler(regexp = 'Karaganda')
def astana(message):
    url = 'http://api.openweathermap.org/data/2.5/weather?appid=a7944b9d9d9abfc17b63880905110c8e&q=Karaganda'
    json_data = requests.get(url).json()
    formatted_data = json_data['weather'][0]['description']
    temp = json_data['main']['temp']
    temp_max = json_data['main']['temp_max']
    temp_min = json_data['main']['temp_min']
    bot.send_message(message.chat.id,"Weather in Karaganda: {}\nTemperature: {}\nMax temperature: {}\nMin temperature: {}\n".format(formatted_data, int(temp)-273, int(temp_max)-273, int(temp_min)-273))
    send_music(message,formatted_data)

@bot.message_handler(regexp = 'Pavlodar')
def astana(message):
    url = 'http://api.openweathermap.org/data/2.5/weather?appid=a7944b9d9d9abfc17b63880905110c8e&q=Pavlodar'
    json_data = requests.get(url).json()
    formatted_data = json_data['weather'][0]['description']
    temp = json_data['main']['temp']
    temp_max = json_data['main']['temp_max']
    temp_min = json_data['main']['temp_min']
    bot.send_message(message.chat.id,"Weather in Pavlodar: {}\nTemperature: {}\nMax temperature: {}\nMin temperature: {}\n".format(formatted_data, int(temp)-273, int(temp_max)-273, int(temp_min)-273))
    send_music(message,formatted_data)


@bot.message_handler(regexp = 'Aktobe')
def astana(message):
    url = 'http://api.openweathermap.org/data/2.5/weather?appid=a7944b9d9d9abfc17b63880905110c8e&q=Aktobe'
    json_data = requests.get(url).json()
    formatted_data = json_data['weather'][0]['description']
    temp = json_data['main']['temp']
    temp_max = json_data['main']['temp_max']
    temp_min = json_data['main']['temp_min']
    bot.send_message(message.chat.id,"Weather in Aktobe: {}\nTemperature: {}\nMax temperature: {}\nMin temperature: {}\n".format(formatted_data, int(temp)-273, int(temp_max)-273, int(temp_min)-273))
    send_music(message,formatted_data)

@bot.message_handler(regexp = 'Atyrau')
def astana(message):
    url = 'http://api.openweathermap.org/data/2.5/weather?appid=a7944b9d9d9abfc17b63880905110c8e&q=Atyrau'
    json_data = requests.get(url).json()
    formatted_data = json_data['weather'][0]['description']
    temp = json_data['main']['temp']
    temp_max = json_data['main']['temp_max']
    temp_min = json_data['main']['temp_min']
    bot.send_message(message.chat.id,"Weather in Atyrau: {}\nTemperature: {}\nMax temperature: {}\nMin temperature: {}\n".format(formatted_data, int(temp)-273, int(temp_max)-273, int(temp_min)-273))
    send_music(message,formatted_data)

@bot.message_handler(regexp = 'Petropavlsk')
def astana(message):
    url = 'http://api.openweathermap.org/data/2.5/weather?appid=a7944b9d9d9abfc17b63880905110c8e&q=Petropavlsk'
    json_data = requests.get(url).json()
    formatted_data = json_data['weather'][0]['description']
    temp = json_data['main']['temp']
    temp_max = json_data['main']['temp_max']
    temp_min = json_data['main']['temp_min']
    bot.send_message(message.chat.id,"Weather in Petropavlsk: {}\nTemperature: {}\nMax temperature: {}\nMin temperature: {}\n".format(formatted_data, int(temp)-273, int(temp_max)-273, int(temp_min)-273))
    send_music(message,formatted_data)

@bot.message_handler(regexp = 'Taraz')
def astana(message):
    url = 'http://api.openweathermap.org/data/2.5/weather?appid=a7944b9d9d9abfc17b63880905110c8e&q=Taraz'
    json_data = requests.get(url).json()
    formatted_data = json_data['weather'][0]['description']
    temp = json_data['main']['temp']
    temp_max = json_data['main']['temp_max']
    temp_min = json_data['main']['temp_min']
    bot.send_message(message.chat.id,"Weather in Taraz: {}\nTemperature: {}\nMax temperature: {}\nMin temperature: {}\n".format(formatted_data, int(temp)-273, int(temp_max)-273, int(temp_min)-273))
    send_music(message,formatted_data)

@bot.message_handler(regexp = 'Uralsk')
def astana(message):
    url = 'http://api.openweathermap.org/data/2.5/weather?appid=a7944b9d9d9abfc17b63880905110c8e&q=Uralsk'
    json_data = requests.get(url).json()
    formatted_data = json_data['weather'][0]['description']
    temp = json_data['main']['temp']
    temp_max = json_data['main']['temp_max']
    temp_min = json_data['main']['temp_min']
    bot.send_message(message.chat.id,"Weather in Uralsk: {}\nTemperature: {}\nMax temperature: {}\nMin temperature: {}\n".format(formatted_data, int(temp)-273, int(temp_max)-273, int(temp_min)-273))
    send_music(message,formatted_data)

@bot.message_handler(regexp = 'Oskemen')
def astana(message):
    url = 'http://api.openweathermap.org/data/2.5/weather?appid=a7944b9d9d9abfc17b63880905110c8e&q=Oskemen'
    json_data = requests.get(url).json()
    formatted_data = json_data['weather'][0]['description']
    temp = json_data['main']['temp']
    temp_max = json_data['main']['temp_max']
    temp_min = json_data['main']['temp_min']
    bot.send_message(message.chat.id,"Weather in Uralsk: {}\nTemperature: {}\nMax temperature: {}\nMin temperature: {}\n".format(formatted_data, int(temp)-273, int(temp_max)-273, int(temp_min)-273))
    send_music(message,formatted_data)

@bot.message_handler(regexp = 'Kyzylorda')
def astana(message):
    url = 'http://api.openweathermap.org/data/2.5/weather?appid=a7944b9d9d9abfc17b63880905110c8e&q=Kyzylorda'
    json_data = requests.get(url).json()
    formatted_data = json_data['weather'][0]['description']
    temp = json_data['main']['temp']
    temp_max = json_data['main']['temp_max']
    temp_min = json_data['main']['temp_min']
    bot.send_message(message.chat.id,"Weather in Kyzylorda: {}\nTemperature: {}\nMax temperature: {}\nMin temperature: {}\n".format(formatted_data, int(temp)-273, int(temp_max)-273, int(temp_min)-273))
    send_music(message,formatted_data)

@bot.message_handler(regexp = 'Shymkent')
def astana(message):
    url = 'http://api.openweathermap.org/data/2.5/weather?appid=a7944b9d9d9abfc17b63880905110c8e&q=Shymkent'
    json_data = requests.get(url).json()
    formatted_data = json_data['weather'][0]['description']
    temp = json_data['main']['temp']
    temp_max = json_data['main']['temp_max']
    temp_min = json_data['main']['temp_min']
    bot.send_message(message.chat.id,"Weather in Shymkent: {}\nTemperature: {}\nMax temperature: {}\nMin temperature: {}\n".format(formatted_data, int(temp)-273, int(temp_max)-273, int(temp_min)-273))
    send_music(message,formatted_data)

@bot.message_handler(regexp = 'Semey')
def astana(message):
    url = 'http://api.openweathermap.org/data/2.5/weather?appid=a7944b9d9d9abfc17b63880905110c8e&q=Semey'
    json_data = requests.get(url).json()
    formatted_data = json_data['weather'][0]['description']
    temp = json_data['main']['temp']
    temp_max = json_data['main']['temp_max']
    temp_min = json_data['main']['temp_min']
    bot.send_message(message.chat.id,"Weather in Semey: {}\nTemperature: {}\nMax temperature: {}\nMin temperature: {}\n".format(formatted_data, int(temp)-273, int(temp_max)-273, int(temp_min)-273))
    send_music(message,formatted_data)

@bot.message_handler(regexp = 'Aktau')
def astana(message):
    url = 'http://api.openweathermap.org/data/2.5/weather?appid=a7944b9d9d9abfc17b63880905110c8e&q=Aktau'
    json_data = requests.get(url).json()
    formatted_data = json_data['weather'][0]['description']
    temp = json_data['main']['temp']
    temp_max = json_data['main']['temp_max']
    temp_min = json_data['main']['temp_min']
    bot.send_message(message.chat.id,"Weather in Aktau: {}\nTemperature: {}\nMax temperature: {}\nMin temperature: {}\n".format(formatted_data, int(temp)-273, int(temp_max)-273, int(temp_min)-273))
    send_music(message,formatted_data)


if __name__ == '__main__':
    print('Starting Weathicbot...')
    bot.polling()