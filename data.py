import csv

def insert_producto(productos):

    campos = ['id', 'nombre', 'cantidad', 'precio_entrada', 'precio_salida', 'proveedor']

    with open('productos.csv', 'a', newline='') as productos_csv:

        producto_writer = csv.DictWriter(productos_csv, fieldnames=campos)
        producto_writer.writeheader()

        for fila in productos:
            producto_writer.writerow(fila)

def read_producto():
    productos = []
    with open('productos.csv', newline='') as productos_csv:
        producto_reader = csv.DictReader(productos_csv, delimiter=',')
        for lines in producto_reader:
            productos.append(lines)
    
    return productos


