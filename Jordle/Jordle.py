import os, sys, random
letters='qwfpbjluyarstgmneioxcdvzkh'
layout=[char for char in 'qwfpbjluy\narstgmneio\n xcdvzkh']
def g(str):
    return f'\033[92m{str}\033[0m'
def y(str):
    return f'\033[33m{str}\033[0m'
def n(str):
    return f'\033[90m{str}\033[0m'
keyboard=[n(x) if x in letters else x for x in [char for char in 'qwfpbjluy\narstgmneio\n xcdvzkh']]
wordsPath=os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), 'WORDS.txt')
with open(wordsPath, 'r') as f:
    words=f.read().split('\n')
word=random.choice(words)
while True:
    print()
    print(''.join(keyboard))
    guess=input().lower()
    if len(guess)==5:
        if guess in words:
            sys.stdout.write('\033[F\033[K')
            sys.stdout.flush()
            for i in range(5):
                if guess[i]==word[i]:
                    print(g(guess[i]),end='')
                elif guess[i] in word:
                    print(y(guess[i]),end='')
                else:
                    print(n(guess[i]),end='')
        else:
            print('Not in word list')
    else:
        print('Input must be 5 letters long',end='')