print("Invertir una cadena")

def invertir_cadena(cadena):
    invertida = ""
    for char in cadena:
        invertida = char + invertida
    return invertida

cadena= input("Ingrese una cadena: ")
invertir = invertir_cadena(cadena)
print(f"La cadena de forma invertida es {invertir}")


