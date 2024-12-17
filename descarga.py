from data import insert_producto, read_producto
from carga import primera_carga
import os

try:
    productos = read_producto()
except FileNotFoundError:
    primera_carga()

def exec_descarga():
    continuar = 1
    while continuar == 1:
        id_to_search = input("- Ingrese ID a buscar: ")
        for registro in productos:
            for key, value in registro.items():
                if key == 'id' and value == id_to_search:
                    print(registro)
                    unidades_vendidas = input("- Ingrese unidades vendidas: ")
                    registro['cantidad'] = str(int(registro['cantidad']) - int(unidades_vendidas))
                    print(f"Nueva existencia de {registro['nombre']} ({registro['id']}) -> {registro['cantidad']} unidades")
        continuar = int(input("Desea continuar descargando (1 > Si / 2 > No)? "))

    insert_producto(productos)
    from menu import main_menu
    main_menu()

def exec_descarga_gral():
    print("Seleccione producto a descargar")
    
    for i in range(len(productos)):
        print(f"{i} - {productos[i]}")
    item_a_descargar = int(input('Opción: '))     
    
    for i in range(len(productos)):
        if i == item_a_descargar:
            print(f"Descargando -> {productos[item_a_descargar]}")
            for key, values in productos[item_a_descargar].items():
                unidades_vendidas = input("- Ingrese unidades vendidas: ")
                
    os.system('cls')
    from menu import main_menu
    main_menu(0)
