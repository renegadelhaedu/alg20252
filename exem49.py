# or (ou) retorna verdadeiro se pelo menos um for True

idade = 19
altura = 1.76
cor_cabelo = 'preto'

if idade >= 18 and altura > 1.50 and (cor_cabelo == 'verde' or cor_cabelo == 'preto' or cor_cabelo == 'loiro'):
    print('aceito conhecer')
else:
    print('nem venha')
