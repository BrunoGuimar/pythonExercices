phrase = str(input('Type a phrase: ')).strip().lower().replace(" ", "")
if phrase == phrase[::-1]:
    print('Your phrase is a PALINDROMO - {}  -  {}'.format(phrase, phrase[::-1]))
else:
    print('Normal phrase')
