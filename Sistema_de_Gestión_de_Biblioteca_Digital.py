class Libro:
    """Representa un libro con tupla para autor-título (inmutable)."""

    def __init__(self, titulo, autor, categoria, isbn):
        self.autor_titulo = (autor, titulo)  # Tupla inmutable
        self.categoria = categoria
        self.isbn = isbn
        self.prestado = False

    @property
    def autor(self):
        return self.autor_titulo[0]

    @property
    def titulo(self):
        return self.autor_titulo[1]

    def __str__(self):
        estado = "Prestado" if self.prestado else "Disponible"
        return f"'{self.titulo}' por {self.autor} ({self.categoria}) - {estado}"


class Usuario:
    """Representa un usuario con lista de libros prestados."""

    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []  # Lista de libros prestados

    def prestar_libro(self, libro):
        if libro not in self.libros_prestados:
            self.libros_prestados.append(libro)

    def devolver_libro(self, libro):
        if libro in self.libros_prestados:
            self.libros_prestados.remove(libro)


class Biblioteca:
    """Gestiona libros, usuarios y préstamos con diferentes estructuras de datos."""

    def __init__(self, nombre="Biblioteca Digital"):
        self.nombre = nombre
        self.libros = {}  # Diccionario: ISBN -> Libro
        self.ids_usuarios = set()  # Conjunto para IDs únicos
        self.usuarios = {}  # Diccionario: ID -> Usuario

    # === GESTIÓN DE LIBROS ===
    def anadir_libro(self, titulo, autor, categoria, isbn):
        """Añade libro usando diccionario para búsqueda eficiente."""
        if isbn in self.libros:
            return False
        self.libros[isbn] = Libro(titulo, autor, categoria, isbn)
        return True

    def quitar_libro(self, isbn):
        """Quita libro si no está prestado."""
        if isbn not in self.libros or self.libros[isbn].prestado:
            return False
        del self.libros[isbn]
        return True

    # === GESTIÓN DE USUARIOS ===
    def registrar_usuario(self, nombre, id_usuario):
        """Registra usuario usando conjunto para IDs únicos."""
        if id_usuario in self.ids_usuarios:
            return False
        self.ids_usuarios.add(id_usuario)
        self.usuarios[id_usuario] = Usuario(nombre, id_usuario)
        return True

    def dar_baja_usuario(self, id_usuario):
        """Da de baja usuario si no tiene libros prestados."""
        if id_usuario not in self.ids_usuarios:
            return False
        if len(self.usuarios[id_usuario].libros_prestados) > 0:
            return False
        self.ids_usuarios.remove(id_usuario)
        del self.usuarios[id_usuario]
        return True

    # === PRÉSTAMOS ===
    def prestar_libro(self, isbn, id_usuario):
        """Presta libro a usuario."""
        if (isbn not in self.libros or id_usuario not in self.ids_usuarios or
                self.libros[isbn].prestado):
            return False

        libro = self.libros[isbn]
        usuario = self.usuarios[id_usuario]
        libro.prestado = True
        usuario.prestar_libro(libro)
        return True

    def devolver_libro(self, isbn, id_usuario):
        """Devuelve libro de usuario."""
        if isbn not in self.libros or id_usuario not in self.ids_usuarios:
            return False

        libro = self.libros[isbn]
        usuario = self.usuarios[id_usuario]
        if libro not in usuario.libros_prestados:
            return False

        libro.prestado = False
        usuario.devolver_libro(libro)
        return True

    # === BÚSQUEDAS ===
    def buscar_por_titulo(self, titulo):
        """Busca libros por título."""
        return [libro for libro in self.libros.values()
                if titulo.lower() in libro.titulo.lower()]

    def buscar_por_autor(self, autor):
        """Busca libros por autor."""
        return [libro for libro in self.libros.values()
                if autor.lower() in libro.autor.lower()]

    def buscar_por_categoria(self, categoria):
        """Busca libros por categoría."""
        return [libro for libro in self.libros.values()
                if categoria.lower() in libro.categoria.lower()]

    # === LISTADOS ===
    def listar_libros_prestados_usuario(self, id_usuario):
        """Lista libros prestados a un usuario."""
        if id_usuario not in self.ids_usuarios:
            return []
        return self.usuarios[id_usuario].libros_prestados.copy()

    def listar_libros_disponibles(self):
        """Lista libros disponibles."""
        return [libro for libro in self.libros.values() if not libro.prestado]

    def estadisticas(self):
        """Muestra estadísticas de la biblioteca."""
        total = len(self.libros)
        prestados = sum(1 for libro in self.libros.values() if libro.prestado)
        print(f"Total libros: {total}, Disponibles: {total - prestados}, "
              f"Prestados: {prestados}, Usuarios: {len(self.usuarios)}")


#  EJEMPLO DE USO
def demo():
    """Demostración del sistema."""
    biblioteca = Biblioteca()

    # Añadir libros
    biblioteca.anadir_libro("1984", "George Orwell", "Ficción", "001")
    biblioteca.anadir_libro("El Quijote", "Cervantes", "Clásico", "002")

    # Registrar usuarios
    biblioteca.registrar_usuario("Ana", "U1")
    biblioteca.registrar_usuario("Carlos", "U2")

    # Préstamos
    biblioteca.prestar_libro("001", "U1")

    # Búsquedas
    print("Libros de Orwell:")
    for libro in biblioteca.buscar_por_autor("Orwell"):
        print(f"  {libro}")

    # Estadísticas
    biblioteca.estadisticas()


if __name__ == "__main__":
    demo()