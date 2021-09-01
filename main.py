import random


def selecionar_palabra():
    with open('./data/data.txt', 'r', encoding=('utf-8')) as f:
        # rstrip para quitar los saltos de linea (\n)
        words = [word.rstrip() for word in f]
        mystery_word = random.choice(words)
        print(mystery_word)
        return mystery_word


def convertir_palabra_secreta(mystery_word):
    resolved_word = ''
    for x in range(0, len(mystery_word)):
        resolved_word += '-'
    return resolved_word


def comprobar_letra(mystery_word, user_word, resolved_word):
    resolved_word = list(resolved_word)
    for x, j in enumerate(resolved_word):
        if(mystery_word[x] == user_word):
            resolved_word[x] = user_word
    return resolved_word


def run():

    print('Bienvenido a juego del ahorcado 👻')
    print('!Adivina la Palabra!')
    # selecionar una palabra alazar
    mystery_word = selecionar_palabra()

    resolved_word = convertir_palabra_secreta(mystery_word)
    mystery_word = list(mystery_word)
    while(True):
        if(mystery_word == resolved_word):
            print('gano')
            break
        else:
            print(' '.join(resolved_word))
            user_word = input('Ingrese una letra: ')
            resolved_word = comprobar_letra(
                mystery_word, user_word, resolved_word)


if __name__ == '__main__':
    run()
