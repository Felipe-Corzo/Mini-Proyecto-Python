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
                c.newStudent()
                u.pause()
            case '2':
                u.clear()
                c.newSubject()
                u.pause()
            case '3':
                u.clear()
                c.registerStudentsubject()
                u.pause()
            case'4':
                u.clear()
                c.registerNote()
                u.pause()
            case '5': 
                u.clear()
                c.commonSubjectS()
                u.pause()
            case '6':
                u.clear()
                c.generarReporte()
                u.pause()
            case '0': 
                Active= exit()
            case _ :
                print("Está ingresando un dato inválido. Por favor intente nuevamente!")
                u.pause()