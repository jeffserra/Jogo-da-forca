cor = ('\033[m',  # sem cor
       '\033[1;32m',  # verde
       '\033[1;31m',  # vermelho
       '\033[1;30;107m',  # branco
       '\033[1;33m')  # amarelo

def cabeçalho(erro):
    print(cor[2], end='')
    print('-' * 45)
    print(f'{"JOGO DA FORCA":^45}')
    print('-' * 45)
    print(f'ERROS: {erro} ')
    print('-' * 45)
    print(cor[0])
    

def mostrar(copia, palavra, l_dig, dica, erro):
    cabeçalho(erro)
    
    forca(erro)

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


def forca(erro):
    if erro == 0:
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

    elif erro == 1:
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

    elif erro == 2:
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
    elif erro == 3:
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
    elif erro == 4:
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
    elif erro == 5:
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
        print('  |      (x_X)')
        print('  |       ---')
        print('  |       \\|/')
        print('  |        |')
        print('  |       / \\')
        print('  |')
        print('  |')
        print('-----')


def enforcado(secreta):
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
    print(f'\nA PALAVRA ERA: {secreta}')
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


def placar(vic, der):
    print(cor[2], end='')
    print('-' * 45)
    print(f'{"PLACAR":^45}')
    print('-' * 45)                           
    print(f'NÚMERO DE VITÓRIAS:           {vic}')
    print('-' * 45)
    print(f'NÚMERO DE DERROTAS:           {der}')
    print('-' * 45)
    print(cor[0])
