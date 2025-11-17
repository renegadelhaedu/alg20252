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