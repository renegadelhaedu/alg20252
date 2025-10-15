'''
construa um programa em python que possua um menu com 3 opções:
1-cadastrar produto
2-listar todos os produtos
0-sair
'''


op = 123
produtos = ['meia','blusa','croped','tenis']
while op != 0:
    print('1-cadastrar produto')
    print('2-listar produtos')
    print('3-remover produto')
    print('0-sair')
    op = int(input('digite a opcaão desajada '))

    if op == 1:
        nome_produto = input('digite a produto')
        produtos.append(nome_produto)

    elif op == 2:
        for i in range(len(produtos)):
            print(i,' - ', produtos[i])

        ind = int(input('digite o indice do elemento que vc quer editar'))
        edicao = input('digite o que vc quer alterar')
        produtos[ind] = edicao
        print(produtos)

    elif op == 3:
        for i in range(len(produtos)):
            print(i, ' - ', produtos[i])
        ind = int(input('digite o indice do elemento que vc quer excluir'))
        produtos.pop(ind)

    elif op == 4:
        nome_busca = input('digite o produto para buscar')
        achei = False
        for p in produtos:
            if nome_busca == p:
                achei = True
                break
        if achei:
            print('achei o produto na lista')
        else:
            print('NAO achei o produto na lista')




    #incremente uma opçao 4 em que o usuário busque um produto
    # e o programa informe se ele está ou nao na lista (use for para percorrer)










