# Práctica de Procesamiento de Datos


## Pre-requisitos

Averigua qué es Kaggle.com y créate una cuenta. Si vas para Big Data, además, elige alguno de los cursillos que ofrecen y ponte fecha para hacerlo. Buenas opciones son Pandas (lo vas a ver más adelante, pero no está de más repasar) o Deep Learning.


Dentro de los datasets (¿qué es un dataset?), localiza uno de “stopwords” en Inglés. Las “stopwords” son aquellas palabras “paja” que no aportan gran cosa a una frase. Descarga el fichero y guárdalo en tu disco duro.


Averigua qué es el Proyecto Gutenberg y descarga el texto completo de Alicia en el País de las Maravillas. Guárdalo en tu disco duro, en la misma carpeta que el de las stopwords.


## Lectura de Ficheros de Texto

Averigua cómo se abre un fichero de texto en Python y lee el contenido de esos dos a sendas variables (cadenas).

Asegúrate de que consigues leer correctamente los dos ficheros.


## Tokenización

Se llama tokenización, el romper una cadena en una lista de subcadenas, cada una de ellas conteniendo una palabra. A esos trocitos de texto (palabras) se les llama tokens. Mírate estas instrucciones y tokeniza los dos textos usando split() o NLTK (si hay huevos).


## Sets

Crea un set a partir de la lista (tokenizada) de los stopwords:

stopwords_set = set(list_of_stopwords)

Crea un función llamada 
### remove_stopwords
que acepta una lista de cadenas, y un set de stopwords y que devuelve una nueva lista con todas las stopwords eliminadas. 
¿Te acuerdas de tu función filter?


## Normalización

Cuando recibes datos que no han sido procesados previamente para consumo del ordenador, es probable que tengas diferentes representaciones para lo mismo. En el caso de palabras, es posible que tengas las siguientes representaciones para la misma palabra here.

* Here
* HERE
* here’s
* heRe
* here,
* here.
* etc….

El proceso de normalización consiste en transformar todas esas versiones en una sola
Crea las siguientes funciones que procesan una sola palabra:

### remove_punctuation

Recibe una cadena, y si esta termina en algún símbolo de puntuación (,.;) devuelve la cadena sin dicho símbolo.
remove_punctuation(“hola”) → “hola”
remove_punctuation(‘hola.”) → “hola”

### remove_apostrophe

Recibe una cadena, y si termina en ‘s, devuelve una cadena sin ese final.

remove_apostrophe(‘Hola’) → ‘Hola’
remove_apostrophe(“here’s”) → ‘here’

### remove_suffix

En el fondo, esas dos funciones son casos especiales de una función que elimina (en caso de existir) un cierto sufijo en una cadena.
Escribe la función remove_suffix.

### normalize

Usando las funciones que acabas de crear así como el map de Python, escribe la función normalize que recibe una lista de cadenas y devuelve una nueva lista de cadenas, con cada elemento transformado de la siguiente forma:

* los sufijos indeseables son eliminados
* las cadenas son convertidas a minúsculas

Con esto, podrás obtener una lista de palabras, sin stopwords, y normalizadas del texto de Alicia.

## Dicts

Un Diccionario (llamado también map en algunos lenguajes) es un Set de dos objetos: una clave y un valor.
Repasa, si necesitas, un poco los dicts de Python.


### count_words

Crea la función count_words que recibe una lista de palabras y devuelve un dict en el cual cada palabra es una clave y el valor asociado es la cantidad de veces que aparece en la lista original.

Para ello, tendrás que recorrer la lista de palabras normalizadas y por cada una de ellas:
* Comprobar si esa palabra ya está en el diccionario
* Si lo está, incrementa su valor (el contado) en una unidad
* Si no lo está, métela con el valor de 1


### word_probability

Crea la función word_probability que recibe el dict resultante de la anterior y lo itera cambiando el valor de cada elemento por el valor dividido por el número total de elementos.

El número total de elementos (palabras en el dict) se obtiene con len. Al dividir cada cantidad por el total, se obtiene la probabilidad de cada palabra.
Un diccionario de palabra y su probabilidad, es un histograma.
Estás procesando un dict cambiando cada uno de los elementos. Eso suena a map. Averigua si se puede hacer con el map de Python.


### display_histogram

Crea la función display_histogram que imprime en cada línea una palabra, seguida por un número de # que indica su probabilidad.

Una palabra cuya probabilidad fuese del 100%, se representaría con 50 # seguidos.
Una palabra cuya probabilidad fuese del 0%, se representaría con 0 #.