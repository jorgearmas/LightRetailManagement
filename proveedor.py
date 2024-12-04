class Proveedor:

    identifier = 0

    def __init__(self, input_nombre, input_numero):

        Proveedor.identifier += 1
        self.id = Proveedor.identifier
        self.nombre = input_nombre
        self.numero = input_numero

    def __repr__(self):
        return f"ID: {self.id} | Nombre: {self.nombre} | Número: {self.numero}"