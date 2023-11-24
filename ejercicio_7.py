#Problema 7:
#Escriba una función de Python que tome un número como parámetro y verifique que el número sea primo o no.

#SOLUCION:

def cualquier_numero(numero):
    if numero <= 1: #para menores q 1
        return False
    # se verifica si es divisible por 2 y el mismo
    for x in range(2, int(numero**0.5) + 1):
        if numero % x == 0:
            return False
    # Si no se encontraron divisores, el número es primo
    return True

# un ejemplo
numero_ingresado = 37  # aqui se cambia a cualquier numero.

if cualquier_numero(numero_ingresado):
    print(f"{numero_ingresado} SI es un número primo.")
else:
    print(f"{numero_ingresado} NO es un número primo.")

