inicio = int(input('Inicio da operacao: '))
fim = int(input('Fim da operacao: '))
listPar = []
listImpar = []
for count in range(inicio, fim+1):
    if count % 2 == 0:
        listPar.append(count)
    else:
        listImpar.append(count)
print("Soma dos numeros pares dentro do intervalo: {} Soma dos numeros impares dentro do intervalo: {}".format(sum(listPar), sum(listImpar)))
print("Numeros pares {}  Numeros Impares {}".format(listPar, listImpar))