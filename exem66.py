nome = 'deliomar batista vieira'
qtde = 0

for i in range(len(nome)):
    if nome[i] == ' ':
        qtde += 1

print('a quantidade de espaço nesse nome completo é ', qtde)
print('a quantidade total de caracteres é', len(nome))