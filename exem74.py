for num in range(10, 5001):
    qtde = 0

    for i in range(1, num + 1):
        if num % i == 0:
            qtde += 1

    if qtde == 2:
        print(num)


