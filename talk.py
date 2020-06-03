def checkFile():
    with open('bot.txt','a+') as f:
        f.seek(0)
        for x in f.readlines():
            if word == x.split('::')[0]:
                return readFromFile(word)
            else:
                def build_menu(buttons, n_cols, header_buttons=None, footer_buttons=None):
                    menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
                    if header_buttons:
                        menu.insert(0, header_buttons)
                    if footer_buttons:
                        menu.append(footer_buttons)
                    return menu
                list_of_questions = ['YES', 'NO']
                button_list = []
                for each in list_of_questions:
                    button_list.append(telegram.InlineKeyboardButton(each, callback_data=each))
                reply_markup = telegram.InlineKeyboardMarkup(build_menu(button_list, n_cols=1))
                bot.send_message(chat_id=update.message.chat_id, text='Suali mene oyretmek isteyirsiniz mi?',
                                 reply_markup=reply_markup)

def addToFile(key,val):
    with open('bot.txt', 'a+') as f:
        f.seek(0)
        f.write(f'{key}::{val}')

def readFromFile(word):
    with open('bot.txt', 'a+') as f:
        f.seek(0)
        for x in f.readlines():
            if x.split('::')[0] == word:
                return x.split('::')[1]



checkFile()