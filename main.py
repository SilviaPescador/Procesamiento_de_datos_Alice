from alice_utils import *

# ___________________Alice in Wonderland__________________________

# NORMALIZO Y TOKENIZO TEXTO ALICE Y STOPWORDS
clean_alice = normalize_tokenize(lines)
clean_stopw = normalize_tokenize(contents)

# PASO STOPWORDS A SET
stopwords_set = set(clean_stopw)

# ELIMINO STOPWORDS DE ALICIA
alicia_sin = remove_stopwords(clean_alice, stopwords_set)

# CREO DICCIONARIO: CLAVE-palabras//VALOR-nº ocurrencia de la palabra.
ocurrence_d = count_words(alicia_sin)

# DICCIONARIO: CLAVE-palabras //VALOR-probabilidad ocurrencia.
probability_d = word_probability(ocurrence_d)

# COMPROBACIÓN de si la longitud del texto tokenizado sin stopwords y el sumatorio
# de los valores del diccionario es igual:
print("Nº de palabras en Alice in Wonderland: ", len(alicia_sin))
total = sum(ocurrence_d.values())
print("Nº de palabras sin stopwords: ", total)

# DICCIONARIO ORDENADO POR PROBABILIDAD DE OCURRENCIAS
sorted_word_probability = sorted_word_probability(probability_d)

# HISTOGRAMA: representación del diccionario de probabilidades ordenadas por frecuencia.
print("________________________________________________________________\n")
print("HISTOGRAMA: ")
print("Ocurrencia de palabras en Alice in Wonderland.")
print("________________________________________________________________\n")
display_histogram(sorted_word_probability)



