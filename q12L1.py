#questao 12 da lista de decisao
from exem8 import desconto

hr = int(input('quantas hroas de trabalho'))
vl = float(input('qual o valor da hora'))
sb = hr * vl

if sb <= 900:
    ir = 0
elif sb <= 1500:
    ir = sb * 0.05
elif sb <= 2500:
    ir = sb * 0.10
elif sb > 2500:
    ir = sb * 0.20

inss = sb * 0.10
fgts = sb * 0.11
descontos = ir + inss
sl = sb - descontos
print(inss)
print(fgts)
print('prezado trabalhador, sobrou apenas', sl)




