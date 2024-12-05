import csv
import os

general_path = 'data/'
productos_name = 'productos.csv'
productos_file_path = os.path.join(general_path, productos_name)
proveedores_name = 'proveedores.csv'
proveedores_file_path = os.path.join(general_path, proveedores_name)

os.makedirs(general_path, exist_ok=True)

def insert_producto(productos):

    campos = ['id', 'nombre', 'cantidad', 'precio_entrada', 'precio_salida', 'proveedor']

    with open(productos_file_path, 'w', newline='') as productos_csv:

        producto_writer = csv.DictWriter(productos_csv, fieldnames=campos)
        producto_writer.writeheader()

        for fila in productos:
            producto_writer.writerow(fila)

def read_producto():
    productos = []
    with open(productos_file_path, newline='') as productos_csv:
        producto_reader = csv.DictReader(productos_csv, delimiter=',')
        for lines in producto_reader:
            productos.append(lines)
    
    return productos

def insert_proveedor(proveedores):
    campos = ['id', 'nombre', 'numero']

    with open(proveedores_file_path, 'w', newline='') as proveedores_csv:

        proveedor_writer = csv.DictWriter(proveedores_csv, fieldnames=campos)
        proveedor_writer.writeheader()

        for fila in proveedores:
            proveedor_writer.writerow(fila)

def read_proveedor():
    proveedores = []
    with open(proveedores_file_path, newline='') as proveedores_csv:
        proveedores_reader = csv.DictReader(proveedores_csv, delimiter=',')
        for lines in proveedores_reader:
            proveedores.append(lines)
    
    return proveedores