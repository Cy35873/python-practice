import random

a=[1,2,3,4,5]

print('sorting...')

while True:
    random.shuffle(a)
    print(a)
    if a==sorted(a):
        print('it is sorted')
        break