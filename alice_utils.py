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

def normalize(list_palabras):
    '''
    Devuelve lista de cadenas sin sufijos, simbolos, ni espacios indeseados, 
    con cada item en minúsculas.
    '''
    
    return list(map(lambda x: remove_punctuation_suffix(x).lower(), list_palabras))

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


def remove_stopwords(list_palabras, predicado):
    '''
    Elimina de una lista de cadenas, los items presentes en un set de stopwords.
    Devuelve una nueva lista de cadenas sin las stopwords.
    '''
    return  list(filter(lambda x : x not in predicado, list_palabras))


def count_words(list_palabras):
    '''
    Devuelve un diccionario donde la clave es la palabra y su valor,
    el número de veces que se repite en una lista de palabras. (a ser
    posible ya normalizada y tokenizada)
    '''
    dict_ocurr = {}
    for word in list_palabras:
        if word not in dict_ocurr.keys():
            dict_ocurr[word] = 1
        else:
            dict_ocurr[word] += 1
    return dict_ocurr


def word_probability(diccionario):
    '''
    Recibe un diccionario (palabras de un texto : nº ocurrencias de esa palabra), y devuelve 
    otro cambiando los valores por su probabilidad de aparecer en el texto. 
    Divide los valores, entre el nº total de palabras incluyendo repeticiones, *100.
    
    '''
    return dict(map(lambda x :(x[0] , round((x[1] / sum(diccionario.values()))*100, 2)), diccionario.items()))


def display_histogram(diccionario):
    for palabra, valor in diccionario.items():
        repre = '#' * round(valor)
        print (f"{palabra}- {valor :30}{repre}")
 


# ___________________CASO CONCRETO: ALICICE IN WONDERLAND__________________________

# NORMALIZO Y TOKENIZO TEXTO ALICE Y STOPWORDS
clean_alice = normalize_tokenize(lines)
clean_stopw = normalize_tokenize(contents)

# PASO STOPWORDS A SET
stopwords_set = set(clean_stopw)
# print(stopwords_set)

# ELIMINO STOPWORDS DE ALICIA
alicia_sin = remove_stopwords(clean_alice, stopwords_set)
# print(alicia_sin)

# CREO DICCIONARIO: CLAVE-palabras//VALOR-nº ocurrencia de la palabra.
ocurrence_d = count_words(alicia_sin)
# print(ocurrence_d)

# DICCIONARIO: CLAVE-palabras //VALOR-probabilidad ocurrencia.
probability_d = word_probability(ocurrence_d)
# print(probability_d)

# COMPROBACIÓN de si la longitud del texto tokenizado sin stopwords y el sumatorio
# de los valores del diccionario es igual:
# print(len(alicia_sin))
# total = sum(ocurrence_d.values())
# print(total)


#HISTOGRAMA: representación del diccionario de probabilidades.
histogram = display_histogram(probability_d)
print(histogram)


