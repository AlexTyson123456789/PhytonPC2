#Problema 5:
#Genere una función que tenga como parámetros el ingreso de un número entero y un dígito.
#Verifique la cantidad de veces que se usa dicho número en el dígito solicitado.
#Ejemplo:
    #Número ingresado: 15789000 y Dígito: 0
    #Cantidad de veces 0 en el número: 4
#Nota: Para resolver este problema, algunos tipos de datos dentro de python contemplan un método count.

#SOLUCION:

#Se realiza mediate una funcion "contador_ de _digitos"
def contador_de_digitos(numero, digito):
    numero_str = str(numero)
    
    # se usa el método "count" para contar la cantidad de veces que aparece el 0.
    cantidad = numero_str.count(str(digito))
    
    return cantidad

# Ejemplo muestra del ejerccicio
numero_ingresado = 15789000
digito_pedido = 0

cantidad_repetido = contador_de_digitos(numero_ingresado, digito_pedido)
print(f"Número ingresado: {numero_ingresado} y Dígito: {digito_pedido}")
print(f"Cantidad de veces {digito_pedido} en el número: {cantidad_repetido}")


