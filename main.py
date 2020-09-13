import config
import telebot
import requests
from bs4 import BeautifulSoup as BS
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import os
import datetime
import locale
import re
# 123
# from telebot import apihelper



# r = requests.get('https://coinmarketcap.com/')
# html = BS(r.content, 'html.parser')
# bot = telebot.TeleBot(config.token)
# for el in html.select('tbody'):
#     t_name = el.select('.eTVhdN')[0].text
#     t_sum = el.select('.cmc-table__cell--sort-by__price')[0].text
#     t_name1 = el.select('a[href="/currencies/ethereum/"]')[0].text
#     t_sum1 = el.select('a[href="/currencies/ethereum/markets/"]')[0].text
#     print( t_name + '\n' + t_sum )
#     print( t_name1 + '\n' + t_sum1 )



r = requests.get('https://coinmarketcap.com/')
html = BS(r.content, 'html.parser')
bot = telebot.TeleBot(config.token)

# apihelper.proxy = {'https': 'https://134.122.75.190:8080'}


currencies = {}

for el in html.select('.cmc-table-row'):
    name = el.select('.cmc-table__column-name')[0].text
    
    s = el.select('.cmc-table__cell--sort-by__price')[0].text
    profit = el.select('.cmc--change-negative, .cmc--change-positive')[0].text
    s = re.sub('\.\d+$', '', s)

    currencies[name] = {
        'sum': s,
        'profit': profit
    }

t_nameB = 'Bitcoin'
t_nameE = 'Ethereum'

t_sumB = currencies['Bitcoin']['sum']
t_sumE = currencies['Ethereum']['sum']

t_profitB = currencies['Bitcoin']['profit']
t_profitE = currencies['Ethereum']['profit']



# profits = {}

# for el in html.select('.cmc-table-row'):
#     name = el.select('.cmc-table__column-name')[0].text
#     profit = el.select('.cmc--change-negative, .cmc--change-positive')[0].text

#     profits[name] = profit


# t_profitB = profits['Bitcoin']
# t_profitE = profits['Ethereum']

# print(t_profitB, t_profitE)
    # t_profitB = el.select('.cmc--change-negative')[0].text

    # t_profitE = el.select('.cmc--change-negative')[0].text

    # print( t_profitB )
    # print( t_profitE )



img = Image.open('/Telegam/TelegamacOS/Maket_new.jpg')
draw = ImageDraw.Draw(img)
myfont = ImageFont.truetype('/USERS/RED_S/APPDATA/LOCAL/MICROSOFT/WINDOWS/FONTS/YANDEXSANSTEXT-BOLD.TTF', 45)
myfont1 = ImageFont.truetype('/USERS/RED_S/APPDATA/LOCAL/MICROSOFT/WINDOWS/FONTS/YANDEXSANSTEXT-BOLD.TTF', 65)



locale.setlocale(locale.LC_ALL, "ru_RU")
now = datetime.datetime.now()
time = now.strftime("%B")
numbr = now.strftime('%d')

def month_from_ru_to_ru(month):
    out = ''
    if month == 'Январь': out = 'января'
    if month == 'Декабрь': out = 'декабря'
    if month == 'Февраль': out = 'февраля'
    if month == 'Март': out = 'марта'
    if month == 'Апрель': out = 'апреля'
    if month == 'Май': out = 'мая'
    if month == 'Июнь': out = 'июня'
    if month == 'Июль': out = 'июля'
    if month == 'Август': out = 'августа'
    if month == 'Сентябрь': out = 'сентября'
    if month == 'Октябрь': out = 'октября'
    if month == 'Ноябрь': out = 'ноября'
    if month == 'Декабрь': out = 'декабря'
    return numbr + ' ' + out



# myfont1 = ImageFont.truetype('/Library/Fonts/Arial.ttf', 25)
# color = aggdraw.Font('red')
# draw. ellipse((10,10,300,300), fill="red", outline="red")
draw.text((123, 100), text=month_from_ru_to_ru(time), font=myfont)
draw.text((230, 232), text=t_nameB + ": " + t_sumB, font=myfont1)
draw.text((230, 370), text=t_nameE + ": " + t_sumE, font=myfont1)
# draw.text((1030, 232), text=t_profitB, font=myfont1)
if t_profitB.startswith('-'):
	draw.text((1005, 232), fill="red", text=t_profitB, font=myfont1)
else:
	draw.text((1005, 232), fill="green", text=t_profitB, font=myfont1)
# draw.text((1030, 370), text=t_profitE, font=myfont1)
if t_profitE.startswith('-'):
	draw.text((1005, 370), fill="red", text=t_profitE, font=myfont1)
else:
	draw.text((1005, 370), fill="green", text=t_profitE, font=myfont1)	
img.save('/Telegam/TelegamacOS/111.png')



@bot.message_handler(commands=['start'])
def main(message):
     bot.send_message(message.chat.id, "Курс валюты на сегодня:\n" + t_nameB + '\n' + t_sumB)

# @bot.message_handler(commands=['help'])
def send_telegram(text: str):
    token = config.token
    url = "https://telegg.ru/orig/bot"
    # https://api.telegram.org/bot
    channel_id = "@IvlievPost"
    url += token
    method = url + "/sendPhoto"
    files = {'photo': open('/Telegam/TelegamacOS/111.png', 'rb')}
    data = {'chat_id' : "111111111"}
    
    r = requests.post(method,files=files,data={
         "chat_id": channel_id,
         "text": t_nameB + " : " + t_sumB, 
          })
    
    # requests.api.request('post', verify=False)
    if r.status_code != 200:
        raise Exception("post_text error")



# del draw

# img.show()

send_telegram('')
os.remove('/Telegam/TelegamacOS/111.png')

# bot.send_photo(message.chat_id, photo=bio)

if __name__ == '__main__':
    bot.polling(none_stop=True)


    

    
