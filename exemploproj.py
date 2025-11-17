import exemplo_minhasfuncoes as mf
import usarwebcam as minhawebcam
from validacoes import validar_login as vl


#falta muita coisa a ser implementada. isso é só p dar exemplo

usuarios = []  # [login, senha, perfil]
produtos_servicos = []  # [id, nome, tipo, horario, valor]
compras = []  # [login_cliente, produto]
agendamentos = []  # [login_cliente, servico, horario_escolhido]

usuarios.append(["admin", "123", "adm"])


id_produto = 1
opcao = '234'
while opcao != "0":
    print("\nMenuuuuuu")
    print("1 - Gerenciar Produtos e Serviços (ADM)")
    print("2 - Comprar / Agendar (CLIENTE)")
    print("3 - Cadastrar Usuário")
    print("0 - Sair")
    opcao = input("Escolha: ")


    if opcao == "1":
        print("\n== LOGIN ADM ==")
        login = input("Login: ")
        senha = input("Senha: ")

        #vl.validar_cpf(login) mostrando exemplo de importar funcao de dentro de um pacote

        # a funcao verificar_login retorna true se achar o adm, entao usamos o not
        if not mf.verificar_login(usuarios, login, senha, 'adm'):
            print("Acesso negado! Somente administradores.")
        else:
            minhawebcam.tirar_foto('imagens//ultimoacesso')
            #tirar uma foto para gravar o acesso do admin
            op_adm = 'inicial'
            while op_adm != '0':
                print("\n=== MENU ADM ===")
                print("1 - Cadastrar produto/serviço")
                print("2 - Buscar produto/serviço")
                print("5 - Listar tudo")
                print("0 - Voltar")
                op_adm = input("Escolha a opcao: ")

                if op_adm == "1":
                    mf.cadastrar_produto(produtos_servicos, id_produto)
                    id_produto += 1
                    print("Cadastrado com sucesso!")


                elif op_adm == "2":
                    termo = input("Digite parte do nome: ")
                    for p in produtos_servicos:
                        if termo.lower() in p[1].lower():
                            print(p)


                elif op_adm == "5":
                    print("\n=== LISTA COMPLETA ===")
                    for p in produtos_servicos:
                        print(p)

