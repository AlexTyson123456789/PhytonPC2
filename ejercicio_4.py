#Problema 4:
#Imaginemos que lo han contratado para un colegio donde se desea realizar un sistema por el cual se
#pueda generar un listado de “n” alumnos y 3 calificaciones que corresponden a alguna de sus materias.
#Puede usar el siguiente esquema a manera de ejemplo:
#    {
#    Alumno: Juan,
#    Notas: [10, 12, 15]
#    }
#Una vez completado el ingreso de los datos, su programa debe mostrar en pantalla el listado completo de los alumnos.
#Nota: El uso de listas con diccionarios le será de utilidad.


#SOLUCION:

# Usamos una funcion para ingresar los datos del alumno y su nota
def ingresar_alumno():
    alumno = input("Ingrese el nombre del alumno: ")
    notas = []
    for i in range(3):
        nota = float(input(f"Ingrese su calificación {i+1} para {alumno}: "))
        notas.append(nota)
    return {"Alumno": alumno, "Notas": notas}

# Función para mostrar el listado completo de alumnos:
def mostrar_lista_de_alumnos(listado):
    for alumno in listado:
        print(f"Alumno: {alumno['Alumno']}, Notas: {alumno['Notas']}")

# Inicializar lista para almacenar los datos de los alumnos
listado_alumnos = []

# Solicitar al usuario la cantidad de alumnos que desea ingresar
num_alumnos = int(input("Ingrese el número de alumnos: "))

# Bucle para ingresar los datos de los alumnos
for _ in range(num_alumnos):
    alumno_actual = ingresar_alumno()
    listado_alumnos.append(alumno_actual)

# Mostrar el listado completo de alumnos
print("\nListado completo de alumnos:")
mostrar_lista_de_alumnos(listado_alumnos)
