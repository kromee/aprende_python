from datetime import datetime, date, timedelta

# Fecha y hora actual (como DateTime.Now en C#)
ahora = datetime.now()
print(ahora)


# Crear una fecha exacta (año, mes, día, hora, minuto, segundo)
nacimiento = datetime(1995, 5, 15, 8, 30, 0)
print(nacimiento)



from datetime import datetime

ahora = datetime.now()

print(ahora.strftime("%d/%m/%Y"))        # 03/08/2026
print(ahora.strftime("%Y-%m-%d"))        # 2026-08-03
print(ahora.strftime("%H:%M:%S"))        # 17:25:34
print(ahora.strftime("%A, %d de %B"))    # Monday, 03 de August



from datetime import datetime

texto = "15/05/1995"
fecha = datetime.strptime(texto, "%d/%m/%Y")

print(fecha)           # 1995-05-15 00:00:00
print(type(fecha))     # <class 'datetime.datetime'>



from datetime import datetime, timedelta

hoy = datetime.now()

# Sumar 5 días
futuro = hoy + timedelta(days=5)
print(futuro.strftime("%d/%m/%Y"))

# Restar 30 días
pasado = hoy - timedelta(days=30)
print(pasado.strftime("%d/%m/%Y"))

# Diferencia entre dos fechas
navidad = datetime(2026, 12, 25)
dias_faltan = navidad - hoy
print(f"Faltan {dias_faltan.days} días para Navidad")



from datetime import datetime, timedelta

# 1. Obtén la fecha/hora actual
ahora = datetime.now()

# 2. Imprime solo la fecha en formato: DD/MM/AAAA
print(ahora.strftime("{%d/%m/%Y}"))

# 3. Crea una fecha para tu cumpleaños este año (ej: 15/05/2026)
# 2. Tu cumpleaños ESTE AÑO (2026)
mi_cumple = datetime(2026, 8, 16)

# 4. Calcula cuántos días faltan desde HOY hasta tu cumpleaños
dias_faltan = mi_cumple - ahora
print(f"Faltan {dias_faltan.days} días para mi cumpleaños")

# 5. Imprime qué día de la semana cae tu cumpleaños (usando %A)
print(mi_cumple.strftime("Mi cumpleaños cae en: %A"))