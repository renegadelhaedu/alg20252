'''
faça um programa em python que leia o nome do cantor/cantora
 que tocou em cada um dos 15 dias de festa em carrapateira-pb.
 se o cantor/cantora se chamar adryhan, encerre o código e diga que
 essa noite foi pancada
'''

for noite in range(15):
    nome = input('informa o nome do cantor ou cantora')
    if nome.lower() == 'adryhan':
        print('esse caba é pancada')
        break

    print('foi bonzinho')





