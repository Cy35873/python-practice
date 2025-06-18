# Jordle is a wordle clone that I made because I can't find any that let you use custom keyboard layouts. Add words or add custom words in WORDS.txt

import os, sys, random, time

layout=[char for char in 'qwfpbjluy\narstgmneio\n xcdvzkh'] # this is the keyboard layout. the default is Colemak DH. feel free to change it to whatever you like. make sure to *not* include any letter more than once (don't have any duplicates).
score='' # this will store the words you have previously entered with their colors

def g(str): # function that turn any string into green color
    return f'\033[92m{str}\033[0m'
def y(str): # function that turn any string to yellow color
    return f'\033[33m{str}\033[0m'
def n(str): # function that turn any string to white color
    return f'\033[37m{str}\033[0m'
def r(str): # function that turn any string into red color
    return f'\033[91m{str}\033[0m'
def w(str): # function that turn any string into gray color
    return f'\033[1;30m{str}\033[0m'

def appendScore():
    global score
    score+='\n'
    for i in range(5):
        if guess[i]==word[i]:  # if it is green (in word, right place)
            score+=g(guess[i])
            if keyboard[layout.index(guess[i])].startswith("\033[37m") or keyboard[layout.index(guess[i])].startswith("\033[33m"):
                keyboard[layout.index(guess[i])]=g(guess[i])
        elif guess[i] in word: # if it is yellow (in word, wrong place)
            score+=y(guess[i])
            if keyboard[layout.index(guess[i])].startswith("\033[37m"):
                keyboard[layout.index(guess[i])]=y(guess[i])
        if not(guess[i] in word):                  # if it is gray (not in word)
            score+=w(guess[i])
            keyboard[layout.index(guess[i])]=w(guess[i])

keyboard=[n(x) if x in 'qwfpbjluyarstgmneioxcdvzkh' else x for x in layout] # this is what stores the keyboard that will be printed, with colored letters/keys.

wordsPath=os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), 'WORDS.txt')
with open(wordsPath, 'r') as f:
    words=f.read().split('\n')
word=random.choice(words)

guess=''
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(w('Jordle. Type quit to give up.'))
    print(''.join(keyboard),end='')
    print(score)
    if guess==word:
        quit()
    guess=input().lower()
    if guess=='quit':
        print(f'The word was {g(word)}')
        quit()
    sys.stdout.write('\033[F\033[K')
    sys.stdout.flush()
    if len(guess)==5:
        if guess in words:
            appendScore()
        else:
            print(r('Not in word list'))
            time.sleep(0.5)
    else:
        print(r('Input must be 5 letters long'))
        time.sleep(0.5)