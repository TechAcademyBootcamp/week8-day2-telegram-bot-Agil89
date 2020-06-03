def checkFile(word, learning):
    with open('bot.txt','a+') as f:
        f.seek(0)
        for x in f.readlines():
            if word == x.split('::')[0]:
                return readFromFile(word)
            print('yazdi')
            return addToFile(word, learning)

def addToFile(word, learning):
    print('add to file')
    with open('bot.txt', 'a+') as f:
        # f.seek(0)
        if not learning:
            f.write(f'{word}::')
        else:
            f.write(f'{word}\n')

def readFromFile(word):
    with open('bot.txt', 'a+') as f:
        f.seek(0)
        for x in f.readlines():
            if x.split('::')[0] == word:
                return x.split('::')[1]
