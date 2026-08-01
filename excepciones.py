# manejo de excepciones

try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("No se puede dividir entre cero")


def dividir(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: división entre cero"

# Pruebas:
print(dividir(10, 2))   # Debe dar: 5.0
print(dividir(10, 0))   # Debe dar: Error: división entre cero
print(dividir(10, "a")) # Debe dar: ??? (prueba y ve qué pasa)
