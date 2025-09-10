# or (ou) retorna verdadeiro se pelo menos um for True

idade = int(input('digite sua idade'))
bolso = float(input('quanto vc possui de dinheiro no bolso'))

if idade >= 18 or bolso >= 50:
    print('vc pode entrar no show de CA')
else:
    print('vc nao pode entrar no show de CA')