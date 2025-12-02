#arquivo = persistência de dados

#criar um arquivo
#escrita = 'w' se tiver criado, ele sobrescreve tudo
#append = 'a'
#leitura = 'r'
arquivo = open('alunos.txt' , 'w')
for i in range(5):
    texto = input('Digite o nome do aluno: ')
    arquivo.write('\n' + texto)
arquivo.close()