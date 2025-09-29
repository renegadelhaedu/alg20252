'''
questao 1

kw = int(input('digite seu consumo'))
band = input('digite a bandeira')

total = 0
if kw <= 100:
    total = kw * 0.50
elif kw > 100 and kw <= 200:
    total = kw * 0.70
else:
    total = kw * 0.90

if band == 'amarela':
    total = total * 1.1
elif band == 'vermelha':
    total = total * 1.2
print('o valor total pago sera', total)

questao 2
nome = input('diz teu nome')
n1 = float(input('digite sua nota'))
n2 = float(input('digite sua nota'))
n3 = float(input('digite sua nota'))
falta = int(input('diz tuas faltas'))
med = (n1 + n2 + n3) / 3

if med >= 7 and falta <= 5:
    print('aprovado')
elif med >= 5 and med < 7 and falta <= 5:
    print('recuperacao')
elif med >= 7 and falta > 5 and falta <= 10:
    print('com ressalvas')

questao 3
time = input('diga teu time')
if time == 'flamengo' or time == 'corinthians' or time == 'atl min':
    print('time grande')
else:
    print('comum')
'''
pag = input('informe o tipo de pagamento')
if pag == 'dinheiro' or pag == 'pix':
    print('abra a caretiera ou diaga o pix')
elif pag == 'credito' or pag == 'debito':
    print('passe ou aproxima o cartao')
else:
    print('nao aceito')

































