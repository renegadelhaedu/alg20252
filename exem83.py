'''
construa um programa em python que possua um menu com 3 opções:
1-cadastrar produto
2-listar todos os produtos
0-sair
'''


op = 123
produtos = []
while op != 0:
    print('1-cadastrar produto')
    print('2-listar produtos')
    print('0-sair')
    op = int(input('digite a opcaão desajada '))

    if op == 1:
        nome_produto = input('digite a produto')
        produtos.append(nome_produto)

    elif op == 2:
        for p in produtos:
            print(p)











