from proveedor import Proveedor
from producto import Producto
from data import insert_producto, insert_proveedor
from menu import main_menu

primera_ejecucion = int(input("Es esta la primera ejecucion (1 > Si / 2 > No)? "))

while primera_ejecucion == 1:
    proveedores = []
    productos = []
    continuar = 1
    
    print("-- Ingrese datos del proveedor del producto --")
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
    primera_ejecucion = 2

main_menu()


        