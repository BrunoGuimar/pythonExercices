aluno = {}
aluno['name'] = str(input('Name: '))
aluno['media'] = float(input('Med: '))
if aluno['media'] > 6:
    aluno['state'] = 'APROVADO'
else:
    aluno['state'] = 'REPROVADO  ;-;'

print(f'{aluno["name"]} - {aluno["media"]} - {aluno["state"]}')