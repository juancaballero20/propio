def elementos_unicos(lista):
    unicos = []
    for elem in lista:
        if elem not in unicos:
            unicos.append(elem)
    return unicos

print(elementos_unicos([1, 2, 2, 3, 4, 4, 5]))
