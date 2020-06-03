import urllib
from bs4 import BeautifulSoup
import requests
import  json
from main import *

def logger(func):
    def wrapper(*args, **kwargs):
        result=None
        with open('logs.txt', 'a') as f:
            try:
                result = func(*args,**kwargs)
                f.write(f'|{func.__name__}|{args},{kwargs}|{result}|True|\n')
                return result
            except:
                f.write(f'|{func.__name__}|{args},{kwargs}|{result}|False|\n')
    return wrapper

def learningBot(update):
    while True:
        with open('bot.txt','a+') as f:
            f.seek(0)
            data_dict = {}
            for line in f.readlines():
                k , v = line.strip().split('::')
                data_dict[k.strip()] = v.strip()
            question = input('Sualinizi verin: ')
            update.message.reply_text(question)
            if question == 'exit':
                exit()
            if question not in data_dict:
                users_answer = input('Suali mene oyretmek isteyirsiniz mi? ')
                if users_answer == 'yes':
                    answer = input('Sualiniza cavab verin: ')
                    f.write(f'{question}::{answer}\n')
                else:
                    exit()
            else:
                print(data_dict[question])
@logger
def news():
    response = requests.get('https://oxu.az/')
    soup = BeautifulSoup(response.text, features = 'html.parser')
    news_list = soup.findAll('div',{'class':'title'})
    news_links = soup.select('.news-i a')
    s=''
    for x in range(len(news_list)):
        s+=news_list[x].text+ ' '+ f"https://oxu.az/{news_links[x]['href']}\n"
    return s
@logger
def exchange():
    response = requests.get('https://api.exchangeratesapi.io/latest?base=TRY')
    response_dict = response.json()
    print('Turk lirasinin bu gune olan mezennesi: ')
    s = "Turk lirasinin bu gune olan mezennesi: "
    for x in response_dict['rates']:
        s+= f"{x} {response_dict['rates'][x]}\n"
    return s

@logger
def weatherInfo():
    response = requests.get('https://api.openweathermap.org/data/2.5/weather?q=Baku&appid=61389a93f65b06e891a9fac33362e797')
    response_dict = response.json()
    s=''
    for x in response_dict:
        s += f"{x} {response_dict[x]}"
    return s
@logger
def googleRequest(word):
    text = word
    response = requests.get(f'https://www.google.com/search?q={text}')
    soup = BeautifulSoup(response.text,features = 'html.parser')
    title = soup.select('.vvjwJb')
    links = soup.select('.UPmit')
    s=''
    for x in range(len(title)):
        s+=f"{title[x].text} {links[x].text.split('›')[0]}\n"
    return s


# while True:
#     l = ['1','2','3','4','5','exit']
#     answer = input("\nLets start talking. What do you want to do? You can choice one of this:\n 1 Talk with me \n 2 Get last news \n 3 Get info about currency \n 4 Get info about weather \n 5 Get searching results from Google \n Type exit if you want quit\n")
#     if answer not in l:
#         print('Type only number between 1-5 or exit!')
#         continue
#     elif answer == 'exit':
#         exit()
#     elif int(answer) == 2:
#         news()
#     elif int(answer) == 3:
#         exchange()
#     elif int(answer) == 4:
#         weatherInfo()
#     elif int(answer) == 5:
#         googleRequest()
#     elif int(answer) == 1:
#         learningBot()
#     else:
#         print('Type only one this numbers please!')