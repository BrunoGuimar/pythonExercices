numberList = []
indexMaior = []
indexMenor = []
maior = 0
menor = 999
for count in range(0, 5):
    number = int(input('Number: '))
    numberList.append(number)
    if numberList[count] > maior:
        maior = number
    elif numberList[count] < menor:
        menor = number
for count in range(0, len(numberList)):
    if numberList[count] == maior:
        indexMaior.append(count)
    elif numberList[count] == menor:
        indexMenor.append(count)
print('Maior numero: {}[{}]  -  Menor numero: {}[{}]'.format(maior, indexMaior, menor, indexMenor))