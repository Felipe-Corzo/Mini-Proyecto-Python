import os
def clear ():
    os.system('cls' if os.name == 'nt' else 'clear')
def pause():
    input("presione enter para continuar.....")    

def exit():
    print("¡Hasta luego!")
    return False