import pygame
from utils.interface import enforcado, campeao
from os import system
from time import sleep
from utils.treat_text import remove_character


def main(letras_dig, palavra_s, copia_palavra_s, cont_e, cont_l):
   
    entrada = str(input('Digite uma letra ou a palavra completa(+2 erros): ')).strip().upper()

    if entrada == '':
        print('\nEntrada inválida. Por favor, digite algo.')
        sleep(2)
        system('cls') or None
        return cont_e, cont_l

    if entrada in letras_dig:
        print('\nVocê já digitou essa letra.')
        sleep(2)
        system('cls') or None
    elif len(entrada) > 1:
        if remove_character(entrada) != remove_character(palavra_s): # caso tente acertar a palavra completa
            cont_e += 2
        else:
            cont_l = len(palavra_s) #caso acerte a palavra completa
            for p, l in enumerate(palavra_s):
                copia_palavra_s[p] = l
    elif all(remove_character(entrada) != remove_character(l) for l in palavra_s):
        cont_e += 1
    else:
        for p, l in enumerate(palavra_s):
            if remove_character(entrada) == remove_character(l):
                if remove_character(entrada) not in letras_dig:
                    copia_palavra_s[p] = l
                    cont_l += 1

    if remove_character(entrada) not in letras_dig and entrada != '': # adiciona uma entrada digitada em uma lista
        letras_dig.append(remove_character(entrada))

    return cont_e, cont_l


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


def end(cont_e, palavra_s, musica_perdeu, musica_ganhou ):
    if cont_e >= 6:
        enforcado(palavra_s)
        defeat_music(musica_perdeu) # toca música de perdedor
    else:
        campeao()
        victory_music(musica_ganhou) # toca música de vitória

def verification(cont_l, palavra_s, cont_e, MAX_E, vit, der):
    if cont_l == len(palavra_s) or cont_e >= MAX_E: # condição de parada
        if cont_l >= len(palavra_s): # acertou a palavra 
            vit += 1
        else:
            der += 1 # errou a palavra
        return True, vit, der
    return False, vit, der  # <- retorno padrão caso o jogo ainda não tenha terminado
            