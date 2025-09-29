#questao 4 lista de estrut de repetição
#ss 1.2%
#cz 1.5%
popcz = 70000
popss = 80000
qtde_anos = 0

while popcz < popss:
    popcz = popcz + (popcz * 0.015)
    popss = popss + (popss * 0.012)
    qtde_anos += 1

print('em anos, demorou:' , qtde_anos)


