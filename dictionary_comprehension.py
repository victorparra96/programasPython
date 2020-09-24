# list comprehension
# Estas lineas de codigo sirven para recorrer del 1
# al 30, buscando numeros pares
pares = []
for num in range(1, 31):
    if num % 2 == 0:
        pares.append(num)
# Otra manera de hacerlo, ahorrando lineas de codigo
even = [num for num in range(1, 31) if num % 2 == 0]

# -------------------------------
# dictionary comprehension
cuadrados = {}
for num in range(1, 11):
    cuadrados[num] = num**2
# Otra manera de hacerlo, ahorrando lineas de codigo
squares = {num: num**2 for num in range(1, 11)}