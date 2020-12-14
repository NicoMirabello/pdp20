import csv
import logging
import os

logging.basicConfig(filename='registro.log',format='%(message)s',level=logging.DEBUG)

def pedirNumeroEntero():
    correcto = False
    numero = 0
    while(not correcto):
        try:
            numero = int(input("\n > "))
            correcto = True
        except ValueError:
            print('\n\t > ERROR. Ingrese una opción válida.\n')
    return numero

def acciones():
    logging.info('Acción')
    CLIENTES = "clientes.csv"
    VIAJES = "viajes.csv"
    cargar_cliente = cargar_csv_cliente(CLIENTES)
    cargar_viaje = cargar_csv_viajes(VIAJES)

    salir = False
    opcion = 0

    while not salir:
        print ("\nElija una opción: \n\n1. Buscar cliente por nombre. \n2. Total de usuarios por empresa.\n3. Total de dinero en viajes por empresa.\n4. Cantidad de viajes y monto total.\n5. Salir")
        #opcion = input ("\n > Ingrese la opción: ")
        opcion = pedirNumeroEntero()
        logging.info('MENÚ')

        if opcion == 5:
            logging.info('Salir')
            salir = True
            exit()
        elif opcion == 1:
            buscar_cliente(cargar_cliente)
            logging.info('Búsqueda de cliente por nombre')
        elif opcion == 2:
            cargar_lista_de_clientes = total_usuario(cargar_cliente)
            imprimir_busqueda = ver_cantidad_usuarios(cargar_lista_de_clientes)
            logging.info('Búsqueda total usuarios por empresa')
        elif opcion == 3:
            cargar_lista_de_clientes_dos = total_usuario(cargar_cliente)
            imprimir_monto, lista_encontrados = total_monto(cargar_lista_de_clientes_dos,cargar_viaje)
            ver_total_monto(cargar_lista_de_clientes_dos,imprimir_monto)
            logging.info('Total de dinero en viajes por nombre de empresa')
        elif opcion == 4:
            cargar_lista_de_clientes_por_dni = total_por_dni(cargar_cliente)
            imprimir_monto_dos, lista = total_monto(cargar_lista_de_clientes_por_dni,cargar_viaje)
            ver_total_monto_y_viajes(cargar_lista_de_clientes_por_dni, imprimir_monto_dos,lista)
            logging.info('Cantidad total de viajes realizados y monto total por documento')
        else:
            print("\n > ERROR. Ingrese una opción válida.\n")


#Cargar el csv de clientes
def cargar_csv_cliente(archivo):
    lista_de_clientes = []
    try:
        with open (archivo, mode="r", newline="", encoding='utf-8') as f_archivo:
            leyendo_archivo = csv.reader(f_archivo)
            next (leyendo_archivo)
            for datos in leyendo_archivo:
                nombre,direccion,documento,fecha,correo,empresa = datos
                validar_campo_cliente(datos)
                validar_documento(documento)
                validar_correo(correo)
                lista_de_clientes.append(datos)
        return lista_de_clientes
    except IOError:
        print("\n Error al cargar el archivo CSV.")
        exit()

#Cargar el csv de viajes
def cargar_csv_viajes(archivo):
    lista_de_viajes = []
    try:
        with open (archivo, mode="r", newline="", encoding='utf-8') as f_archivo:
            leyendo_archivo = csv.reader(f_archivo)
            next (leyendo_archivo)
            for datos in leyendo_archivo:
                dni,fecha,monto = datos
                validar_campo_viaje(datos)
                validar_documento(dni)
                validar_monto(monto)
                lista_de_viajes.append(datos)
        return lista_de_viajes
    except IOError:
        print("\n Error al cargar el archivo CSV.")
        exit()

def mensaje_de_salida():
    input("\n > Presiene cualquier tecla para salir.")
    exit()

#Validar CSV por documento
def validar_documento(dato):
    if (len(str(dato)) >= 7 and len(str(dato)) <=8):
        return
    else:
        print("\nERROR. Documeto no válido.")
        mensaje_de_salida()

