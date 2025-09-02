idade = int(input('digite sua idade '))

if idade >= 18:
    print('Pode entrar na festa. voce é de maior')
    ano = 2025 - idade
    print('voce nasceu em ', ano)
else:
    print('voce nao pode entrar nesta festa')