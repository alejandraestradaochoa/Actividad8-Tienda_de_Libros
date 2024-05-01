class LibroError(Exception):
    pass

class LibroAgotadoError(LibroError):
    def __init__(self, titulo, isbn):
        self.titulo = titulo
        self.isbn = isbn
        mensaje = f"El libro con título '{titulo}' y ISBN '{isbn}' está agotado."
        super().__init__(mensaje)

    def __str__(self):
        return f"El libro con título '{self.titulo}' y ISBN '{self.isbn}' está agotado."