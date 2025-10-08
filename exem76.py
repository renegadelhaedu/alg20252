'''
faça um programa que leia 2 notas dos alunos do p1 (40 alunos).
o programa deve ler o nome de cada aluno também.
ao final, informe a média da turma e
 o nome do aluno com a maior nota.
'''
nome_maior = ''
maior_media = 0
soma = 0
for aluno in range(40):
    n1 = float(input('digite sua nota '))
    n2 = float(input('digite sua nota '))
    nome = input('qual seu nome ')
    media = (n1 + n2) / 2
    if media > maior_media:
        maior_media = media
        nome_maior = nome

    soma += media

media_turma = soma / 40
print(media_turma)
print(nome_maior)




