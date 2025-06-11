import unicodedata
import re

def remove_character(palavra):
    # Substitui hífens por espaços
    palavra = palavra.replace('-', ' ')
    # Normaliza para separar acentos
    normalizada = unicodedata.normalize('NFD', palavra)
    # Remove os acentos
    sem_acento = normalizada.encode('ascii', 'ignore').decode('utf-8')
    # Remove tudo que não seja letra, número ou espaço
    apenas_validos = re.sub(r'[^A-Za-z0-9 ]', '', sem_acento)
    # Reduz múltiplos espaços para um único espaço, converte para maiúsculas e retorna
    return re.sub(r'\s+', ' ', apenas_validos).strip().upper()
    