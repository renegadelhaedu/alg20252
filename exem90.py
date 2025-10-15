#remover pelo conteúdo do item
amizades = ['pedro','maria','jose','felipe','carla','joaquim']

traira = input('diga o nome da amizade que acabou')
if traira in amizades:
    amizades.remove(traira)
    print('esta pessoa foi removida com sucesso')
else:
    print('esse infeliz já nao era seu amigo')

for item in amizades:
    print(item, end=' ')
print(amizades)
