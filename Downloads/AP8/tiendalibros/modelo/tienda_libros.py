from libro import Libro
from libro_error import LibroExistenteError
from carro_compra import CarroCompras
from typing import Dict
from libro_error import LibroAgotadoError, ExistenciasInsuficientesError


class Libro:
    def __init__(self, isbn: str, titulo: str, precio: float, existencias: int):
        self.isbn: str = isbn
        self.titulo: str = titulo
        self.precio: float = precio
        self.existencias: int = existencias

    def __str__(self):
        return "({}) {} - ${:,.2f}".format(self.isbn, self.titulo, self.precio)

class TiendaLibros:
    def __init__(self, catalogo: Dict[str, "Libro"]):
        self.catalogo = catalogo
        self.carrito = CarroCompras()

    def adicionar_libro_a_catálogo(self, isbn: str, titulo: str, precio: float, existencias: int) -> Libro:
        if isbn in self.catalogo:
            raise LibroExistenteError(f"El libro con ISBN {isbn} ya existe en el catálogo.")

        nuevo_libro = Libro(isbn, titulo, precio, existencias)
        self.catalogo[isbn] = nuevo_libro
        return nuevo_libro
    
    def agregar_libro_a_carrito(self, libro: "Libro", cantidad: int):
        if libro.existencias == 0:
            raise LibroAgotadoError(f"El libro '{libro.titulo}' está agotado.", libro.isbn)
        if cantidad > libro.existencias:
            raise ExistenciasInsuficientesError(f"No hay suficientes existencias para '{libro.titulo}'.", libro.isbn, cantidad, libro.existencias)
        self.carrito.agregar_item(libro, cantidad)
    
    def retirar_item_de_carrito(self, isbn: str):
        self.carrito.quitar_item(isbn)


