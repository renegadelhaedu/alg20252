megasena = []
num = int(input('diga o numero entre 1 e 60'))
while len(megasena) < 6:
    megasena.append(num)
    num = int(input('diga o numero entre 1 e 60'))
    while num in megasena:
        num = int(input('diga novamente o numero entre 1 e 60'))
    if len(megasena) == 6:
        break
print(megasena)