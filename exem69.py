
op = 99

while op != 0:
    print('\n-----MENU-----')
    print('1-fazer login')
    print('2-calcular blalba')
    print('0-sair')

    op = int(input('digite a opcao desejada '))

    if op == 1:
        logado = False
        for i in range(3):
            login = input('digite seu login ')
            senha = input('digite sua senha ')
            if login == 'admin' and senha == 'admin123':
                logado = True
                break
            print('login ou senha incorretos')

        if logado == True:
            print('voce esta logado. mostrar menu do usuariio')
            op2 = 99
            while op2 != 0:
                print('1-opcao 1')
                print('2-opcao 2')
                print('3-opcao 3')
                print('4-opcao 4')

        else:
            print('usuario ou senha invalidos')