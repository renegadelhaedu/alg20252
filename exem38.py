#descobrir o peso ideal

sexo = input('digite masculino ou feminino').lower()
alt = float(input('digite sua altura'))

if sexo == 'masculino':
    peso = 72.7 * alt - 58

else:
    peso = 62.1 * alt - 44.7

print('seu peso idel e ', peso)