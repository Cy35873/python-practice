index=1
print('welcome to jint triangle maker')
char=input('what character do you want your triangle to be made of ')
if len(char)!=1:
    print('that is not a character')
    input()
    quit()
height=input('how tall do you want your triangle to be (in lines) ')
try:
    height=int(height)
    if height<1:
        print('that is not a positive integer get out')
        input()
        quit()
except ValueError:
    print('that is not an integer get out')
    input()
    quit()
for _ in range(height):
    print(char*index)
    index+=1