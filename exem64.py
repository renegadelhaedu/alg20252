#estrutura de repetição: for
'''
desenvolva um algoritmo em python que o usuário forneça a quantidade
de pacientes atendidos. o programa deve receber também como entrada
a idade de cada paciente, para ao final gerar a idade média de
atendimento no consultório.
'''

qtde_pacientes = int(input('digite a qtde de pacientes: '))
soma = 0
for paciente in range(qtde_pacientes):
    idade = int(input('qual tua idade '))
    soma = soma + idade

media = soma / qtde_pacientes
print(media)













