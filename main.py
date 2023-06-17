from alice_utils import *

# ___________________Alice in Wonderland__________________________

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
#print(probability_d)

# COMPROBACIÓN de si la longitud del texto tokenizado sin stopwords y el sumatorio
# de los valores del diccionario es igual:
# print(len(alicia_sin))
# total = sum(ocurrence_d.values())
# print(total)


#HISTOGRAMA: representación del diccionario de probabilidades.
print("Probabilidades:  ____________________________________________________________________________")
display_histogram(probability_d)
print("__________________________________________________________________________________________")



