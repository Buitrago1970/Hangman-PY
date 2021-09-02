import random
from os import system


def selecionar_palabra():
    with open('./data/data.txt', 'r', encoding=('utf-8')) as f:
        # rstrip para quitar los saltos de linea (\n)
        words = [word.rstrip() for word in f]
        mystery_word = random.choice(words)
        return mystery_word


def comprobar_letra(mystery_word, user_word):
    for x in range(len(mystery_word)):
        if(mystery_word[x] == user_word):
            return True
    return False


def cambiar_letra(mystery_word, user_word, resolved_word):
    resolved_word = list(resolved_word)
    for x, j in enumerate(resolved_word):
        if(mystery_word[x] == user_word):
            resolved_word[x] = user_word
            system('cls')

    return resolved_word


def run():
    vidas = 5

    print("""                                   Bienvenido a juego del""")
    print("""
                                      
                                    )                   (        
                                ) ( /(     (          )  )\ )     
                            ( /( )\()) (  )(   (  ( /( (()/( (   
                            )(_)|(_)\  )\(()\  )\ )(_)) ((_)))\  
                            ((_)_| |(_)((_)((_)((_|(_)_  _| |((_) 
                            / _` | ' \/ _ \ '_/ _|/ _` / _` / _ \ 
                            \__,_|_||_\___/_| \__|\__,_\__,_\___/ 
                                      
""")
    # selecionar una palabra alazar
    mystery_word = selecionar_palabra()
    # copia de la palabra secreta cambiando letras por (-)
    resolved_word = "-" * len(mystery_word)
    print(mystery_word)
    mystery_word = list(mystery_word)
    # ciclo del juego
    while(True):
        if(mystery_word == resolved_word):
            print(""" $$$$$$\                                           $$\             $$\ 
$$  __$$\                                          $$ |            $$ |
$$ /  \__| $$$$$$\  $$$$$$$\   $$$$$$\   $$$$$$$\$$$$$$\   $$$$$$\ $$ |
$$ |$$$$\  \____$$\ $$  __$$\  \____$$\ $$  _____\_$$  _| $$  __$$\$$ |
$$ |\_$$ | $$$$$$$ |$$ |  $$ | $$$$$$$ |\$$$$$$\   $$ |   $$$$$$$$ \__|
$$ |  $$ |$$  __$$ |$$ |  $$ |$$  __$$ | \____$$\  $$ |$$\$$   ____|   
\$$$$$$  |\$$$$$$$ |$$ |  $$ |\$$$$$$$ |$$$$$$$  | \$$$$  \$$$$$$$\$$\ 
 \______/  \_______|\__|  \__| \_______|\_______/   \____/ \_______\__|""")
            print('La palabra era:')
            print(''.join(resolved_word))
            break
        if(vidas <= 0):
            print("""
 ______  ______  ______  _____   __  ______  ______  ______    
/\  == \/\  ___\/\  == \/\  __-./\ \/\  ___\/\__  _\/\  ___\   
\ \  _-/\ \  __\\ \  __<\ \ \/\ \ \ \ \___  \/_/\ \/\ \  __\   
 \ \_\   \ \_____\ \_\ \_\ \____-\ \_\/\_____\ \ \_\ \ \_____\ 
  \/_/    \/_____/\/_/ /_/\/____/ \/_/\/_____/  \/_/  \/_____/ 
                                                               
""")
            print('La palabra era:')
            print(''.join(mystery_word))
            break
        else:
            print('Recuerda: Tienes ' + str(vidas) + ' vidas. Ten cuidado')
            print(''.join(resolved_word))
            user_word = input('Ingrese una letra: ')
            if(comprobar_letra(mystery_word, user_word)):
                resolved_word = cambiar_letra(
                    mystery_word, user_word, resolved_word)
            else:
                vidas -= 1


if __name__ == '__main__':
    run()
