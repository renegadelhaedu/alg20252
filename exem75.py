nome = input('digite o primeiro nome do aluno para verificar a quantidade de presenças: ')
#abrindo o arquivo em modo leitura
meu_arquivo = open('C:\\Users\\Rene\\Desktop\\alunos.txt')
qtde = 0
#lendo as linhas do arquivo
linhas = meu_arquivo.readlines()
for linha in linhas:
    if nome in linha:
        qtde += 1

#fechando o arquivo
meu_arquivo.close()
print(f'o aluno {nome} estava presente {qtde} vezes')