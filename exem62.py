#48 questao

num = input('diigte um numero')
qtde = len(num) * -1
inicio = -1
while inicio >= qtde:
    if inicio == -1 and num[inicio] != '0':
        print(num[inicio], end='')
    elif inicio < -1:
        print(num[inicio], end='')
    inicio -= 1