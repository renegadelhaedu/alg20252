#faça um algoritmo que leia peso e altura, calcule o IMC,
#o programa deve mandar o usuário procurar a UPA se o IMC
#for maior que 30

peso = float(input('digite seu peso '))
altura = float(input('digite seu altura '))

imc = peso / (altura * altura)

if imc > 30:
    print('se cuide, pois vc nao esta bem')
else:
    print('vc está relativamente bem')