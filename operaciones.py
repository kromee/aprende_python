a = 10
b = 36
print(f"{a} dividido entre {b} es: {a / b} (decimal) o {a // b} (entero)")

edad = 15
tiene_licencia = True

# ¿Puede conducir? (mayor de 18 Y tiene licencia)
puede_conducir = edad >= 18 and tiene_licencia

print(f"¿Puede conducir? {puede_conducir}")


nota1 = 70
nota2 = 65
nota3 = 45

promedio = (nota1 + nota2 + nota3) / 3

aprobado = promedio >= 60 and nota1 >= 50 and nota2 >= 50 and nota3 >= 50

print(f"Promedio: {promedio}")
print(f"¿Aprobó? {aprobado}")

# Cambia edad a 16 y ejecuta de nuevo. ¿Qué sale?