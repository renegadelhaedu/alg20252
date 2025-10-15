#crie um menu que possa inserir numa lista um usuario com nome,login e senha
#cada usuario será uma sub lista dentro da lista principal

usuarios = []

while True:
    print('1-cadastrar usuario')
    print('2-remover usuario')

    op = int(input('digita a opçao desejada'))

    if op == 1:
        nome = input('digite seu nome')
        email = input('digite seu email')
        senha = input('digite sua senha')
        usuarios.append([nome, email, senha])

    elif op == 2:
        busca = input('digite o e-mail do usuario quer voce quer remover')
        ind = -1
        for i in range(len(usuarios)):
            if busca == usuarios[i][1]:
                ind = i
                break

        if ind >= 0:
            usuarios.pop(ind)
            print('usuario removido com sucesso')
        else:
            print('nao achei ele')



















