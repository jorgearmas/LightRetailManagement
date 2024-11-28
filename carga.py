from data import insert_producto, read_producto
from proveedor import Proveedor
from producto import Producto

def exec_carga_existente():
    productos = read_producto()
    proveedores = []

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
    proveedor = Proveedor(proveedor_value)
    
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
                prov = Proveedor(value)

            producto = Producto(nombre_producto, cantidad, precio_entrada, precio_salida, prov)
        
    #Agregar nuevos productos
    continuar = 1

    while continuar == 1:
        
        print("-- Ingrese datos del producto --")
        nombre_producto = input("Nombre: ")
        cantidad = input("Cantidad: ")
        precio_entrada = input("Precio de compra: ")
        precio_salida = input("Precio de venta: ")

        producto = Producto(nombre_producto, cantidad, precio_entrada, precio_salida, proveedor)
        productos.append({
            'id': producto.id, 
            'nombre': producto.nombre, 
            'cantidad': producto.cantidad, 
            'precio_entrada': producto.precio_entrada, 
            'precio_salida': producto.precio_salida, 
            'proveedor': producto.proveedor.nombre})

        print(productos)
        continuar = int(input("Desea agregar otro producto del mismo proveedor (1 > Si / 2 > No)? "))
    
    insert_producto(productos)