numeros = [1, 2, 3, 4, 5]
# Forma tradicional (bucle for):
dobles_tradicional = []
for numero in numeros:
    dobles_tradicional.append(numero ** 2)

# Forma con list comprehension:
dobles = [numero ** 2 for numero in numeros]

#imprime
print(dobles_tradicional)
print(dobles)



numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Solo los pares:
pares = [numero for numero in numeros if numero % 2==0]

# Solo los mayores a 5:
mayores = [numero for numero in numeros if numero > 5]

#imprime
print(pares)
print(mayores)



