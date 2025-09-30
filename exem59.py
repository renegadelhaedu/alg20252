#5 questao
popcz = int(input('qual a popu inicial'))
popss = int(input('qual a popu inicial'))
qtde_anos = 0
txcz = float(input('qual a taxa de cz')) / 100
txss = float(input('qual a taxa de Ss')) / 100

while popcz < popss:
    popcz = popcz + (popcz * txcz)
    popss = popss + (popss * txss)
    qtde_anos += 1

print('em anos, demorou:' , qtde_anos)