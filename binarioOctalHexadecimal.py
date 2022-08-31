number = int(input('Type a number: '))
type = str(input('The type of conversion: Binary, Octal or Hexadecimal: ')).upper().strip()
binary = bin(number)
octal = oct(number)
hexadecimal = hex(number)
if type == 'BINARY':
    print('The binary number : {}'.format(binary[2:]))
elif type == 'OCTAL':
    print('The octal number: {}'.format(octal[2:]))
elif type == 'HEXADECIMAL':
    print('The hexadecimal number: {}'.format(hexadecimal[2:]))
else:
    print('Type of conversion doesn`t exist !')