def pares(lista):
    pares = []
    for num in lista:
        if num % 2 == 0:
            pares.append(num)
    return pares

print(pares([1, 2, 3, 4, 5, 6, 7, 8]))
