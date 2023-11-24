#Problema 9:
#Al enviar mensajes de texto o twittear, no es raro acortar las palabras para ahorrar tiempo o espacio,
#por ejemplo, omitiendo las vocales.
#Implemente un programa que solicite al usuario una cadena de texto y luego retorne ese mismo
#texto pero con todas las vocales (A, E, I, O y U) omitidas, ya sea que se ingresen en mayúsculas o minúsculas.
#Ejemplo:
#   - Input: Twitter Output: Twttr
#   - Input: What's your name? Output: Wht's yr nm?


#SOLUCION:

def acortar_vocales(cadena):
    # Crea una cadena nueva sin las vocales
    cadena_sin_vocales = ''.join(char for char in cadena if char.lower() not in ['a', 'e', 'i', 'o', 'u'])
    return cadena_sin_vocales

ingreso_de_palabra = input("Ingrese una cadena de texto: ") #se puede ingresar cualquier palabra para verrificar.

resultado = acortar_vocales(ingreso_de_palabra)

# impresion de la neuva palabra
print(f"Texto con vocales acortadas: {resultado}")

