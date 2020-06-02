import telegram
import requests
from functions import *

def main():
    bot = telegram.Bot(token="1211173538:AAFM0ki6145h4l0bUC654T5t-_n7cBVdPaM")
    while True:
        echo(bot)
update_id = None

def echo(bot):
    global update_id
    for update in bot.get_updates(offset=update_id, timeout=10):
        update_id = update.update_id + 1
        l = ['exchange','news','weather','search']
        if update.message:
            message = update.message.text
            if message not in l or not message.startswith('search'):
                with open('bot.txt', 'a+') as f:
                    f.seek(0)
                    data_dict = {}
                    for line in f.readlines():
                        k, v = line.strip().split('::')
                        data_dict[k.strip()] = v.strip()
                    question = message
                    # update.message.reply_text(question)
                    if question not in data_dict:
                        def build_menu(buttons, n_cols, header_buttons=None, footer_buttons=None):
                            menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
                            if header_buttons:
                                menu.insert(0, header_buttons)
                            if footer_buttons:
                                menu.append(footer_buttons)
                            return menu
                        # update.message.reply_text('Suali mene oyretmek isteyirsiniz mi? ')
                        list_of_questions = ['YES','NO']
                        button_list = []
                        for each in list_of_questions:
                            button_list.append(telegram.InlineKeyboardButton(each, callback_data=each))
                        reply_markup = telegram.InlineKeyboardMarkup(build_menu(button_list, n_cols=1))
                        bot.send_message(chat_id=update.message.chat_id, text='Suali mene oyretmek isteyirsiniz mi?',
                                         reply_markup=reply_markup)
                        if update.message.text.lower()=='yes':
                            print('sagol')
                            exit()
                        # if users_answer == 'yes':
                        #     answer = input('Sualiniza cavab verin: ')
                        #     f.write(f'{question}::{answer}\n')
            if message =='salam':
                update.message.reply_text('Aleykum salam.Xeberler ucun news,hava melumati ucun weather,mezenneni oyrenmek uchun exchange,goole-da search ucun search+axtarilacaq soz,sual cavab ucun ise start frazalarindan istifade ede bilersiniz')
            if message =='exchange':
                update.message.reply_text(exchange())
            if message =='news':
                update.message.reply_text(news())
            if message =='weather':
                update.message.reply_text(weatherInfo())
            if 'search' in message:
                word = message.split(' ')[1]
                update.message.reply_text(googleRequest(word))


if __name__ == '__main__':
    main()