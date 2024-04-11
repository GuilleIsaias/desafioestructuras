import sys

with open(sys.argv[1], "r") as file:
    texto=file.read()

caracteres = set(texto)
cont_caracteres = len(caracteres)

palabras = set(texto.split(" "))
cont_palabras = len(palabras)

print(f'El número de caracteres distintos es: {cont_caracteres} \nEl número de palabras distintas es: {cont_palabras}')
file.close()