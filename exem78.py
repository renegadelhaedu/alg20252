'''
questao 6 da lista de rpeetiçao'''

n = int(input('digite qual termo da seuencia'))
ant = 0
atual = 1
print(atual)
for i in range(n):
    prox = ant + atual
    ant = atual
    atual = prox
    print(prox)


