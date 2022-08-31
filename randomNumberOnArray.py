import random
import array
chosen = random.randint(0, 3)
aluno1 = str(input('Nome do primeiro aluno: '))
aluno2 = str(input('Nome do segundo aluno: '))
aluno3 = str(input('Nome do terceiro aluno: '))
aluno4 = str(input('Nome do quarto aluno: '))


alunos = [aluno1, aluno2, aluno3, aluno4]
ordem = random.sample(alunos, k=4)
print(ordem)
print('Primerio aluno a apresentar: {}'.format(ordem[0]))
print('Segundo aluno a apresentar: {}'.format(ordem[1]))
print('Terceiro aluno a apresentar: {}'.format(ordem[2]))
print('Quarto aluno a apresentar: {}'.format(ordem[3]))
