#questao 25 da lista de decisao

p1 = input('vc telefonou ara vitima')
p2 = input('esteve no local do xrime')
p3 = input('mora peerto da vitima')
p4 = input('deve para a vitima')
p5 = input('ja trabalhou com a vitima')
qtde = 0

if p1 == 'sim':
    qtde = qtde + 1
if p2 == 'sim':
    qtde = qtde + 1
    #qtde += 1
if p3 == 'sim':
    qtde = qtde + 1
if p4 == 'sim':
    qtde = qtde + 1
if p5 == 'sim':
    qtde = qtde + 1

if qtde == 2:
    print('vc é suspeita')
elif qtde == 3 or qtde == 4:
    print('cúmplice')
elif qtde > 4:
    print('assassino')
else:
    print('ofende ninguem')




