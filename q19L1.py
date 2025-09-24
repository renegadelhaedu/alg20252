#questao 19 da lista de decisao

num = int(input('digite um numero'))

if num < 1000:
    qtde100 = num // 100
    resto = num - qtde100 * 100
    qtde10 = resto // 10
    qtde1 = resto - qtde10 * 10

    print(qtde100,'centenas,',qtde10,'dezenas e', qtde1,'unidades')
else:
    print('numero maior q 1000')