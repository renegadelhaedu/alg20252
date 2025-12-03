usuarios = []

while True:
    print('1- cadastrar usuario')
    print('2- salvar usuarios em arquivo')
    print('3- importar usuarios do arquivo')
    print('4- listar')
    op = input('digite a opcao')
    if op == '1':
        nome = input('digite a nome')
        login = input('digite a login')
        senha = input('digite a senha')
        usuarios.append([nome,login,senha])

    elif op == '2':
        arq = open('usuarios.txt','w')
        for u in usuarios:
            arq.write(u[0] + ' - ' + u[1] + ' - ' + u[2] + '\n')
        arq.close()

    elif op == '3':
        arq = open('usuarios.txt','r')
        linhas = arq.readlines()
        for l in linhas:
            dados = l.split(' - ')
            usuarios.append([dados[0], dados[1], dados[2].replace('\n','') ])

        arq.close()


    elif op == '4':
        print(usuarios)



