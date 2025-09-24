#faça um programa que o usuário digite o time do coração e o jogador
#preferido. o programa deve executar até que alguém digite que o
#time é o Sousa ou o jogador é o neymar

nome = input('digite o jogador preferido')
time = input('digite o time preferido')

while nome != 'neymar' and time != 'sousa':
    nome = input('digite o jogador preferido')
    time = input('digite o time preferido')

print('voce gosta de um time horrivel ou de um jogador bandido')