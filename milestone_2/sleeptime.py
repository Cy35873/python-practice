import math
print('no information entered in the program is stored anywhere except for your local memory. all personal information entered in this program is completely destroyed upon quitting.')
print()
def sleeptime(age):
    try:
        age=float(age)
        if age>0:
            return 6.7+49/(6.9+age)
        else:
            print('That is not a valid age.')
            quit()
    except ValueError:
        print('That is not a valid age.')
        quit()
wakeuptime=input('What time do you (want to) wake up? (HH:mm) ')
try:
    wakeuptime2=float(wakeuptime.split(':')[0])+float(wakeuptime.split(':')[1])/60
except ValueError:
    print('That is not a valid time.')
    quit()
if not(0<=wakeuptime2<=24):
    print('That is not a valid time.')
    quit()
age=input('How old are you in years? ')
sleepamount=round(sleeptime(age),1)
print(f'\nBased on your age, you should be getting around {(sleepamount)} hours of sleep per day.')
sleeptime=(wakeuptime2-sleepamount)%24
sleeptime=str(math.floor(sleeptime))+':'+str(int(round((sleeptime-math.floor(sleeptime))*60,0)))
print(f'If you want to wake up at {wakeuptime} and get enough sleep, you should go to sleep at around {sleeptime}.')
print()