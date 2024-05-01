class LibroError(Exception):
    pass

class LibroExistenteError(LibroError):
    def __init__(self, titulo, isbn):
        self.titulo = titulo
        self.isbn = isbn
        mensaje = f"El libro con título '{titulo}' y ISBN '{isbn}' ya existe en el catálogo."
        super().__init__(mensaje)

    def __str__(self):
        return f"El libro con título '{self.titulo}' y ISBN '{self.isbn}' ya existe en el catálogo."
