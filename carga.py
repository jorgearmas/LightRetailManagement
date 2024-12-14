from data import insert_producto, read_producto, insert_proveedor, read_proveedor
from proveedor import Proveedor
from producto import Producto
import os

try:
    productos = read_producto()
except FileNotFoundError:
    print("Proceso archivo inicial stock")

try:
    proveedores = read_proveedor()
except FileNotFoundError:
    print("Proceso archivo inicial stock")

def instanciar_productos(productos):
    
    #globales para hacer instancias de 'Producto' con data del dict 'productos'
    nombre_producto = ""
    cantidad = 0
    precio_entrada = 0
    precio_salida = 0
    prov = ""

    #Carga de clase 'Producto'
    for registro in productos:
        for key, value in registro.items():
            if key == 'nombre':
                nombre_producto = value
            elif key == 'cantidad':
                cantidad = value
            elif key == 'precio_entrada':
                precio_entrada = value
            elif key == 'precio_salida':
                precio_salida = value
            elif key == 'proveedor':
                prov = value

            Producto(nombre_producto, cantidad, precio_entrada, precio_salida, prov)

def instanciar_proveedores(proveedores):
    nombre = ""
    numero = ""
    
    for registro in proveedores:
        for key, value in registro.items():
            if key == 'nombre':
                nombre = value
            elif key == 'numero':
                numero = value
            
            Proveedor(nombre, numero)

def exec_carga_existente():

    continuar = 1
    proveedores = []

    #instanciar 'Producto' con productos existentes del diccionario 'productos'
    instanciar_productos(productos)

    #extraer proveedores del diccionario 'productos'
    for registro in productos:
        for key, value in registro.items():
            if key == 'proveedor':
                if value in proveedores:
                    continue
                else:
                    proveedores.append(value)

    #seleccionar proveedor
    print("Seleccione el proveedor: ")
    for i in range(len(proveedores)):
        print(str(i)+" - "+proveedores[i])

    proveedor_index = int(input("Opción: "))
    proveedor_value = proveedores[proveedor_index]
    
    # 1. instanciar 'Producto' con nuevos valores 2. agregar dict a lista de productos
    while continuar == 1:
        
        print("-- Ingrese datos del producto --")
        nombre_producto = input("Nombre: ")
        cantidad = input("Cantidad: ")
        precio_entrada = input("Precio de compra: ")
        precio_salida = input("Precio de venta: ")

        producto = Producto(nombre_producto, cantidad, precio_entrada, precio_salida, proveedor_value)
        productos.append({
            'id': producto.id, 
            'nombre': producto.nombre, 
            'cantidad': producto.cantidad, 
            'precio_entrada': producto.precio_entrada, 
            'precio_salida': producto.precio_salida, 
            'proveedor': producto.proveedor})

        continuar = int(input("Desea agregar otro producto del mismo proveedor (1 > Si / 2 > No)? "))
    
    #escribir lista en el archivo
    insert_producto(productos)
    os.system('cls')
    from menu import main_menu
    main_menu()

def exec_carga_stock():

    #instanciar 'Producto' con productos existentes del diccionario 'productos'
    instanciar_productos(productos)

    #input id a buscar
    id_to_search = input("- Ingrese ID a buscar: ")

    #1. iterar sobre lista de productos
    #2. iterar sobre registro encontrar id a modificar
    #3. modificar cantidad (stock)
    for registro in productos:
        for key, value in registro.items():
            if key == 'id' and value == id_to_search:
                print(f"Invetario actual de {registro['nombre']} -> {registro['cantidad']}")
                cantidad_ingresada = int(input("- Numero de items a agregar: "))
                nueva_cantidad = int(registro['cantidad']) + cantidad_ingresada
                print(f"Nuevo invetario de {registro['nombre']} -> "+str(nueva_cantidad))
                registro['cantidad'] = str(nueva_cantidad)
    
    insert_producto(productos)
    input('Pulse enter para volver al menú')
    os.system('cls')
    from menu import main_menu
    main_menu()
            
def exec_carga_no_existente():
    #instanciar 'Producto' con productos existentes del diccionario 'productos'
    instanciar_productos(productos)
    #instanciar 'Proveedores' con proveedores existentes del diccionario 'proveedores'
    instanciar_proveedores(proveedores)

    #proveedores = []
    continuar = 1
    
    print("-- Ingrese proveedor del producto --")
    nombre_proveedor = input("Nombre: ")
    numero_proveedor = input("Teléfono: ")
    proveedor = Proveedor(nombre_proveedor, numero_proveedor)

    proveedores.append({
        'id': proveedor.id,
        'nombre': proveedor.nombre,
        'numero': proveedor.numero})
    
    insert_proveedor(proveedores)
            
    while continuar == 1:
        
        print("-- Ingrese datos del producto --")
        nombre_producto = input("Nombre: ")
        cantidad = input("Cantidad: ")
        precio_entrada = input("Precio de compra: ")
        precio_salida = input("Precio de venta: ")

        producto = Producto(nombre_producto, cantidad, precio_entrada, precio_salida, proveedor.nombre)
        productos.append({
            'id': producto.id, 
            'nombre': producto.nombre, 
            'cantidad': producto.cantidad, 
            'precio_entrada': producto.precio_entrada, 
            'precio_salida': producto.precio_salida, 
            'proveedor': proveedor.nombre})

        continuar = int(input("Desea agregar otro producto del mismo proveedor (1 > Si / 2 > No)? "))
    
    insert_producto(productos)
    input('Pulse enter para volver al menú')
    os.system('cls')
    from menu import main_menu
    main_menu()