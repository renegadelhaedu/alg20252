#criar lista, inserir na lista, remover da lista, alterar na lista

#percorrer uma lista e buscar elemento na lista
alunos = ['kk','bb','aa','ze','maria','ingrid']

#print('ze' in alunos)

#alternativa
achei = False
for a in alunos:
    if 'kk' == a:
        achei = True
        break

print(achei)