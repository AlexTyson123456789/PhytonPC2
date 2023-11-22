#Problema 2:
#Escriba un programa en Python para construir el siguiente patrón.
    # *
    # * *
    # * * *
    # * * * *
    # * * * * *
    # * * * *
    # * * *
    # * *
    # *

#SOLUCION:

# 1. Para este caso lo tomamos como 2 triangulos uno de altura 5 y otro de altura 4.
# 2. Imprimir la figura del triangulo()

# Número de filas para la mitad superior
altura_superior = 5
for fila_x in range(1, altura_superior +1):
    for fila_y in range(fila_x):
        print("*", end=" ")
    print()

# Número de filas para la mitad inferior
altura_inferior = 4
for fila_x in range(altura_inferior, 0, -1):
    for fila_y in range(fila_x):
        print("*", end=" ")
    print()
