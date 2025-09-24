#desenvolva um algoritmo em python que receba o email e a senha
#cadastrada pelo usuário. o programa deve pedir para repetir o email
# caso nao contenha @
#o programa deve pedir para repetir a senha se a quantidade de
#caracteres for menos que 8

login = input('digite seu email')
while '@' not in login:
    login = input('animal, coloque o @ no email, meu querido')

senha = input('digite sua senha')
while len(senha) < 8:
    senha = input('digite sua senha novamente com mais de 8 carac')

print('login e senha cadastrados com sucesso')