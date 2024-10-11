print("Comprobar si un número esta dentro de un rango")

def comrpobar(inicio, numero, final):

    if inicio < numero and numero < final:
        return True
    else:
        return False
    
inicio = float(input("Ingrese el comienzo del rango: "))
final = float(input("Ingrese el final del rango: "))
numero = float(input("Ingrese el número a buscar dentro del rango:"))

if comrpobar(inicio, numero, final):
    print(f"{numero} se encuentra en el rango de {inicio} hasta {final}")

else: 
    print(f"{numero} no se encuentra en el rango de {inicio} hasta {final}")

