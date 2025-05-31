cor = ('\033[m',  # sem cor
       '\033[1;32m',  # verde
       '\033[1;31m',  # vermelho
       '\033[1;30;107m',  # branco
       '\033[1;33m')  # amarelo

def cabeçalho(cont_e):
    print(cor[2], end='')
    print('-' * 45)
    print(f'{"JOGO DA FORCA":^45}')
    print('-' * 45)
    print(f'ERROS: {cont_e} ')
    print('-' * 45)
    print(cor[0])
    

def mostrar(cont_e, pista, copia_palavra_s, palavra_l, letras_dig, palavra_s):
    cabeçalho(cont_e)
    
    forca(cont_e)

    print(f'\n\nDica: {pista}\n\n')

    for l in copia_palavra_s:
        print(f'{l} ', end='')
    print('')

    for l in palavra_l:
        if l == ' ':
            print('  ', end='')
        else:
            print('- ', end='')
    print('')

    print('\nLetras digitadas: ', end='')
    for l in letras_dig:
        if len(l) > 1:
            if l != palavra_s:
                print(f'{cor[2]}{l}{cor[0]}', end=' ')
            else:
                print(f'{cor[1]}{l}{cor[0]}', end=' ')
        elif l not in palavra_l:
            print(f'{cor[2]}{l}{cor[0]}', end=' ')
        else:
            print(f'{cor[1]}{l}{cor[0]}', end=' ')
    print('\n')


def forca(cont_e):
    if cont_e == 0:
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

    elif cont_e == 1:
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

    elif cont_e == 2:
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
    elif cont_e == 3:
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
    elif cont_e == 4:
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
    elif cont_e == 5:
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


def enforcado(palavra_s):
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
    print(f'\nA PALAVRA ERA: {palavra_s}')
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
