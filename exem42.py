cnh = input('digite sim se tiver CNH').lower()
veic = input('seu veiculo ta com ipva pago').lower()
gaso = input('o carro esta abastecido')

if cnh == 'sim' and veic == 'sim' and gaso == 'sim':
    print('voce pode dirigir')
else:
    print('vc nao pode conduzir')