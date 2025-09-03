#questao 11 da lista de decisao

sal = float(input('qual seu salario'))

if sal <= 280:
    reaj = sal * 1.20 #aumentando 20%
    perc = 20
if sal > 280 and sal <= 700:
    reaj = sal * 1.15 #aumentando 15%
    perc = 15
if sal > 700 and sal <= 1500:
    reaj = sal * 1.1 #aumentando 10%
    perc = 10
if sal > 1500:
    reaj = sal * 1.05 #aumentando 5%
    perc = 5


print('vc recebia ', sal)
print('o percentual de aumento foi', perc)
aumento = reaj - sal
print('o valor que aumentou foi ', aumento)
print('vc ganhara ', reaj)
