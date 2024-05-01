import sys
from modelo import carro_compra
from modelo.tienda_libros import TiendaLibros
from modelo.libro_agotado_error import LibroAgotadoError
from modelo.libro_error import ExistenciasInsuficientesError
class UIConsola:

    def __init__(self):
        self.tienda_libros: TiendaLibros = TiendaLibros()
        self.opciones = {
            "1": self.adicionar_un_libro_a_catalogo,
            "2": self.agregar_libro_a_carrito_de_compras,
            "3": self.retirar_libro_de_carrito_de_compras,
            "4": self.salir
        }

    @staticmethod
    def salir():
        print("\nGRACIAS POR VISITAR NUESTRA TIENDA DE LIBROS. VUELVA PRONTO")
        sys.exit(0)

    @staticmethod
    def mostrar_menu():
        titulo = "¡Tienda Libros!"
        print(f"\n{titulo:_^30}")
        print("1. Adicionar un libro al catálogo")
        print("2. Agregar libro a carrito de compras")
        print("3. Retirar libro de carrito de compras")
        print(f"{'_':_^30}")

    def ejecutar_app(self):
        while True:
            self.mostrar_menu()
            opcion = input("Seleccione una opción: ")
            accion = self.opciones.get(opcion)
            if accion:
                accion()
            else:
                print(f"{opcion} no es una opción válida")

    def __init__(self, tienda_libros):
        self.tienda_libros = tienda_libros

    def agregar_libro_a_carrito_de_compras(self):
        try:
            isbn = input("Ingrese el ISBN del libro que desea agregar al carrito: ")
            cantidad = int(input("Ingrese la cantidad de unidades que desea agregar al carrito: "))
            libro = self.tienda_libros.catalogo.get(isbn)
            if libro is None:
                raise KeyError("El libro con ese ISBN no se encuentra en el catálogo.")
            self.tienda_libros.agregar_libro_a_carrito(libro, cantidad)
            print("El libro se agregó al carrito con éxito.")
        except ValueError:
            print("Error: La cantidad debe ser un número entero.")
        except KeyError as e:
            print(f"Error: {e}")
        except LibroAgotadoError as e:
            print(f"Error: {e}")
        except ExistenciasInsuficientesError as e:
            print(f"Error: {e}")
        
    def adicionar_un_libro_a_catalogo(self):
        try:
            isbn = input("Ingrese el ISBN del libro: ")
            titulo = input("Ingrese el título del libro: ")
            precio = float(input("Ingrese el precio del libro: "))
            existencias = int(input("Ingrese las existencias del libro: "))
            self.tienda_libros.adicionar_libro_a_catalogo(isbn, titulo, precio, existencias)
            print("El libro se agregó al catálogo con éxito.")
        except ValueError:
            print("Error: El precio y las existencias deben ser números.")
     
 