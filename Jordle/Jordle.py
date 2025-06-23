# Jordle is a wordle clone that I made because I can't find any that let you use custom keyboard layouts. Add words or add custom words in WORDS.txt

import os, sys, random, time

layout=[char for char in 'qwfpbjluy\narstgmneio\n xcdvzkh'] # this is the keyboard layout. the default is Colemak DH. feel free to change it to whatever you like. make sure to *not* include any letter more than once (don't have any duplicates).
score='' # this will store the words you have previously entered with their colors

def green(str): # function that turn any string into green color
    return f'\033[92m{str}\033[0m'
def yellow(str): # function that turn any string to yellow color
    return f'\033[33m{str}\033[0m'
def white(str): # function that turn any string to white color
    return f'\033[37m{str}\033[0m'
def red(str): # function that turn any string into red color
    return f'\033[91m{str}\033[0m'
def gray(str): # function that turn any string into gray color and bold it
    return f'\033[1;30m{str}\033[0m'

def evaluateGuess(): # once the users guess is entered and identified to be valid, it will use this function to color the letters correctly and add it onto the end of the score as well as updating the colors of the keyboard letters.
    global score
    score+='\n'
    for i in range(5):
        if guess[i]==word[i]:  # if it is green (in word, right place)
            score+=green(guess[i])
            if keyboard[layout.index(guess[i])].startswith("\033[37m") or keyboard[layout.index(guess[i])].startswith("\033[33m"):
                keyboard[layout.index(guess[i])]=green(guess[i])
        elif guess[i] in word: # if it is yellow (in word, wrong place)
            score+=yellow(guess[i])
            if keyboard[layout.index(guess[i])].startswith("\033[37m"):
                keyboard[layout.index(guess[i])]=yellow(guess[i])
        if not(guess[i] in word):                  # if it is gray (not in word)
            score+=gray(guess[i])
            keyboard[layout.index(guess[i])]=gray(guess[i])

keyboard=[white(x) if x in 'qwfpbjluyarstgmneioxcdvzkh' else x for x in layout] # this is what stores the keyboard that will be printed, with colored letters/keys.

wordsPath=os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), 'WORDS.txt')
with open(wordsPath, 'r') as f:
    words=f.read().split('\n')
word=random.choice(words)

guess=''

while True:
    os.system('cls' if os.name=='nt' else 'clear') # clears the terminal, ready to print the updated keyboard and score.

    print(gray('Jordle. Type quit to give up.'))
    print(''.join(keyboard),end='') # prints the keyboard with colored letters
    print(score)
    
    # note that this will be the input from the previous run, not the current run. the first time this is run, guess=''.
    if guess==word: # if you correctly guess the word
        quit() # you win and the program quits

    guess=input().lower() # asks for the user input for the next word, and makes it not case sensitive.

    if guess=='quit':
        print(f'The word was {green(word)}')
        quit()

    sys.stdout.write('\033[F\033[K') # moves the cursor up and removes the current line
    sys.stdout.flush() # flushes the buffer

    if len(guess)!=5:
        print(red('Input must be 5 letters long'))
        time.sleep(0.5)
        continue
    if guess not in words:
        print(red('Not in word list'))
        time.sleep(0.5)
        continue
    evaluateGuess() # processes the user input to color it correctly once it has checked that the input is valed