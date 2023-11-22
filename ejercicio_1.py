#Problema 1:
#Escribe un programa en Python para encontrar los números que son divisibles por 7 y múltiplos de 5,
#en el rango de 1500 y 2700 (ambos incluidos).

#SOLUCION:

#PARA ENCONTRAR LOS NUMEROS DIV. POR 7° Y MULT. DE 5 SE REALIZA.
lista_de_numeros = []

#busqueda de todos los # en rango de (1500 a 2700)
for numero in range(1500, 2701):
    #se evalua si los numeros es div. por 7 y mul.de 5
    if numero % 7 == 0 and numero % 5 == 0:
        #aqui se guarda la lista de numeros.
        lista_de_numeros.append(numero)

# Imprimir los resultados de la lista de nuemros.
print("Números divisibles por 7 y múltiplos de 5 en el rango de 1500 a 2700:")
print(lista_de_numeros)
