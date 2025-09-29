all_games = []

def new_game ():
    name=input("Nombre del Video juego: ")
    genero=input("Genero: ") 
    state="✗"
    date_game= (name , genero , state)
    all_games.append(date_game)
    print("\n ★ Haz agregado un nuevo juego con éxito ★ \n")

def show_games():
    if not all_games:
        print("★Aún no tenemos colección de video juegos★\n\n ") 
    else:
        print("★ ¡Ésta es nuestra colección de video juegos! ★ \n")
        print("N | NOMBRE \t| GENERO \t| ESTADO  |\n")
        for i , game in enumerate(all_games , 1):
            print(f"{i} | {game[0]} \t| {game[1]} \t|    {game[2]}    | \n")



def update_game():
    show_games(), "\n"
    try:
        if all_games:            
            indice=int(input("¿Que video juego quiere actualizar? \n\n >> Seleccione un numero:   "))
            if indice > 0 and indice < len(all_games) + 1 :
                game=all_games[indice -1]
                name , genero , state = game
                state= "✓"
                newgame= name , genero , state 
                all_games[indice -1]= newgame
                print("\n★ Actualizaste el estado del video juego con éxito ★\n")
    except ValueError:
        print("Por favor seleccione una opción válida")
        indice=int(input(">> Seleccione un numero:   "))


def statistics():
    sum_all= len(all_games)
    complet=0
    incomplets=0
    for i in all_games:
        if i[2] == "✓":
            complet=complet +1
        else :
            incomplets= incomplets +1
    print(f"Cantidad de juegos: {sum_all} \n ")
    print(f"Juegos completados: {complet} \n")
    print(f"Juegos incompletos: {incomplets} \n")
