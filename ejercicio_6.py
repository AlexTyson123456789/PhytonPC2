#Problema 6:
#Escriba un programa en Python para obtener la serie de Fibonacci entre 0 y 50.
#Nota: La secuencia de Fibonacci es la serie de números:
#   0, 1, 1, 2, 3, 5, 8, 13, 21,. ...
#Cada número siguiente se obtiene sumando los dos números anteriores.

#SOLUCION:

def serie_de_fibonacci(limite):
    metodo_fibonaci = [0, 1]  # Inicia con los sig. numeros.

    while metodo_fibonaci[-1] + metodo_fibonaci[-2] <= limite:
        # suma los numeros anteriores
        metodo_fibonaci.append(metodo_fibonaci[-1] + metodo_fibonaci[-2])
    return metodo_fibonaci

# límite para la serie o total de nuemros
total = 50

# Obtén la serie de Fibonacci hasta el límite
resultado = serie_de_fibonacci(total)

# imprime la serie de Fibonaci
print(f"Serie de Fibonacci hasta {total}:")
print(resultado)
