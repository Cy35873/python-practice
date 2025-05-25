def jint(q,ca):
    global score
    ca=ca.lower().split('/')
    ua=input(q+' \n>> ')
    if ua in ca:
        print('Correct')
        score+=1
    else:
        print('Incorrect')
jint('This is a test','a/B/c/D')