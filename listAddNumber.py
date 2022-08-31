verify = ''
array = []
while verify != 'N':
    number = int(input('A number: '))
    if number in array:
            print('Number already exists')
    if number not in array:
            array.append(number)
    verify = str(input('(Y/N))')).upper().strip()
print(array)
