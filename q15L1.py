#questao 15 da lista de decisao

l1 = float(input('digite o lado'))
l2 = float(input('digite o lado'))
l3 = float(input('digite o lado'))

if l1 + l2 > l3 and l2 + l3 > l1 and l1 + l3 > l2:
    print('é um triangulo')
    if l1 == l2 and l2 == l3:
        print('triangulo equilatero')
    elif l1 != l2 and l2 != l3 and l3 != l1:
        print('triangulo escaleno')
    elif (l1 == l2 and l2 != l3) or (l2 == l3 and l3 != l1) or (l1 == l3 and l3 != l2):
        print('triangulo isosceles')
    else:
        print('nao existe')
else:
    print('NAO é um triangulo')