#Validar CSV por campo
def validar_campo_viaje(dato):
    if dato[0] and dato[1] and dato[2] != "":
        return
    else:
        print("\nERROR. Campo no válido.")
        mensaje_de_salida()

#Validar CSV por campo
def validar_campo_cliente(dato):
    if dato[0] and dato[1] and dato[2] and dato[3] and dato[4] and dato[5] != "":
        return
    else:
        print("\nERROR. Campo no válido.")
        mensaje_de_salida()

#Validar CSV por correo
def validar_correo(dato):
    arroba = "@"
    punto = "."
    if (punto in dato and arroba in dato):
        return
    else:
        print("\nERROR. Correo electrónico no válido.")
        mensaje_de_salida()

#Validar CSV por monto
def validar_monto(dato):
    if "." in str(dato):
        decimales = str(dato).split(".")[-1]
        cantidad_decimales = len(decimales)
        if (cantidad_decimales == 2):
            return
        else:
            print("\nERROR. Monto cargado no válido.")
            mensaje_de_salida()

#Validar con flag
def validador_flag(flag):
    if flag != False:
        flag = False
    else:
        print("\n\t > No se encontraron resultados\n\n")

#Ingresar nombre de cliente
def busqueda_nombre():
    print("\n--------------------\n")
    nombre_cliente = input("Buscar cliente: ")
    return nombre_cliente

#Ingresar nombre de empresa
def busqueda_empresa():
    print("\n--------------------\n")
    nombre_empresa = input("Empresa: ")
    return nombre_empresa

#Ingresar numero de dni
def busqueda_dni():
    print("\n--------------------\n")
    num_dni = input("Documento: ")
    return num_dni

#Busqueda total o parcial por nombre de cliente
def buscar_cliente(lista_clientes):
    flag = False
    cliente = busqueda_nombre()
    for i in lista_clientes:
        if cliente in i[0]:
            print(i)
            flag = True
    flag = validador_flag(flag)

#Obtener el listado total de usuarios buscando por el nombre de la empresa
def total_usuario(lista_clientes):
    lista_encontrados = []
    busqueda = busqueda_empresa()
    for i in lista_clientes:
        if busqueda == i[5]:
            lista_encontrados.append(i)
    return lista_encontrados

#Imprimir la cantidad total de usuarios por empresa y todos sus datos
def ver_cantidad_usuarios(datos):
    cantidad = len(datos)
    if cantidad > 0:
        print(f"Total usuarios: {cantidad}\n--------------------\n")
        for item in datos:
            print(item)
    else:
        print("\n\t > No se encontraron resultados\n\n")

#Obtener el total de dinero en viajes por empresa
def total_monto(cliente,viaje):
    lista_encontrados_dni =[]
    total_monto = 0
    for i in viaje:
        doc,fec,monto = i
        for ii in cliente:
            if ii[2] == doc:
                lista_encontrados_dni.append(i)
                total_monto += float(monto)
    return total_monto, lista_encontrados_dni

#Imprimir el monto total acumulado por empresa
def ver_total_monto(datos,monto):
    cantidad = len(datos)
    if cantidad > 0:
        print(f"Monto total: {monto:.2f}")
        print("\n--------------------\n")
    else:
        print("\n\t > No se encontraron resultados\n\n")

#Obtener el listado total de usuarios buscando por el numero de documento
def total_por_dni(lista_clientes):
    lista_encontrados = []
    busqueda = busqueda_dni()
    for i in lista_clientes:
        if busqueda == i[2]:
            lista_encontrados.append(i)
    return lista_encontrados

#Imprimir los datos del usuario por documento, el monto total acumulado y los datos de sus viajes
def ver_total_monto_y_viajes(datos,monto,encontrados):
    cantidad = len(encontrados)
    if cantidad > 0:
        print("\n--------------------\n")
        for cliente in datos:
            print(cliente)
        print(f"\n--------------------\nTotal viajes: {cantidad}. Monto total: {monto:.2f}\n--------------------\n")
        for i in encontrados:
            print(i)
        print("\n--------------------\n")
    else:
        print("\n\t > No se encontraron resultados\n\n")


acciones()
