peso = float(input('digite seu peso '))
altura = float(input('digite seu altura '))

imc = peso / (altura * altura)

if imc > 30:
    print('se cuide, pois vc nao esta bem')

if imc < 16:
    print('procure um nutricionistapois vc esta abaixo')

else:
    print('uhuuuuu')