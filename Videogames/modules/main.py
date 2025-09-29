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
                c.new_game()
                u.pause()
            case '2':
                u.clear()
                c.show_games()
                u.pause()
            case '3':
                u.clear()
                c.update_game()
                u.pause()
            case '4':
                u.clear()
                c.statistics()
                u.pause()
            case '0': 
                Active= exit()
            case _ :
                print("Está ingresando un dato inválido. Por favor intente nuevamente!")
                u.pause()