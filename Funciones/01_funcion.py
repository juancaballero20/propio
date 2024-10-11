numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
numero3 = int(input("Ingrese el tercer número: "))

def maximo_num(numero1, numero2, numero3):
    if numero1 >= numero2 and numero1 >= numero3:
        return numero1
    elif numero2 >= numero1 and numero2 >= numero3:
        return numero2
    else:
        return numero3
    
maximo = maximo_num(numero1, numero2, numero3)
print(f"El número máximo es: {maximo}")