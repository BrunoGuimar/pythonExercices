valorCasa = float(input('House Price: '))
salario = float(input('Your salary: '))
anosQnt = int(input('How much years: '))
parcelas = valorCasa / (12 * anosQnt)
if parcelas > salario * 0.3:
    print('Valor da parcela excedeu 30% do seu salario, Valor : {:2f}, Valor da Parcela: {:2f}'.format(salario * 0.3, parcelas))
else:
    print('Emprestimo Realizado com sucesso, valor das Parcelas: {:2f}, 30% do seu Salario Mensal: {:2f} !'.format(parcelas, salario * 0.3))