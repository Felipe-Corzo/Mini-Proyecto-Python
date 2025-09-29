import modules.mesagges as m
import modules.CRUD as c
import modules.utils as u
def main():
    Active = True
    while Active:
        u.clear() 
        opcion= m.menu()
        match opcion:
            case '1':
                u.clear()
                c.registrar_usuario()
                u.pause()
            case '2':
                u.clear()
                c.agregar_libro()
                u.pause()
            case '3':
                u.clear()
                c.prestar_libro()
                u.pause()
            case'4':
                u.clear()
                c.devolver_libro()
                u.pause()
            case '5': 
                u.clear()
                c.recomendar_libros()
                u.pause()
            case '6':
                u.clear()
                c.analisis_usuarios()
                u.pause()
            case '0': 
                Active= exit()
            case _ :
                print("Está ingresando un dato inválido. Por favor intente nuevamente!")
                u.pause()