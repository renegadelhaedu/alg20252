#questao 5 da lista de decisao

n1 = float(input('digite sua nota'))
n2 = float(input('digite sua nota'))

media = (n1 + n2) / 2

if media >= 7 and media < 10:
    print('aprovado')

if media == 10:
    print('voce bateu as paradas')

if media >= 4 and media < 7:
    final = float(input('digite sua nota da final'))
    if final >= 5:
        print('aprovado na final')
    else:
        print('vc passa na proxima vez')

if media < 4:
    print('vc foi reprovado mas tera outro oportunidade adiante')


