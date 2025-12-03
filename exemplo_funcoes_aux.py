import random

def verifica_login_existente(usuarios, login):
    usuarios.clear()
    for u in usuarios:
        if u[0] == login:
            return True
    return False

def sortear_usuario(usuarios):
    qtde = len(usuarios)
    numero = random.randint(0, qtde-1)
    return numero
