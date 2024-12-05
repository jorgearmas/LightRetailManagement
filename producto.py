from proveedor import Proveedor

class Producto:

    identifier = 0
    
    def __init__(self, input_nombre, input_cantidad, input_precio_entrada, input_precio_salida, input_proveedor):

        Producto.identifier += 1
        self.id = Producto.identifier
        self.nombre = input_nombre
        self.cantidad = input_cantidad
        self.precio_entrada = input_precio_entrada
        self.precio_salida = input_precio_salida
        self.proveedor = input_proveedor
    
    def __repr__(self) :
        return f"""
        ID: {self.id}
        Nombre: {self.nombre}
        Cantidad: {self.cantidad}
        Precio entrada: {self.precio_entrada }
        Precio salida: {self.precio_salida}
        Proveedor:{self.proveedor}"""

    


