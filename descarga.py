from data import insert_producto, read_producto
from proveedor import Proveedor
from producto import Producto

try:
    productos = read_producto()
except FileNotFoundError:
    print("Proceso archivo inicial stock")

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