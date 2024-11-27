from proveedor import Proveedor
from producto import Producto
from data import insert_producto

productos = []

proveedor = Proveedor("DISTELSA", "42828238")

producto = Producto("Samsung", 6, 2500, 3100, proveedor)
productos.append({
    'id': producto.id, 
    'nombre': producto.nombre, 
    'cantidad': producto.cantidad, 
    'precio_entrada': producto.precio_entrada, 
    'precio_salida': producto.precio_salida, 
    'proveedor': producto.proveedor.nombre})


producto = Producto("LG", 6, 2250, 2700, proveedor)
productos.append({
    'id': producto.id, 
    'nombre': producto.nombre, 
    'cantidad': producto.cantidad, 
    'precio_entrada': producto.precio_entrada, 
    'precio_salida': producto.precio_salida, 
    'proveedor': producto.proveedor.nombre})

insert_producto(productos)
print(productos)


