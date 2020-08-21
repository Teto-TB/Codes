import telebot
from flask import Flask, request
import requests
from bs4 import BeautifulSoup
from PIL import Image, ImageDraw, ImageFont
import urllib.request
import os
import time

bot_token = ""

bot = telebot.TeleBot(bot_token)
server = Flask(__name__)


@bot.message_handler(commands=['start'])
def command(message):
    bot.send_message(message.chat.id, 'Hi, use the command /code to get the latest TV code')
    
    
    
@bot.message_handler(commands=['code'])
def code(message):
    
    # Set the URL you want to webscrape from
    url = "https://www.blackfiretv.com/%d9%83%d9%88%d8%af-%d8%aa%d9%81%d8%b9%d9%8a%d9%84-code-black-tv-iptv-2020-2021/"
    r = requests.get(url)
    print("Searching for")
    soup = BeautifulSoup(r.content, "html.parser")
    ancher = soup.find_all('div', {'class': "post-content-bd"})
    for pt in ancher:
        img = pt.find('img', {'sizes': '(max-width: 500px) 100vw, 500px'})
        imgsrc = img.get('src')
        print(imgsrc)
        bot.send_message(message.chat.id, imgsrc)
        # urllib.request.urlretrieve(img.get("src") ,"123.jpg")
    print("Done")


while True:
    try:
        bot.polling(none_stop=True)
        # ConnectionError and ReadTimeout because of possible timout of the requests library
        # maybe there are others, therefore Exception
    except Exception:
        time.sleep(15)
