import modules.utils as u
allBooks=[]

def newBook ():
    name=input("Nombre del libro: ")
    autor=input("Autor: ")
    genero=input("Genero: ") 
    year=input("Año de publicación: ")
    state=input("¿Leido? (s/n) : ") 
    state= "Leido ✔️" if state.lower()== 's' else "Por leer⏳"
    book= {"Nombre":name , "Autor":autor , "Genero":genero , "Anio": year , "Estado":state}
    allBooks.append(book)
    print("\n ★ Haz agregado un nuevo libro con éxito ★ \n")
def listBooks():
    for i , book in enumerate(allBooks , 1):           
            print(f"Libro  {i}\n\n   Nombre: {book.get('Nombre','')} \n   Autor: {book.get('Autor','')} \n   Genero: {book.get('Genero','')} \n   Año de publicación: {book.get('Anio','')} \n   {book.get('Estado','')} \n -------------------------------- ")          
def showBooks():
    if not allBooks:
        print("★ Aún no tenemos libros en la biblioteca ★\n\n ") 
    else:
        print("★ ¡Ésta es nuestra colección de libros! ★ \n")
        listBooks()
def changeState():
    listBooks()
    option=int(input("\n¿A cual libro le quieres cambiar el estado? \n >>> "))
    book=allBooks[option-1] 
    book=book.get('Estado')
    book= "Leido ✔️"
    allBooks[option-1]['Estado']=book   
    print("\n Estado se cambio con éxito ")
def deleteBook():#falta proteger el input
    try:
        if not allBooks:
            print("¡No hay libros para eliminar!")
        else:            
            librosEliminados=[]
            listBooks()
            seleccion=int(input("Seleccione el libro que desea eliminar : "))
            librosEliminados=allBooks.pop(seleccion -1)
            print("libro eliminado con exito!")            
    except ValueError:
      print("opcion invalida ")
def searchBook():
    try:
        if not allBooks:
            print("¡No hay libros que buscar!\n")
        else:            
            librosEncontrados=[]
            seleccion=input("Quiere buscar por: \n 1 - Nombre \n 2 - Autor \n 3 - Genero\n >> ")  
            match seleccion:
                case '1':                   
                    busca_nombre=input("Nombre del libro:  ")
                    for i, libro  in enumerate(allBooks) :
                        nombre = libro.get('Nombre', '').lower()                           
                        if busca_nombre in nombre:
                            librosEncontrados.append(libro)
                    if not librosEncontrados:
                        print("¡No se encontraron coincidencias!")                        
                    else:
                        print(f"\n Coincidencias con tu busqueda: {len(librosEncontrados)}\n")
                        for i , book in enumerate(librosEncontrados , 1):           
                            print(f"Libro  {i}\n\n   Nombre: {book.get('Nombre','')} \n   Autor: {book.get('Autor','')} \n   Genero: {book.get('Genero','')} \n   Año de publicación: {book.get('Anio','')} \n   {book.get('Estado','')} \n -------------------------------- ")
                case '2':
                    busca_autor=input("Autor del libro:  ")
                    for i, libro  in enumerate(allBooks) :
                        autor = libro.get('Autor', '').lower()                           
                        if busca_autor in autor:
                            librosEncontrados.append(libro)
                    if not librosEncontrados:
                        print("¡No se encontraron coincidencias!")                        
                    else:
                        print(f"\n Coincidencias con tu busqueda: {len(librosEncontrados)}\n")
                        for i , book in enumerate(librosEncontrados , 1):           
                            print(f"Libro  {i}\n\n   Nombre: {book.get('Nombre','')} \n   Autor: {book.get('Autor','')} \n   Genero: {book.get('Genero','')} \n   Año de publicación: {book.get('Anio','')} \n   {book.get('Estado','')} \n -------------------------------- ")
                    
                case '3':
                    busca_genero=input("Genero del libro:  ")
                    for i, libro  in enumerate(allBooks) :
                        genero = libro.get('Genero', '').lower()                           
                        if busca_genero in genero:
                            librosEncontrados.append(libro)
                    if not librosEncontrados:
                        print("¡No se encontraron coincidencias!")                        
                    else:
                        print(f"\n Coincidencias con tu busqueda: {len(librosEncontrados)}\n")
                        for i , book in enumerate(librosEncontrados , 1):           
                            print(f"Libro  {i}\n\n   Nombre: {book.get('Nombre','')} \n   Autor: {book.get('Autor','')} \n   Genero: {book.get('Genero','')} \n   Año de publicación: {book.get('Anio','')} \n   {book.get('Estado','')} \n -------------------------------- ")
                case _:
                    print("Está ingresando una opción inválida!")
                    u.pause()    
    except ValueError :
        ("Error 404")       
def statistics():
    generos=[]
    conteo={}
    leidos=0
    noleidos=0
    for i , book in enumerate(allBooks):
        t=book.get('Estado', '')
        generos.append(book.get('Genero'))
        if t == "Leido ✔️":
            leidos+=1
        else:
            noleidos+=1
    for i in generos:
        if i in conteo:
            conteo[i] +=1 
        else:
            conteo[i]=1
    generomax = max(conteo, key=conteo.get)
    print(f"Total libros: {len(allBooks)}")
    print(f"\nLibros leidos  ✔️   {leidos}")
    print(f"\nLibros Por leer ⏳   {noleidos}")
    print(f"\nEl genero mas frecuente es:{generomax}\n")