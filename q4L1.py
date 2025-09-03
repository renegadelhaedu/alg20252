#questao 4 da lista de decisao

l = input('digite uma letra ').lower()
if l != 'a':
    if l != 'e':
        if l != 'i':
            if l != 'o':
                if l != 'u':
                    print('consoante', l)
                else:
                    print('vogal u')
            else:
                print('vogal o')
        else:
            print('vogal i')
    else:
        print('vogal e')
else:
    print('vogal a')