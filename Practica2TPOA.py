frase = input("Ingresa una frase: ")

lista_palabras = frase.split()
print("Lista de palabras:", lista_palabras)

print("\nPalabras en mayusculas:")
for palabra in lista_palabras:
    print(palabra.upper())

buscar = input("\n¿Que palabra quieres contar en la frase?: ")
veces = frase.count(buscar)
print("La palabra '" + buscar + "' aparece", veces, "veces.")

reemplazar = input("\n¿Que palabra quieres reemplazar?: ")
nueva = input("¿Por cual palabra la quieres reemplazar?: ")
frase_modificada = frase.replace(reemplazar, nueva)
print("Frase modificada:", frase_modificada)