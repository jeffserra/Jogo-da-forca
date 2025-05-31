import pygame
from os import system
from time import sleep
from random import choice

# importação dos módulos locais
from utils.data import dic
from utils.interface import * #importa tudo do modulo interface
from utils.logic import *

pygame.mixer.init()
pygame.init()

#constantes
MAX_ERROS = 6
MUSIC_LOOP = -1 # -1 para repetir indefinidamente
BACKGROUND_MUSIC = "sound_effects/background.mp3"
DEFEAT_SOUND = "sound_effects/defeat.mp3"
VICTORY_SOUND = "sound_effects/victory.mp3"

# carrega as chaves do dicionário em uma lista
chaves = [c for c in dic.keys()]

vitorias = derrotas = 0

while True:
    # inicializa as variáveis
    dica = choice(chaves)
    p_secreta = choice(dic[dica]).upper()
    cont_letra = 0
    cont_erro = 0
    palavra_lista = list()
    copia = []
    l_dig = list()

    for l in p_secreta:
        palavra_lista.append(l)
        if l == ' ':
            cont_letra += 1
        copia.append(' ')

    # toca música de fundo
    BG(BACKGROUND_MUSIC, MUSIC_LOOP)

    while True:
        system('cls') or None

        mostrar(cont_erro, dica, copia, palavra_lista, l_dig, p_secreta)

        cont_erro, cont_letra = main(l_dig, p_secreta, palavra_lista, copia, cont_erro, cont_letra)

        interromper, vitorias, derrotas = verification(cont_letra, palavra_lista, cont_erro, MAX_ERROS, vitorias, derrotas)

        if interromper:
            break
    
    system('cls') or None
    mostrar(cont_erro, dica, copia, palavra_lista, l_dig, p_secreta)
    sleep(2)
    system('cls') or None

    end(cont_erro, p_secreta, DEFEAT_SOUND, VICTORY_SOUND)
    
    sleep(3)
    if not continuar(): # pergunta se quer continuar
        break

system('cls') or None

placar(vitorias, derrotas) # mostra o placar
