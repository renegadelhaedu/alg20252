#faça um algoritmo em python para ler a idade dos alunos do p1
#do curso de ciência da computação. O programa deve ir lendo idades
# do usuário enquanto estas forem maiores que zero. Ao digitar 0,
#o programa deve encerrar.
#acrescente ao programa que ele deve calcular e exibir ao final
#a média das idades dos usuários
soma = 0
qtde = 0
idade = int(input('digite sua idade '))
pos18 = 0
while idade > 0:
    qtde += 1
    soma = soma + idade
    if idade > 18:
        pos18 += 1
    idade = int(input('digite sua idade '))
if qtde > 0:
    media = soma / qtde
    print('a media de idades dos alunos é ', media)
    print(pos18 , 'foi a quantidade de alunos com mais de 18 anos')
else:
    print('nenhuma idade válida foi digitada')