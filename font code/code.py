import pygame
from os import system
from time import sleep
from random import choice

dic = {
    "Filme": [
        "HOMEM ARANHA", "STAR WARS", "MEU MALVADO FAVORITO", "HOMEM FORMIGA", "SHREK",
        "TOY STORY", "TITANIC", "VELOZES E FURIOSOS", "O REI LEAO", "MADAGASCAR",
        "JURASSIC PARK", "OS INCRIVEIS", "FROZEN", "ALADDIN", "BATMAN",
        "SUPERMAN", "A BELA E A FERA", "PIRATAS DO CARIBE", "AVATAR", "PLANETA DOS MACACOS"
    ],
    "Fruta": [
        "UVA", "TANJA", "GOIABA", "MURTA", "MURICI", "ABACATE", "AMOROSA",
        "BANANA", "MANGA", "MORANGO", "LARANJA", "CAJU", "MARACUJA",
        "ABACAXI", "COCO", "PITANGA", "JABUTICABA", "PERA", "MELANCIA",
        "KIWI", "MELAO", "TAMARINDO", "FRAMBOESA"
    ],
    "Lugar": [
        "LAGO DAS PEDRAS", "AXIXA", "SANTA LUZIA", "SANTA INES", "ROSARIO",
        "RIO DE JANEIRO", "SAO PAULO", "BELO HORIZONTE", "FORTALEZA", "RECIFE",
        "SALVADOR", "PORTO ALEGRE", "MANAUS", "BRASILIA", "CURITIBA",
        "CAMPINAS", "NATAL", "GOIANIA", "JOAO PESSOA", "FLORIANOPOLIS"
    ],
    "Animal": [
        "CACHORRO", "GATO", "ELEFANTE", "GIRAFA", "LEAO",
        "TIGRE", "COBRA", "TARTARUGA", "PAPAGAIO", "LOBO",
        "JACARE", "ARARA", "GORILA", "ORNITORRINCO", "CAVALO",
        "RINOCERONTE", "GALO", "TAMANDUA", "PANDA", "FALCAO"
    ],
    "Objeto": [
        "CADEIRA", "MESA", "COMPUTADOR", "CELULAR", "GELADEIRA",
        "TELEVISAO", "LIVRO", "CADERNO", "CANETA", "LAMPADA",
        "TESOURA", "RELOGIO", "MOCHILA", "FONE DE OUVIDO", "CHAVE",
        "GUITARRA", "ASPIRADOR", "BICICLETA", "PANELA", "MICROONDAS"
    ],
    "Profissão": [
        "MEDICO", "PROFESSOR", "ENGENHEIRO", "CANTOR", "ADVOGADO",
        "JORNALISTA", "ARQUITETO", "VETERINARIO", "PILOTO", "BOMBEIRO",
        "POLICIAL", "DENTISTA", "PSICOLOGO", "COSTUREIRA", "MOTORISTA",
        "BARBEIRO", "ELETRICISTA", "PINTOR", "PROGRAMADOR", "ATOR"
    ],
    "Time de Futebol": [
        "FLAMENGO", "CORINTHIANS", "SAO PAULO", "PALMEIRAS", "VASCO",
        "SANTOS", "INTERNACIONAL", "GREMIO", "FLUMINENSE", "CRUZEIRO",
        "ATLETICO MINEIRO", "BAHIA", "FORTALEZA", "BOTAFOGO", "SPORT",
        "GOIAS", "CUIABA", "ATLETICO PARANAENSE", "CHAPECOENSE", "CEARA"
    ],
    "País": [
        "BRASIL", "ARGENTINA", "EUA", "ALEMANHA", "FRANCA",
        "ITALIA", "JAPAO", "CHINA", "ESPANHA", "PORTUGAL",
        "CANADA", "MEXICO", "INGLATERRA", "AUSTRALIA", "RUSSIA",
        "INDIA", "AFRICA DO SUL", "COREIA DO SUL", "CHILE", "PERU"
    ],
    "Cor": [
        "VERMELHO", "AZUL", "VERDE", "AMARELO", "PRETO",
        "BRANCO", "LARANJA", "ROXO", "CINZA", "MARROM",
        "ROSA", "BEGE", "VIOLETA", "TURQUESA", "DOURADO",
        "PRATA", "BORDO", "SALMAO", "ANIL", "CARMESIM"
    ],
    "Personagem": [
        "MICKEY MOUSE", "HARRY POTTER", "BATMAN", "SUPERMAN", "HOMEM ARANHA",
        "HOMER SIMPSON", "GOKU", "NARUTO", "SONIC", "MARIO",
        "LUIGI", "SCOOBY DOO", "PATRICK ESTRELA", "BOB ESPONJA", "SHERLOCK HOLMES",
        "DARTH VADER", "YODA", "LARA CROFT", "KRATOS", "MEGAMAN"
    ]
}

cor = ('\033[m',  # sem cor
       '\033[1;32m',  # verde
       '\033[1;31m',  # vermelho
       '\033[1;30;107m',  # branco
       '\033[1;33m')  # amarelo

def cabeçalho():
    print(cor[2], end='')
    print('-' * 45)
    print(f'{"JOGO DA FORCA":^45}')
    print('-' * 45)
    print(f'ERROS: {cont_erro} ')
    print('-' * 45)
    print(cor[0])

