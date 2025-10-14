#lista
pretendentes = []

#append adiciona ao final da lista
pretendentes.append('maria clara')
pretendentes.append('valeria')
for i in range(3):
    nome = input('qual o nome dessa pretendente? ')
    pretendentes.append(nome)

print(pretendentes)