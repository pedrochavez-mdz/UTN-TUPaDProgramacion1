import os
import sqlite3

DB_NAME = "biblioteca.db"


class Autor:
    def __init__(self, id_autor, nombre, nacionalidad):
        self.id_autor = id_autor
        self.nombre = nombre
        self.nacionalidad = nacionalidad

    def __str__(self):
        return f"Autor [{self.id_autor}]: {self.nombre} ({self.nacionalidad})"


class Libro:
    def __init__(self, id_libro, titulo, anio_publicacion, autor):
        self.id_libro = id_libro
        self.titulo = titulo
        self.anio_publicacion = anio_publicacion
        self.autor = autor

    def __str__(self):
        return (
            f"Libro [{self.id_libro}]: '{self.titulo}' "
            f"({self.anio_publicacion}) - {self.autor.nombre}"
        )


def conectar():
    conexion = sqlite3.connect(DB_NAME)
    conexion.execute("PRAGMA foreign_keys = ON")
    return conexion


def inicializar_db():
    with conectar() as conexion:
        conexion.execute(
            """
            CREATE TABLE IF NOT EXISTS autores (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                nacionalidad TEXT
            )
            """
        )
        conexion.execute(
            """
            CREATE TABLE IF NOT EXISTS libros (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                anio INTEGER,
                autor_id INTEGER NOT NULL,
                FOREIGN KEY (autor_id) REFERENCES autores(id)
            )
            """
        )


def registrar_autor(nombre, nacionalidad):
    conexion = conectar()
    try:
        with conexion:
            cursor = conexion.execute(
                "INSERT INTO autores (nombre, nacionalidad) VALUES (?, ?)",
                (nombre, nacionalidad),
            )
            return cursor.lastrowid
    finally:
        conexion.close()


def registrar_libro(titulo, anio, autor_id):
    conexion = conectar()
    try:
        with conexion:
            cursor = conexion.execute(
                "INSERT INTO libros (titulo, anio, autor_id) VALUES (?, ?, ?)",
                (titulo, anio, autor_id),
            )
            return cursor.lastrowid
    finally:
        conexion.close()


def listar_libros():
    conexion = conectar()
    try:
        cursor = conexion.execute(
            """
            SELECT libros.id, libros.titulo, libros.anio, autores.nombre
            FROM libros
            JOIN autores ON libros.autor_id = autores.id
            ORDER BY libros.id
            """
        )
        return cursor.fetchall()
    finally:
        conexion.close()


def actualizar_titulo_libro(id_libro, nuevo_titulo):
    conexion = conectar()
    try:
        with conexion:
            cursor = conexion.execute(
                "UPDATE libros SET titulo = ? WHERE id = ?",
                (nuevo_titulo, id_libro),
            )
            return cursor.rowcount > 0
    finally:
        conexion.close()


def eliminar_libro(id_libro):
    conexion = conectar()
    try:
        with conexion:
            cursor = conexion.execute(
                "DELETE FROM libros WHERE id = ?",
                (id_libro,),
            )
            return cursor.rowcount > 0
    finally:
        conexion.close()


def mostrar_libros():
    libros = listar_libros()
    if not libros:
        print("No hay libros registrados.")
        return
    for id_libro, titulo, anio, nombre_autor in libros:
        print(f"{id_libro:>3} | {titulo:<35} | {anio} | {nombre_autor}")


if __name__ == "__main__":
    if os.path.exists(DB_NAME):
        os.remove(DB_NAME)

    print("1. Inicializando la base de datos...")
    inicializar_db()
    print(f"Base de datos '{DB_NAME}' creada correctamente.\n")

    print("2. Registrando autores y libros...")
    id_garcia_marquez = registrar_autor("Gabriel García Márquez", "Colombiana")
    id_borges = registrar_autor("Jorge Luis Borges", "Argentina")

    autor_gm = Autor(id_garcia_marquez, "Gabriel García Márquez", "Colombiana")
    autor_jlb = Autor(id_borges, "Jorge Luis Borges", "Argentina")
    print(autor_gm)
    print(autor_jlb)

    id_l1 = registrar_libro("Cien años de soledad", 1967, id_garcia_marquez)
    id_l2 = registrar_libro("El amor en los tiempos del cólera", 1985, id_garcia_marquez)
    id_l3 = registrar_libro("Ficciones", 1944, id_borges)

    libro_objeto = Libro(id_l3, "Ficciones", 1944, autor_jlb)
    print(libro_objeto)
    print()

    print("3. Listado de libros registrados:")
    mostrar_libros()
    print()

    print("4. Actualizando el título del libro con id", id_l2)
    if actualizar_titulo_libro(id_l2, "El amor en los tiempos del cólera (Edición revisada)"):
        print("Título actualizado. Listado actual:")
    mostrar_libros()
    print()

    print("5. Eliminando el libro con id", id_l1)
    if eliminar_libro(id_l1):
        print("Libro eliminado. Listado resultante:")
    mostrar_libros()
