#28 questao
#Faça um programa que calcule o valor total investido por
# um colecionador em sua coleção de CDs e o valor médio gasto
#em cada um deles. O usuário deverá informar a quantidade de
# CDs e o valor para em cada um.
qtde_total = 0
total = 0
valor = 100
while valor != 0:
    valor = float(input('digite o valor do CD'))
    if valor == 0:
        break
    qtde  = int(input('digite a quantidade'))
    qtde_total += qtde
    total += valor * qtde

media = total / qtde_total
print(media)

