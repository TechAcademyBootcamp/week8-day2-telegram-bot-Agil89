import telegram
import requests
from functions import *
from telegram.error import NetworkError, Unauthorized
from time import sleep
from talk import *

update_id = None
def main():
    global update_id
    bot = telegram.Bot(token="1211173538:AAFM0ki6145h4l0bUC654T5t-_n7cBVdPaM")
    while True:
        try:
            echo(bot)
        except NetworkError:
            sleep(1)
        except Unauthorized:
            update_id += 1


def echo(bot):
    global update_id
    for update in bot.get_updates(offset=update_id, timeout=10):
        update_id = update.update_id + 1
        l = ['exchange','news','weather','search']
        if update.callback_query:
            query = update.callback_query
            if query.answer():
                if query.data == "YES":
                    query.edit_message_text(
                        text="Suala cavab verin: ",
                        reply_markup=None
                    )
        if update.message:
            message = update.message.text
            if message not in l or not message.startswith('search'):
                checkFile(message)
                if checkFile(message)==None:

                    # question = message
                    # update.message.reply_text(question)
                    if message not in data_dict and data:
                        question = message
                        f.write(f'{question}::{None}\n')

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