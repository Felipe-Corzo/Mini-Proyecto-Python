MateriasDisponibles=set()
Estudiantes=[]
def validateID(id):   
    for estudiante in Estudiantes:
        if estudiante.get("Id",'') ==id:
           return True 
    return False

def validateSubject(materia):
    for i in MateriasDisponibles:
        if i.lower() == materia.lower():
            return True
    return False
            
def newSubject():
    materia=input("Ingrese nueva materia : ")
    MateriasDisponibles.add(materia)
    print(f"Ahora {materia} está disponible!")

def commonSubjectS():
    id1=int(input("ID primer estudiante: "))
    id2=int(input("ID segundo estudiante: "))
    for estudiante in Estudiantes:
        if id1==estudiante["Id"]:
            estudiante1= estudiante
    for estudiante in Estudiantes:
        if id2 == estudiante["Id"]:
            estudiante2=estudiante
        else:
            ("ID no existe. ")
    Me1=set(estudiante1['Materias'].keys())
    Me2=set(estudiante2['Materias'].keys())
    Mcomunes=Me1&Me2
    print(Mcomunes)

def newStudent():
    id=int(input("Id estudiante: "))
    if not validateID(id):      
        nombre=input("Nombre estudiante: ")
        Estudiantes.append({"Id":id, "Nombre": nombre, "Materias":{}})
        print(f"{nombre} Agregado con exito!")
    else:
        print("Error. ID ya está registrado.")  
def registerStudentsubject():
    try:
        if not MateriasDisponibles:
            print("No hay materias disponibles")
        else:
            id=int(input("Id estudiante: "))
            if validateID(id): 
                print(f"Materias disponibles: \n {MateriasDisponibles}")
                materia=input("Seleccione una Materia: ").lower()
                if validateSubject(materia):
                    for estudiante in Estudiantes:
                        if estudiante["Id"] == id: 
                            if materia not in estudiante["Materias"]:                      
                                estudiante["Materias"][materia] = []
                                print("Materia agregada correctamente")
                            else:
                                    print(f"El estudiante ya esta matriculado en {materia}")
                else:
                    print("No existe Materia.")
    except ValueError:
        print("Opción incorrecta.")

def registerNote():
    try:
        id=int(input("Id estudiante: "))
        if validateID(id):        
            for i, estudiante in enumerate(Estudiantes):
                   if estudiante["Id"] == id:
                        posicion=i
                        print(f"Seleccione materia para asignar calificación: \n {list(estudiante['Materias'].keys())}")
                        materia=input(">>>  ")
                        if materia in estudiante["Materias"]:
                            nota=float(input("Nota: "))
                            estudiante["Materias"][materia].append(nota)

                        else:
                            print("El estudiante no cursa esa materia.")    

    except ValueError:
        print("ID inválido.")

def generarReporte():
    for estudiante in Estudiantes:
        print(f"\n Reporte de {estudiante['Nombre']} (ID: {estudiante['Id']})")
        
        materias = estudiante["Materias"]
        suma_total = 0
        cantidad_total = 0

        for materia, notas in materias.items():
            if notas: 
                promedio = sum(notas) / len(notas)
                print(f"   - {materia}: {promedio:.2f}")
                suma_total += sum(notas)
                cantidad_total += len(notas)
            else:
                print(f"   - {materia}: Sin notas registradas")

        if cantidad_total > 0:
            promedio_general = suma_total / cantidad_total
            print(f"Promedio general: {promedio_general:.2f}")
        else:
            print("No hay notas registradas.")