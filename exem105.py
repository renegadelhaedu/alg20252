#arquivo = persistência de dados

#criar um arquivo
#escrita = 'w' se tiver criado, ele sobrescreve tudo
#append = 'a' append, adiciona no final
#leitura = 'r'
arquivo = open('professores.txt' , 'a')
for i in range(5):
    texto = input('Digite o nome do professor: ')
    arquivo.write('\n' + texto)
arquivo.close()