# Define la clase Pelicula para representar las películas con título y director.
class Pelicula:
    def __init__(self, titulo, director):
        self.titulo = titulo
        self.director = director

# Define la clase Tematica para manejar las temáticas de la biblioteca, que contienen películas.
class Tematica:
    def __init__(self, nombre):
        self.nombre = nombre
        self.peliculas = []  # Inicializa una lista vacía de películas.

    def agregar_pelicula(self, pelicula):
        self.peliculas.append(pelicula)  # Agrega una película a la lista de películas.

# Define la clase Biblioteca para gestionar temáticas y listas de visualización.
class Biblioteca:
    def __init__(self):
        self.tematicas = {}  # Inicializa un diccionario vacío para las temáticas.
        self.lista_visualizacion = []  # Inicializa una lista vacía para la lista de visualización.

    def agregar_tematica(self, tematica):
        self.tematicas[tematica.nombre] = tematica  # Agrega una temática al diccionario.

    def agregar_pelicula_a_tematica(self, nombre_tematica, pelicula):
        # Añade una película a una temática específica.
        if nombre_tematica in self.tematicas:
            self.tematicas[nombre_tematica].agregar_pelicula(pelicula)
        else:
            print(f"Temática '{nombre_tematica}' no encontrada.")  # Mensaje de error si la temática no existe.

    def mostrar_tematicas(self):
        # Muestra todas las temáticas disponibles.
        for i, tematica in enumerate(self.tematicas.values()):
            print(f"{i + 1}. {tematica.nombre}")

    def mostrar_peliculas(self, nombre_tematica):
        # Muestra todas las películas de una temática específica.
        tematica = self.tematicas.get(nombre_tematica)
        if tematica:
            for i, pelicula in enumerate(tematica.peliculas):
                print(f"{i + 1}. '{pelicula.titulo}' dirigida por {pelicula.director}")
        else:
            print(f"Temática '{nombre_tematica}' no encontrada.")  # Mensaje de error si la temática no existe.

    def agregar_pelicula_a_lista_visualizacion(self, pelicula):
        self.lista_visualizacion.append(pelicula)  # Añade una película a la lista de visualización.

    def mostrar_lista_visualizacion(self):
        # Muestra todas las películas en la lista de visualización.
        if not self.lista_visualizacion:
            print("No hay películas en la lista de visualización.")
        else:
            for pelicula in self.lista_visualizacion:
                print(f"'{pelicula.titulo}' dirigida por {pelicula.director}")

# Función principal que maneja la lógica del programa.
def main():
    biblioteca = Biblioteca()

    # Define las temáticas de la biblioteca.
    tematicas = ["Acción", "Comedia", "Ciencia Ficción", "Drama", "Documental"]
    for nombre_tematica in tematicas:
        biblioteca.agregar_tematica(Tematica(nombre_tematica))

    # Define las películas disponibles.
    peliculas = [
        Pelicula("Mad Max: Fury Road", "George Miller"),
        Pelicula("Superbad", "Greg Mottola"),
        Pelicula("Blade Runner 2049", "Denis Villeneuve"),
        Pelicula("La La Land", "Damien Chazelle"),
        Pelicula("13th", "Ava DuVernay")
    ]

    # Asocia películas con sus respectivas temáticas.
    peliculas_por_tematica = {
        "Acción": ["Mad Max: Fury Road"],
        "Comedia": ["Superbad"],
        "Ciencia Ficción": ["Blade Runner 2049"],
        "Drama": ["La La Land"],
        "Documental": ["13th"]
    }

    # Añade las películas a las temáticas correspondientes.
    for pelicula in peliculas:
        for nombre_tematica, titulos_peliculas in peliculas_por_tematica.items():
            if pelicula.titulo in titulos_peliculas:
                biblioteca.agregar_pelicula_a_tematica(nombre_tematica, pelicula)

    # Menú interactivo para el usuario.
    while True:
        print("\n1. Agregar película a la lista de visualización")
        print("2. Ver lista de visualización")
        print("3. Salir")
        print("-------------------------------------------------")
        opcion = input("Selecciona una opción: ")
        print("-------------------------------------------------")
        if opcion == '1':
            print("Temáticas disponibles:")
            biblioteca.mostrar_tematicas()
            indice_tematica = int(input("Ingrese el número de la temática: ")) - 1
            nombre_tematica = tematicas[indice_tematica]
            print(f"Películas disponibles en la temática {nombre_tematica}:")
            biblioteca.mostrar_peliculas(nombre_tematica)
            indice_pelicula = int(input("Ingrese el número de la película: ")) - 1
            pelicula = biblioteca.tematicas[nombre_tematica].peliculas[indice_pelicula]
            biblioteca.agregar_pelicula_a_lista_visualizacion(pelicula)
            print(f"Película '{pelicula.titulo}' agregada a la lista de visualización.")

        elif opcion == '2':
            biblioteca.mostrar_lista_visualizacion()

        elif opcion == '3':
            break

        else:
            print("Opción no válida. Inténtalo de nuevo.")  # Mensaje para opciones no válidas.

# Ejecuta la función principal si el script es ejecutado directamente.
if __name__ == "__main__":
    main()
