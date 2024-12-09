from proveedor import Proveedor
from producto import Producto
from data import insert_producto, insert_proveedor
from carga import exec_carga_existente, exec_carga_no_existente, exec_carga_stock

from descarga import *

print("-- LIGHT RETAIL MANAGEMENT --")
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

opcion_menu = 0

print("1. Cargar inventario proveedor existente")
print("2. Cargar inventario - solo stock")
print("3. Cargar inventario proveedor nuevo")
print("4. Descargar inventario")
opcion_menu = int(input("Ingrese opcion: "))

if opcion_menu == 1:
    exec_carga_existente()
elif opcion_menu == 2:
    exec_carga_stock()
elif opcion_menu == 3:
    exec_carga_no_existente()
# elif opcion_menu == 4:
#     exec_descarga()
    