def mostrar():
    cabeçalho()
    
    forca()

    print(f'\n\nDica: {dica}\n\n')

    for l in copia:
        print(f'{l} ', end='')
    print('')

    for l in palavra:
        if l == ' ':
            print('  ', end='')
        else:
            print('- ', end='')
    print('')

    print('\nLetras digitadas: ', end='')
    for l in l_dig:
        if l not in palavra:
            print(f'{cor[2]}{l}{cor[0]}', end=' ')
        else:
            print(f'{cor[1]}{l}{cor[0]}', end=' ')
    print('\n')


def forca():
    if cont_erro == 0:
        print('   ________')
        print('  |        |')
        print('  |')
        print('  |')
        print('  |')
        print('  |')
        print('  |')
        print('  |')
        print('  |')
        print('  |')
        print('-----')

    elif cont_erro == 1:
        print('   ________')
        print('  |        |')
        print('  |       ---')
        print('  |      (^0^)')
        print('  |       ---')
        print('  |')
        print('  |')
        print('  |')
        print('  |')
        print('  |')
        print('-----')

    elif cont_erro == 2:
        print('   ________')
        print('  |        |')
        print('  |       ---')
        print('  |      (^0^)')
        print('  |       ---')
        print('  |        |')
        print('  |        |')
        print('  |')
        print('  |')
        print('  |')
        print('-----')
    elif cont_erro == 3:
        print('   ________')
        print('  |        |')
        print('  |       ---')
        print('  |      (^0^)')
        print('  |       ---')
        print('  |       \\|')
        print('  |        |')
        print('  |')
        print('  |')
        print('  |')
        print('-----')
    elif cont_erro == 4:
        print('   ________')
        print('  |        |')
        print('  |       ---')
        print('  |      (^0^)')
        print('  |       ---')
        print('  |       \\|/')
        print('  |        |')
        print('  |')
        print('  |')
        print('  |')
        print('-----')
    elif cont_erro == 5:
        print('   ________')
        print('  |        |')
        print('  |       ---')
        print('  |      (^0^)')
        print('  |       ---')
        print('  |       \\|/')
        print('  |        |')
        print('  |       / ')
        print('  |')
        print('  |')
        print('-----')
    else:
        print('   ________')
        print('  |        |')
        print('  |       ---')
        print('  |      (^0^)')
        print('  |       ---')
        print('  |       \\|/')
        print('  |        |')
        print('  |       / \\')
        print('  |')
        print('  |')
        print('-----')


def enforcado():
    print(cor[2], end='')
    print('\nVOCÊ FOI ENFORCADO !!!\n')
    print('     __________ ')
    print('    /          \\')
    print('   /  **    **  \\')
    print('  |   **    **   |')
    print('   \\            /')
    print('    \\     x    /')
    print('     |        |')
    print('     | !!!!!! |')
    print('      \\ !!!! /')
    print('       ------')
    print(f'\nA PALAVRA ERA: {p_secreta}')
    print(cor[0])


def campeao():
    print(cor[4], end='')
    print('\nPARABÉNS, VOCÊ GANHOU !\n')
    print('    ______________')
    print('   |:::           |')
    print('    --------------')
    print('    \\::          /')
    print('     \\::        /')
    print('    __\\::      /__')
    print('   / __\\::    /__ \\')
    print('   \\ \\  \\:   /  / /')
    print('    \\ \\__|  |__/ /')
    print('     \\___|  |___/')
    print('         |  |')
    print('        /    \\ ')
    print('        ------')
    print('       | ☆☆☆  |')
    print('        ------')
    print(cor[0])


pygame.mixer.init()
pygame.init()

chaves = list()
for c in dic.keys():
    chaves.append(c)

vic = der = 0

while True:
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

    pygame.mixer.music.load("sound effects/background.mp3")
    pygame.mixer.music.play(-1) # -1 música repete indefinidamente

    while True:
        system('cls') or None

        mostrar()

        letra = str(input('Digite uma letra: ')).strip().upper()

        if letra in l_dig:
            print('\nVocê já digitou essa letra')
            sleep(2)
            system('cls') or None
        elif letra not in palavra and letra != '':
            cont_erro += 1
        else:
            for p, l in enumerate(palavra):
                if letra == l:
                    if letra not in l_dig:
                        copia[p] = l
                        cont += 1

        if letra not in l_dig and letra != '':
            l_dig.append(letra)

        if cont == len(palavra) or cont_erro == 6:
            if cont == len(palavra):
                vic += 1
            else:
                der += 1
            break

    mostrar()
    sleep(2)
    system('cls') or None

    if cont_erro == 6:
        enforcado()
        pygame.mixer.music.load("sound effects/defeat.mp3")
        pygame.mixer.music.play(loops=0, start=0.0)
        #pygame.event.wait()

    else:
        campeao()
        pygame.mixer.music.load("sound effects/victory.mp3")
        pygame.mixer.music.play(loops=0, start=0.0)
        #pygame.event.wait()
    
    sleep(3)
    while True:
        continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()

        if continuar in 'SN' and continuar != '':
            break
        else:
            print('\nOpção inválida, por favor digite S ou N.\n')
    
    if continuar == 'N':
        break

system('cls') or None

print(cor[2], end='')
print('-' * 45)
print(f'{"PLACAR":^45}')
print('-' * 45)                           
print(f'NÚMERO DE VITÓRIAS:           {vic}')
print('-' * 45)
print(f'NÚMERO DE DERROTAS:           {der}')
print('-' * 45)
print(cor[0])
