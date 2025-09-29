#questao 26 lista de estrut de repetição
total = int(input('diga o total de eleitores'))
contador = 0
v1 = 0
v2 = 0
v3 = 0
while contador < total:
    voto = int(input('qual seu voto, 1, 2 ou 3'))
    if voto == 1:
        v1 += 1
    elif voto == 2:
        v2 += 1
    elif voto == 3:
        v3 += 1
    contador += 1

print('v1', v1)
print('v2', v2)
print('v3', v3)
