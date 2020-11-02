import csv

def acciones():
    ARCHIVO = "empleados.csv"
    VACACIONES = "dias.csv"
    CAMPOS = ["Legajo", "Apellido", "Nombre", "Vacaciones"]

    while True:
        print ("Elija una opción: \n1. Guardar datos del empleado.\n2. Cargar días de vacaciones disponibles.\n3. Salir")
        opcion = input ("")

        if opcion == "3":
            exit()
        if opcion == "1":
            guardar_datos(ARCHIVO,CAMPOS)
        if opcion == "2":
            cargar_vacaciones(ARCHIVO,VACACIONES)
        else:
            print("\n >Error. Ingrese opcion una opción valida.\n")


def guardar_datos(archivo,campos):

    archivo = input("Ingrese el nombre del documento que desea guardar en csv: ")

    lista_de_empleados = []
    guardar = "si"

    while guardar =="si":
        empleado = {}

        for campo in campos:
            empleado[campo] = input(f"Ingrese {campo} del empleado: ")
        lista_de_empleados.append(empleado)
        guardar = input("\n\t¿Desea cargar otro empleado? si/no: ")

    try:
        with open(archivo, mode="w", newline="") as file:
            escribiendo_archivo = csv.DictWriter(file, fieldnames = campos)
            escribiendo_archivo.writeheader()
            escribiendo_archivo.writerows(lista_de_empleados)

    except IOError:
        print("Error al abrir el archivo.")


def cargar_vacaciones(archivo,vacaciones):

    try:
        with open(archivo, mode="r", newline="") as f_empleados, open(vacaciones, mode="r", newline="") as f_vacaciones:
            leyendo_empleados = csv.reader(f_empleados)
            leyendo_vacaciones = csv.reader(f_vacaciones)

            next(leyendo_empleados)
            next(leyendo_vacaciones)

            fila_empleados = next(leyendo_empleados,None)
            fila_vacaciones = next(leyendo_vacaciones,None)
            print("\nLos días que le quedan disponibles de vacaciones a cada empleado:")
            while fila_empleados:
                emp_legajo,emp_apellido,emp_nombre,emp_vacaciones = fila_empleados
                #print(emp_legajo)
                contador_dias = 0
                while (fila_vacaciones and fila_vacaciones[0] == emp_legajo):
                    #print(fila_vacaciones[0])
                    contador_dias +=1
                    fila_vacaciones = next(leyendo_vacaciones,None)

                dias_restantes = int(emp_vacaciones) - contador_dias
                print(f"\tLegajo {emp_legajo} : {emp_nombre} {emp_apellido}, le restan {dias_restantes} dias de vacaciones.")

                fila_empleados = next(leyendo_empleados,None)
        return
    except IOError:
        print("Error al abrir el archivo.")


acciones()





'''
def pedir_entero():
    while True:
        valor = input("Ingrese un número entero: ")
        try:
            return int(valor)
        except ValueError:
            print("'{}' no es un número entero.".format(valor))
'''
