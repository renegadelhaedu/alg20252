#arquivo = persistência de dados

#criar um arquivo
#escrita = 'w' se tiver criado, ele sobrescreve tudo
#append = 'a' append, adiciona no final
#leitura = 'r'
arquivo = open('professores.txt' , 'r')

#pega o arquivo aberto e lê todas as linhas, transformando em uma lista de linhas
linhas = arquivo.readlines()
arquivo.close() #fecha o arquivo
professores = []
#percorrer a lista de linhas e pegar os valores úteis
for linha in linhas:
    texto = linha.replace('\n','')
    if len(texto) > 0:
        professores.append(texto)

print(professores)
nome = input('Digite o nome do professor: ')
novo_nome = input('Digite o novo nome do professor: ')
professores.remove(nome)
professores.append(novo_nome)

arquivo = open('professores.txt', 'w')
for prof in professores:
    arquivo.write(prof + '\n')
arquivo.close()


