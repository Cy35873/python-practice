correct = 0 # stores the amount of CORRECTLY answered questions
total   = 0   # stores the amount of answered questions

# define question function
def jint(q,ca,ex): # this is a function that asks a question, requests a user input, and decides whether if the input is correct.
    global correct # this makes sure that the 'correct' variable is referring to the global variable and not some local one.
    global total # this makes sure that the 'total' variable is referring to the global variable and not some local one.
    ca=ca.split('`') # splits the answer so multiple answers are allowed. eg a`b will make it so a and b are two accepted answers.
    ua=input('Q: '+q+' \n>> ') # this is the input.
    if ua in ca: # checks if the user input is included in the list of accepted correct answers
        print('\033[32mCorrect\033[0m') # tells the user that their answer is correct
        correct += 1 # increases the number of correct answers by 1
    else: # if it is not correct
        print('\033[91mIncorrect\033[0m') # tell the user that their answer is incorrect
    print(f'\033[94mExplaination: {ex}\033[0m')
    total += 1 # either way, increase the number of answered questions by 1

# greeting message
print('Welcome to Jint SI quiz. Make sure that your answers are in standard symbolic notation (eg. kg instead of kilogram, m^2 instead of square meter).')

# questions
jint('What is the SI unit for mass?'                    ,'kg'       ,'kg (kilogram) is the SI unit for mass.')
jint('What is the SI unit for weight?'                  ,'N'        ,'Technically, weight is a measure of force, not mass. So it is measured in N (newtons), the SI unit for force.')
jint('What is the SI unit for density?'                 ,'kg/m^3'   ,'Density is a measure of the amount of mass per certain amount of volume. kg the mass, and m^3 (cubic meter) is the measure of volume.')
jint('What is the SI unit for pressure?'                ,'Pa`N/m^2' ,'Pressure is a measure of force over an area, which is measured in N/m^2, also known as Pa (pascals).')
jint('What SI unit is used to measure energy over time?','W'        ,'1 W (watt) = 1 J/s (joule per second). J (joule) is the SI unit for energy.')
jint('What is the SI unit for velocity or speed?'       ,'m/s`ms^-1','Velocity or speed is a measure of distance over time.')

print(f'Your score is {correct}/{total}') # tells you your final score out of the total amount of question