a = float(input('digite um numero'))
b = float(input('digite um numero'))
c = float(input('digite um numero'))
delta = b*b - 4 * a * c

x1 = (-b + delta  ** (1/2)) / (2 * a)
x2 = (-b - delta  ** (1/2)) / (2 * a)

print('o valor de x1 e' , x1)
print('o valor de x2 e' , x2)