from datetime import datetime

import exemplo_funcoes_aux as faux

def verificar_login(usuarios, login, senha, perfil):
    adm_logado = False
    for u in usuarios:
        if u[0] == login and u[1] == senha and u[2] == perfil:
            adm_logado = True
            break
    return adm_logado


def cadastrar_produto(produtos_servicos, id_produto):
    nome = input("Nome: ")
    tipo = input("Tipo (produto/servico): ")
    horario = ""
    if tipo == "servico":
        horario = input("Horários disponíveis (ex: 10h, 14h, 16h): ")
    valor = input("Valor: ")

    produtos_servicos.append([id_produto, nome, tipo, horario, valor])


def cadastrar_usuario(usuarios):
    login = input("Login: ")
    while faux.verifica_login_existente(usuarios, login):
        login = input("digite novamente o Login: ")
    senha = input("Senha: ")
    tipo = 'cliente'
    ultimo_acesso = datetime.now()

    usuarios.append([login,senha, tipo, ultimo_acesso])









