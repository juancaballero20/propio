def palindromo(cadena):
    cadena = cadena.replace(" ", "").lower()
    return cadena == cadena[::-1]

print(palindromo("Ana")) 
print(palindromo("Anita lava la tina")) 
