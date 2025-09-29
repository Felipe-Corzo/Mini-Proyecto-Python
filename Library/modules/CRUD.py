usuarios = {}
libros = {}  
generos = set()  
def registrar_usuario():
    try:
        id = input("Ingrese cédula del usuario: ")
        if id in usuarios:
            print("Usuario ya registrado.")
            return
        nombre = input("Ingrese nombre del usuario: ")
        generos_fav = input("Ingrese géneros favoritos separados por coma: ")
        generos_favoritos = set(g for g in generos_fav.split(",") if g.strip())
        usuarios[id] = {"nombre": nombre,"generos_favoritos": generos_favoritos,"historial": []}
        generos.update(generos_favoritos)
        print(f"Usuario {nombre} registrado con géneros favoritos: {generos_favoritos}")
    except ValueError:
        print("Error al registrar usuario ")
def agregar_libro():
    try:
        codigo = int(input("Ingrese código del libro: "))
        if codigo in libros:
            print("Código de libro ya existe.")
            return
        titulo = input("Ingrese título del libro: ")
        autor = input("Ingrese autor del libro: ")
        genero = input("Ingrese género del libro: ")
        libros[codigo] = {"titulo": titulo, "autor": autor, "genero": genero, "disponible": True}
        generos.add(genero)
        print(f"Libro '{titulo}' agregado al catálogo.")
    except ValueError:
        print("El código debe ser un número entero.")
def prestar_libro():
    try:
        id = input("Ingrese id del usuario: ")
        if id not in usuarios:
            print("Usuario no registrado.")
            return
        codigo = int(input("Ingrese código del libro a prestar: "))
        if codigo not in libros:
            print("Libro no existe.")
            return
        if not libros[codigo]["disponible"]:
            print("Libro no disponible.")
            return
        libros[codigo]["disponible"] = False
        usuarios[id]["historial"].append(codigo)
        print(f"Libro '{libros[codigo]['titulo']}' prestado a {usuarios[id]['nombre']}.")
    except ValueError:
        print("El código debe ser un número entero.")
def devolver_libro():
    try:
        id = input("Ingrese id del usuario: ")
        if id not in usuarios:
            print("Usuario no registrado.")
            return
        codigo = int(input("Ingrese código del libro a devolver: "))
        if codigo not in libros:
            print("Libro no existe.")
            return
        if libros[codigo]["disponible"]:
            print("El libro ya está disponible en la biblioteca.")
            return
        libros[codigo]["disponible"] = True
        print(f"Libro '{libros[codigo]['titulo']}' devuelto por {usuarios[id]['nombre']}.")
    except ValueError:
        print("El código debe ser un número entero.")
def recomendar_libros():
    try:
        id = input("Ingrese id del usuario para recomendar libros: ")
        if id not in usuarios:
            print("Usuario no registrado.")
            return
        favoritos = usuarios[id]["generos_favoritos"]
        recomendados = []
        for codigo, info in libros.items():
            if info["genero"] in favoritos and info["disponible"]:
                recomendados.append(info["titulo"])
        if recomendados:
            print(f"Libros recomendados para {usuarios[id]['nombre']}: {recomendados}")
        else:
            print("No hay libros disponibles para recomendar en sus géneros favoritos.")
    except ValueError:
        print("id inválido ")
def analisis_usuarios():
    try:
        if not usuarios:
            print("No hay usuarios registrados.")
            return
        lista_generos = [u["generos_favoritos"] for u in usuarios.values()]
        interseccion = lista_generos[0]
        for g in lista_generos[1:]:
            interseccion = interseccion & g
        print(f"Géneros favoritos en común entre todos los usuarios: {interseccion}")

        if len(lista_generos) >= 2:
            diff_sim = lista_generos[0] ^ lista_generos[1]
            print(f"Géneros únicos entre los dos primeros usuarios: {diff_sim}")

        total_prestamos = sum(len(u["historial"]) for u in usuarios.values())
        print(f"Total usuarios: {len(usuarios)}")
        print(f"Total libros: {len(libros)}")
        print(f"Total préstamos realizados: {total_prestamos}")
    except ValueError:
        print("Error. ")