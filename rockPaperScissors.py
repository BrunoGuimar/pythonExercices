import random
computerChoises = ['rock', 'paper', 'scissors']
computerChoise = random.choice(computerChoises)
humanChoise = str(input('Rock, Paper or Scissors? ')).strip().lower()
if humanChoise == 'rock':
    if computerChoise == 'paper':
        print('Computer: {} -- You: {} -- COMPUTER WIN'.format(computerChoise, humanChoise))
    elif computerChoise == 'scissors':
        print('Computer: {} -- You: {} -- YOU WIN'.format(computerChoise, humanChoise))
    else:
        print('Computer: {} -- You: {} -- DRAW'.format(computerChoise, humanChoise))
elif humanChoise == 'paper':
    if computerChoise == 'paper':
        print('Computer: {} -- You: {} -- DRAW'.format(computerChoise, humanChoise))
    elif computerChoise == 'scissors':
        print('Computer: {} -- You: {} -- COMPUTER WIN'.format(computerChoise, humanChoise))
    else:
        print('Computer: {} -- You: {} -- YOU WIN'.format(computerChoise, humanChoise))
elif humanChoise == 'scissors':
    if computerChoise == 'paper':
        print('Computer: {} -- You: {} -- YOU WIN'.format(computerChoise, humanChoise))
    elif computerChoise == 'scissors':
        print('Computer: {} -- You: {} -- DRAW'.format(computerChoise, humanChoise))
    else:
        print('Computer: {} -- You: {} -- COMPUTER WIN'.format(computerChoise, humanChoise))
else:
    print('INVALID OPTION TRY AGAIN!')