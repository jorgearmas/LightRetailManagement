
from carga import exec_carga_existente, exec_carga_no_existente, exec_carga_stock
from descarga import exec_descarga
import os

def main_menu(opcion_menu):
    print("******** LIGHT RETAIL MANAGEMENT ********")
    print("-----------------------------------------")
    print("1. Cargar inventario proveedor existente")
    print("2. Cargar inventario - solo stock")
    print("3. Cargar inventario proveedor nuevo")
    print("4. Descargar inventario")
    print("5. Salir")
    print("-----------------------------------------")
    opcion_menu = int(input("Ingrese opcion: "))

    while opcion_menu != 5:
        if opcion_menu == 1:
            exec_carga_existente()
        elif opcion_menu == 2:
            exec_carga_stock()
        elif opcion_menu == 3:
            exec_carga_no_existente()
        elif opcion_menu == 4:
            os.system('cls')
            menu_descarga(0)
        elif opcion_menu == 5:
            exit()
        else:
            print("Ingrese opción correcta")
            opcion_menu = int(input("Ingrese opcion: "))

def menu_descarga(opcion_menu_descarga):
    print("******** LIGHT RETAIL MANAGEMENT ********")
    print("********* Control de descargas **********")
    print("1. Descargar por ID")
    print("2. Seleccionar de inventario")
    print("3. Regresar")
    print("-----------------------------------------")
    opcion_menu_descarga = int(input("Ingrese opcion: "))

    while opcion_menu_descarga != 4:
        if opcion_menu_descarga == 1:
            exec_descarga()
        elif opcion_menu_descarga == 2:
            pass
        elif opcion_menu_descarga == 3:
            os.system('cls')
            main_menu(0)
        else:
            print("Ingrese opción correcta")
            opcion_menu_descarga = int(input("Ingrese opcion: "))