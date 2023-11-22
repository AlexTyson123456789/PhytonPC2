#Problema 3:
#Por medio de un bucle While genere un código que permita el ingreso de números por teclado. El
#ingreso de los números debe ser permitido hasta que el usuario decida ya no ingresar nuevos números.
#Con dichos números, su programa debe evaluar cada uno de estos números e indicar la cantidad de números pares e impares.

#SOLUCION:

# se ingresa lo datos 
numeros_pares = 0
numeros_impares = 0

while True:
    try:
        # Solicitamos al usuario que ingrese un número
        numeros_por_teclado = int(input("Ingresa un número: "))
        
        # se verifica si el número es par o impar
        if numeros_por_teclado % 2 == 0:
            numeros_pares += 1
        else:
            numeros_impares += 1
    except ValueError:
        # Si el usuario ingresa un dato q no sea un numero, se sale del bucle
        print("Salida del programa.")
        break

# se muestra todos los resultados
print("Cantidad de números pares:", numeros_pares)
print("Cantidad de números impares:", numeros_impares)

