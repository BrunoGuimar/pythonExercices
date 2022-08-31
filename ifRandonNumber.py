import random
randomNumber = random.randint(0, 10)
askedNumber = int(input('Choose a number between 0 and 10 --> '))
if type(askedNumber) == str:
    print('Only NUMBERS between 0 and 10!')
else:
    if askedNumber == randomNumber:
        print('RIGHT NUMBER ! COMPUTER NUMBER {} - YOUR NUMBER {}'.format(randomNumber, askedNumber))
    else:
        print('WRONG NUMBER ;-; EXPECTED: {}'.format(randomNumber))