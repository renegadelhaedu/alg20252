alunos = [['gilvan', 19],['talles',22]]

alunos.append(['maria',18])
#print(alunos[2][1])
soma = 0
for aluno in alunos:
    soma += aluno[1]
print(f'a soma total das idades é {soma}')