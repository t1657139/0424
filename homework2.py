luckynumber ='8'
while True:
    number = input('guess lucky number')
    if number == luckynumber:
        print('Correct')
        break
    elif number == 'q':
        print('You\'ve given it up')
        break
    else:
        print('try again')
