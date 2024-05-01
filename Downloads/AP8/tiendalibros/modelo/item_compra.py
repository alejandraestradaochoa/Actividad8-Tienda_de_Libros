from libro import Libro

class ItemCompra:
    def __init__(self, libro:str, cantidad:Libro,int):

        self.libro = libro
        self.cantidad = cantidad

    def calcular_subtotal(self):
        return self.cantidad * self.libro.precio    




