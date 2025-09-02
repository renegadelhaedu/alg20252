altura = float(input('qual sua altura'))

if altura > 1.55:
    dancar = input('voce gosta de dançar, sim ou nao')
    if dancar == 'sim':
        esporte = input('voce gosta de praticar esporte')

        if esporte == 'sim':
            idade = int(input('qual sua idade'))
            if idade >= 18:
                print('voce tem grande chance de ser a mulher da vida adryhan')
            else:
                print('va brincar de boneca. vc nao tem idade ')
        else:
            print('deixe de ser morta, mulher')

    else:
        print('nao acredito. uma pena')
else:
    print('infelizmente eu nao estou no seu nivel')