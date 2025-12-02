sorteio = {'a':'rene', 'b':'eric', 'c':'deliomar'}

#atualizar/sobrescrevendo
sorteio['a'] = 'ryan'

print(sorteio)
#removendo o par(chave:valor)
del(sorteio['b'])
print(sorteio)