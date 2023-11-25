#Problema 10:
#En los Estados Unidos, las fechas suelen tener el siguiente formato: mes-día-año (MM/DD/AAAA). Las
#fechas en ese formato no se pueden ordenar fácilmente porque el año de la fecha es el último en
#lugar del primero. Intente ordenar, por ejemplo, 2/2/1800, 3/3/1900 y 1/1/2000 cronológicamente
#en cualquier programa (por ejemplo, una hoja de cálculo). Las fechas en ese formato también son
#ambiguas. ¡Una fecha como el 8 de septiembre de 1636, podría interpretarse como el 9 de agosto de 1636!
#Implementar un programa que pida al usuario una fecha, en orden mes-día-año, con formato como
#8/9/1636 o Septiembre 8, 1636, donde el mes en este último podría ser cualquiera de los valores en la lista abajo:
#   [
#   "Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"
#   ]
#Luego, genere esa misma fecha en formato AAAA-MM-DD.

#SOLUCION:

def obtener_numero_mes(mes):
    meses = {
        "enero": 1,
        "febrero": 2,
        "marzo": 3,
        "abril": 4,
        "mayo": 5,
        "junio": 6,
        "julio": 7,
        "agosto": 8,
        "septiembre": 9,
        "octubre": 10,
        "noviembre": 11,
        "diciembre": 12
    }
    return meses.get(mes.lower())

def convertir_fecha(fecha):
    # Dividir la fecha 
    if "/" in fecha:
        partes = fecha.split("/")
        mes, dia, anio = partes

    numero_mes = obtener_numero_mes(mes)

    # FORMATO la fecha en AAAA-MM-DD
    fecha_formateada = f"{anio}-{numero_mes:d}-{int(dia):2d}"

    return fecha_formateada

fecha_ingresada = input("Ingrese una fecha (en formato mes-día-año o Mes día, año): ")


fecha_convertida = convertir_fecha(fecha_ingresada)
print(f"Fecha en formato AAAA-MM-DD: {fecha_convertida}")



#no funciona correctament.... falta corregir

