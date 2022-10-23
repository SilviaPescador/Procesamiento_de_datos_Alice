from alice_texts import *
import re

#____________________________PRUEBAS_______________________________
def remove_punctuation_suffix(cadena):
    '''
    Elimina de una cadena:
    - signos indeseados 
    - sufijos
    - espacios múltiples
    - los números
    Devuelve una cadena limpia.
    '''
    signos_out = '[\\!\\"\\“\\”\\’\\#\\$\\%\\&\\(\\)\\*\\+\\,\\-\\—\\.\\/\\:\\;\\<\\=\\>\\?\\@\\[\\\\\\]\\^_\\`\\{\\|\\}\\~\\´]'
    limp = re.sub(signos_out , ' ', cadena)
    limp = limp.replace('\'s', '')
    limp = re.sub("\\s+", ' ', limp)
    limp = re.sub("\d+", ' ', limp)
    return limp

def tokeniza(cadena):
    '''
    Separa las palabras de una cadena y devuelve una lista de palabras.
    '''
    tokenizada = cadena.split(' ')
    return tokenizada

def normalize(lista_palabras):
    '''
    Devuelve lista de cadenas sin sufijos, simbolos, ni espacios indeseados, 
    con cada item en minúsculas.
    '''
    
    return list(map(lambda x: remove_punctuation_suffix(x).lower(), lista_palabras))

# ____________________________USADAS_________________________________


def normalize_tokenize(texto):
    '''
    Elimina de una cadena:
    - signos indeseados 
    - sufijos (- convierte i'll en i will)
    - espacios múltiples
    - números
    - pasa palabras a minúsculas
    - tokeniza la cadena
    Devuelve una lista limpia de palabras(tokens).
    '''
    limp = texto.lower()
    signos_out = '[\\!\\"\\\'\\“\\”\\“\\’\\‘\\#\\$\\%\\&\\(\\)\\*\\+\\,\\-\\—\\.\\/\\:\\;\\<\\=\\>\\?\\@\\[\\\\\\]\\^_\\`\\{\\|\\}\\~\\´]'
    limp = re.sub(signos_out , ' ', texto)
    limp = limp.replace('\'s', '') 
    limp = re.sub("\\s+", ' ', limp)
    limp = re.sub("\d+", ' ', limp)
    #tokeniza una vez limpia
    limp = limp.split(' ')
    return limp


def remove_stopwords(lista_palabras, predicado):
    '''
    Elimina de una lista de cadenas, los items presentes en un set de stopwords.
    Devuelve una nueva lista de cadenas sin las stopwords.
    '''
    return  list(filter(lambda x : x not in predicado, lista_palabras))


def count_words(lista_palabras):
    '''
    Devuelve un diccionario donde la clave es la palabra y su valor,
    el número de veces que se repite en una lista de palabras. (a ser
    posible ya normalizada y tokenizada)
    '''
    dict_ocurr = {}
    for word in lista_palabras:
        if word not in dict_ocurr.keys():
            dict_ocurr[word] = 1
        else:
            dict_ocurr[word] += 1
    return dict_ocurr


def word_probability(count_words):
    return dict(map(lambda x : (x[0], round((x[1] / len(count_words)*100), 2)), count_words.items()))


def display_histogram(dict_word_prob):
    for palabra, prob in dict_word_prob.items():
        return (f"{palabra} - {'#'* int(prob)}")


# ___________________ALICICE IN WONDERLAND__________________________

# NORMALIZO Y TOKENIZO TEXTO ALICE Y STOPWORDS
a_limp = normalize_tokenize(lines)
sw_limp = normalize_tokenize(contents)

# PASO STOPWORDS A SET
stopwords_set = set(sw_limp)
#print(stopwords_set)

# ELIMINO STOPWORDS DE ALICIA
alicia_sin = remove_stopwords(a_limp, stopwords_set)
# print(alicia_sin)

# CREO DICCIONARIO: CLAVE-palabras//VALOR-nº ocurrencia de la palabra.
alicia_ocurr = count_words(alicia_sin)
# print(alicia_ocurr)

# DICCIONARIO: CLAVE-palabras //VALOR-probabilidad ocurrencia.
alicia_prob = word_probability(alicia_ocurr)
print(alicia_prob)

#HISTOGRAMA: representación del diccionario de probabilidades.
histogram = display_histogram(alicia_prob)
# print(histogram)