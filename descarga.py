from data import insert_producto, read_producto
from proveedor import Proveedor
from producto import Producto

productos = read_producto()

def exec_descarga():

    id_to_search = input("- Ingrese ID a buscar: ")
    for registro in productos:
        for key, value in registro.items():
            print(registro)