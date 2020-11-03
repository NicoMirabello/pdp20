import csv
import os

def acciones():

    ruta = input(f"Ingrese el nombre del archivo: ")
    if os.path.isfile(ruta):
        print('El archivo existe. ¿Desea sobreescribirlo?: ',end="")
        flag = input("si / no: ")
        if flag == "no":
            ruta = input(f"Ingrese un nuevo nombre de archivo: ")
    else:
        print('Se creo correctamente.\n');

    ARCHIVO = ruta
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

    lista_de_empleados = []
    guardar = "si"

    while guardar =="si":
        empleado = {}

        for campo in campos:
            if campo == "Legajo":
                print(f"Ingrese {campo} del empleado: ",end ="")
                empleado[campo] = pedir_entero()
            elif campo =="Vacaciones":
                print(f"Ingrese {campo} del empleado: ",end ="")
                empleado[campo] = pedir_entero()
            else:
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


def pedir_entero():
    while True:
        valor = input("")
        try:
            return int(valor)
        except ValueError:
            print("'{}' no es un número entero. Por favor ingrese un numero valido: ".format(valor))


acciones()
