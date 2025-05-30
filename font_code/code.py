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
    p_secreta =choice(dic[dica]).upper()
    cont = 0
    cont_erro = 0
    palavra = list()
    copia = []
    l_dig = list()

    for l in p_secreta:
        palavra.append(l)
        if l == ' ':
            cont += 1
        copia.append(' ')

    # toca música de fundo
    BG(BACKGROUND_MUSIC, MUSIC_LOOP)

    while True:
        system('cls') or None

        mostrar(copia, palavra, l_dig, dica, cont_erro)

        entrada = str(input('Digite uma letra ou a palavra completa(+2 erros): ')).strip().upper()

        if entrada in l_dig:
            print('\nVocê já digitou essa letra')
            sleep(2)
            system('cls') or None
        elif len(entrada) > 1:
            if entrada != p_secreta and entrada != '': # caso tente acertar a palavra completa
                cont_erro += 2
            else:
                cont = len(palavra) #caso acerte a palavra completa
        elif entrada not in palavra and entrada != '':
            cont_erro += 1
        else:
            for p, l in enumerate(palavra):
                if entrada == l:
                    if entrada not in l_dig:
                        copia[p] = l
                        cont += 1

        if entrada not in l_dig and entrada != '': # adiciona uma entrada digitada em uma lista
            l_dig.append(entrada)

        if cont == len(palavra) or cont_erro >= MAX_ERROS: # condição de parada
            if cont >= len(palavra): # acertou a palavra 
                vitorias += 1
            else:
                derrotas += 1 # errrou a palavra
            break

    mostrar(copia, palavra, l_dig, dica, cont_erro)
    sleep(2)
    system('cls') or None

    if cont_erro == 6:
        enforcado(p_secreta) 
        defeat_music(DEFEAT_SOUND) # toca música de perdedor

    else:
        campeao()
        victory_music(VICTORY_SOUND) # toca música de vitória
    
    sleep(3)
    if not continuar(): # pergunta se quer continuar
        break

system('cls') or None

placar(vitorias, derrotas) # mostra o placar
