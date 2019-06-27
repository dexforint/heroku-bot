# import requests

# TOKEN = '671928042:AAHrd_FbSJGbkvN9h96lZGwk0ea-gTTzXCw'
# MAIN_URL = 'https://api.telegram.org/bot' + TOKEN

# r = requests.get(MAIN_URL + '/getMe')
# print(r.json())

# import requests
# from bs4 import BeautifulSoup


# url = "http://free-proxy.cz/ru/proxylist/country/all/socks5/speed/all"
# r = requests.get(url)

# print(r.text)

import telebot
from telebot import apihelper

bot = telebot.TeleBot('671928042:AAHrd_FbSJGbkvN9h96lZGwk0ea-gTTzXCw')
apihelper.proxy = {'https':'socks5://144.217.56.17:12128'}

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start')

bot.polling()

# import requests

# def get_tor_session():
#     session = requests.session()
#     # Tor uses the 9050 port as the default socks port
#     session.proxies = {
#                        'https': 'socks5://144.217.56.17:12128'}
#     return session

# # Make a request through the Tor connection
# # IP visible through Tor
# session = get_tor_session()
# print(session.get("http://httpbin.org/ip").text)
# # Above should print an IP different than your public IP

# # Following prints your normal public IP
# print(requests.get("http://httpbin.org/ip").text)