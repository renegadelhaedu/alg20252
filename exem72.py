#questao 32 com for

num = int(input('digte um numero '))
fatorial = 1
print(f'{num}! = ', end='')
for i in range(num, 1, -1):
    fatorial = fatorial * i
    print(f'{i} . ', end='')

print(f'1 = {fatorial}')