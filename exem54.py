op = 99
while op != 0:
    print('------MENU-----')
    print('1-Calcular IMC')
    print('2-verificar pressao arterial')
    print('3-checar nome')
    print('0-sair')

    op = int(input('digite a opcao desejada: '))

    if op == 1:
        peso = float(input('digite seu peso '))
        altura = float(input('digite sua altura '))

        imc = peso / altura**2
        print('seu IMC é ', imc)
    elif op == 2:
        pmax = int(input('digite a pressao maxima'))
        pmin = int(input('digite a pressao minima'))
        if pmax >= 8 and pmax <= 11 and pmin >= 6 and pmin <= 8:
            print('voce está bem')
        else:
            print('chama o SAMU')

    elif op == 3:
        nome = input('digite seu nome ')
        if nome == 'joao felipe':
            print('voce é o desmantelo em pessoa')
        else:
            print('aí tá certo. voce é um prefeito')
    elif op == 0:
        print('SISTEMA ENCERRADO')
    else:
        print('opção inválida')

