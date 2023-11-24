#Problema 8:
#Escribe una función de Python para calcular el factorial de un número (un entero no negativo). La
#función acepta el número como argumento.

#SOLUCION:

def factorial_de_un_numero(num):
    factorial = 1
    for n in range(num):  #para "n" numeros n: 1,2,3, ....,n
        factorial*=(n+1)
    return factorial

N = int(input('Ingrese el número: ')) #se ingresa cualquier numero positovo
resultado = factorial_de_un_numero(N)
print('El número factorial es: ',resultado)  #SE IMPRIME TAL NUMERO
