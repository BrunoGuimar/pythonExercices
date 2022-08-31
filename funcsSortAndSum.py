from random import randint, sample


def sumPar(list):
    result = 0
    for value in list:
        if value % 2 == 0:
            result += value
    print(f'A soma entre os valores pares da lista e: {result}')


def sort(length, list):
    for i in range(0, length):
        list.append(randint(1, 10))
    randomList = sample(list, length)
    print(randomList)
    sumPar(randomList)

numsList = list()
sort(4, numsList)
