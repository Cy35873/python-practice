import sys, os

# ADD REDO FUNCTION PLS

commands=['a','r','help','q','clr','ud','sort','sortw'] # list of allowed function that the user may execute to prevent the user from executing unwanted commands

hist=[]  # list that stores the previous states of todo.txt so that the ud (undo) function works

msg='' # string that stores any error or information messages that the program may show the user

todopath=os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), 'todo.txt') # creates a variable for the path of todo.txt which makes the code more readable

def loghist(): # function that saves the content of todo.txt the hist variable before executing funcmap(user_input)
    global hist # tells the function that msg is a global variable
    with open(todopath, "r") as file:
        hist.append(file.read()) # saves previous state to variable hist

def ud(): # undo 
    with open(todopath, "w") as file:
        file.write(hist.pop()) # writes hist to todo.txt, undoing the previous action

def a(a): # function to add a task
    loghist() # function that saves the content of todo.txt the hist variable before executing funcmap(user_input)
    with open(todopath, "a") as file:
        file.write(str(a)+'\n') # writes a new line for the new task

def r(a): # remove/complete a task
    global msg # tells the function that msg is a global variable
    loghist() # function that saves the content of todo.txt the hist variable before executing funcmap(user_input)
    a=a.strip() # removes any useless characters from the end of the arument like spaces
    try: # attempt to perform what this function intends to do if a is a valid index and integer
        a=int(a) # converts the argument into an integer
        with open(todopath, "r") as file:
            lines=file.readlines() # get the lines of todo.txt
            try: # attempts to remove line with the index that the user_input provided
                del lines[a] # removes the task with the index that the user provided
                with open(todopath, "w") as file:
                    file.writelines(lines) # writes it to todo.txt
            except IndexError: # the index is not valid
                    msg=f'\033[91mSyntax error: There is no task with the index {a}.\033[0m'
    except ValueError: # if it not a valid integer and a could not be converted
        if a=='': # checks if any argument was provided at all
            msg=f'\033[91mSyntax error: no index was provided. Try ending rm; with a valid integer.\033[0m'
        else: # otherwise, the input must exist but be invalid (contains non-digit characters)
            msg=f'\033[91mValue error: \"{a}\" is not a valid integer.\033[0m'

def pr(): # show list of tasks
    global msg # tells the function that msg is a global variable
    if len(content)!=0: # check if the content of todo.txt is not empty
        lineindex=0 # sets the current line to 1
        for _ in range(len(content)-1): # prints the next line until all of the lines are printed
                print('\033[95m'+str(lineindex)+'\033[0m',end=' ') # prints the line number (inital line number is 0)
                lineindex+=1 # increments line number by 1 for next print
                print(content[lineindex-1]) # prints the line
    # if the content of todo.txt is empty, nothing will print

def help(): # prints helpful information
    global msg # tells the function that msg is a global variable
    msg='\033[32mJintTodo is a minimal todo application built in Python. Todo files are stored in the todo.txt file in the same directory.\na <task name>: adds a new task. Example: a buy milk\nr <task number>: removes a task.\nq: quits jintTodo.\nclr: deletes all of your tasks.\nud: undo command\nsort: Displays tasks sorted by unicode value (alphabetical order).\nsortw: sorts tasks by alphabetical order and writes it to file.\nTip: use ISO 8601 date formatting (year-month-day) in the beginning of the task name and use the sort; command to see your tasks sorted by date.\033[0m'

def q():
    quit()

def clr(): # delete all tasks, overwrite todo.txt with nothing
    loghist() # function that saves the content of todo.txt the hist variable before executing funcmap(user_input)
    confirm=input('\033[91mAre you sure you want to remove all of your tasks? [y]/[type anything else] \033[0m')
    if confirm.lower().strip()=='y': # checks if the user input is yes
        with open(todopath, "w") as file:
            file.write('') # overwrites todo.txt with nothing

def sort(): # prints the todolist in alphabetical order
    global msg # tells the function that msg is a global variable
    if len(content)==0: # checking if todo.txt is empty
        msg='\033[33mThere are no tasks to sort. Add a task with ad;<taskname>.\033[0m'
    else:
        lineindex=0 # sets the current line to 0
        for _ in range(len(content)-1):
                msg=msg+'\033[34m'+str(lineindex)+' \033[0m' # prints the line number (inital line number is 0)
                lineindex+=1 # increments line number by 1 for next print
                msg=msg+(sorted(content)[lineindex])+'\n' # prints the line
        msg=msg.strip() # removes useless spaces or newlines at the end of the message

def sortw(): # prints the todolist in alphabetical order
    global content
    global msg
    grig=sorted(content)[1:]
    del content[0]
    with open(todopath, "w") as file:
        file.write('\n'.join(grig)+'\n') # writes a new line for the new task

def funcmap(a): # maps the user input to a function and executes it
    global msg # tells the function that msg is a global variable
    funcarg=a.split(' ') # splits the user_input into parts separated by ;
    funcname=funcarg[0] # first part of user_input is the function/command name
    if len(funcarg)>1: # checks if there is an argument
        argument=' '.join(funcarg[1:]) # makes the rest of it one single argument. example: for the command a;b;c, 'a' is the funcarg and 'b;c' is the argument, instead of splitting it into more than 2 parts (a, b, and c).
    func=globals().get(funcname)
    if funcname in commands: # checks if the function is an allowed to be run
        try:
            func() # attemps to run the function without an  argument
        except TypeError: # if it fails, that means that the function needs an argument
            try:    
                func(argument) # executes the function with the argument
            except UnboundLocalError:
                msg=f"\033[91mSyntax error: no argument provided\033[0m"
    else:
        msg=f"\033[91mSyntax error: command \"{a}\" not found\033[0m"

os.system('cls' if os.name == 'nt' else 'clear') # clears the terminal
loghist() # make the hist variable equal to the sorted(content)[1:] of todo.txt so that undoing does nothing (overwrites with what is already there), instead of overwriting with nothing

while True: # repeat this forever
    with open(todopath, "r") as file:
        content=file.read().split('\n') # updates the content variable. content is the variable that stores all of the lines in todo.txt as a list.
    os.system('cls' if os.name == 'nt' else 'clear') # clears the terminal
    print(msg,end='') # prints out information for the user related the previous input
    if len(content)!=2:
        plural='s'
    else:
        plural=''
    print(f'\n\033[90mJintTodo: You have {len(content)-1} task{plural}. Type help; for help, type ud; for undo\033[0m')
    pr() # prints out todo.txt
    msg='' # resets the message so that it doesn't appear multiple times
    user_input=input('\033[96m>> ') # gives the user a prompt to enter a command. color is light blue.
    print('\033[0m') # resets text color to normal
    funcmap(user_input) # executes a function based on user_input