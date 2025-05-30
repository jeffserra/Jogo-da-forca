import pygame

def continuar():
    while True:
        op = str(input('\nQuer continuar? [S/N]: ')).strip().upper()

        if op in 'SN' and op != '':
            break
        else:
            print('\nOpção inválida, por favor digite S ou N.\n')
    if op ==  'N':
        return False
    else:
        return True

def BG(caminho, loop):
    pygame.mixer.music.load(caminho)
    pygame.mixer.music.play(loop)


def defeat_music(caminho):
    pygame.mixer.music.load(caminho)
    pygame.mixer.music.play()


def victory_music(caminho):
    pygame.mixer.music.load(caminho)
    pygame.mixer.music.play()

