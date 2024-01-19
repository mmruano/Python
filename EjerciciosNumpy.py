import numpy as np

## Ejercicio 1  

# a) Crea un objeto ndarray con números del 0 al 9. El tipo de
# los datos es tipo entero de 32 de bits (int32).

array_int32 = np.arange(10, dtype=np.int32)

# b) Una vez tenemos nuestro ndarray, le cambiamos el tipo a
# float64.

array_float64 = array_int32.astype(np.float64)

# c) Ahora, necesitamos crear un ndarray con todos sus elementos
# igual a 1 del mismo tamaño que el array creado anteriormente.

array_ones = np.ones_like(array_float64)

# d) La última operación es sumar los arrays creados.  

resultado_suma = array_float64 + array_ones

print("Array original (int32):", array_int32)
print("Array convertido a float64:", array_float64)
print("Array de unos:", array_ones)
print("Resultado de la suma:", resultado_suma)

print("\n*******************************")
print("\n")


## Ejercicio 2

# a) Creamos un objeto ndarray con números del 0 al 20. El tipo
# de los datos es tipo float64.

array_float64 = np.arange(21, dtype=np.float64)

# b) Necesitamos aplicar las siguientes funciones unarias a
# nuestro array:

#   - Calcular la raíz cuadrada de cada elemento.
#   - Calcular el cuadrado de cada elemento.
#   - Preguntaremos si los elementos de nuestro array son números
#   o no.

raiz_cuadrada = np.sqrt(array_float64)
cuadrado = np.square(array_float64)
es_numero = np.isnan(array_float64)

# c) Necesitamos aplicar las siguientes funciones binarias a
# nuestro array. Para ello crearemos otro objeto ndarray con sus
# elementos igual a 1 y del mismo tamaño que el anterior:

#   - Sumaremos los elementos de ambos arrays.
#   - Multiplicaremos los elementos de ambos arrays.
#   - Sumaremos uno al array con todos sus elementos igual a 1.  
#   - Elevaremos los elementos del primer array a los elementos
#   de este nuevo array.

array_unos = np.ones_like(array_float64)

suma_elementos = array_float64 + array_unos
producto_elementos = array_float64 * array_unos
suma_uno = array_float64 + 1
elevado_a_uno = np.power(array_float64, array_unos)

print("Array original:", array_float64)
print("\nFunciones unarias:")
print("Raíz cuadrada:", raiz_cuadrada)
print("Cuadrado:", cuadrado)
print("¿Es número?:", es_numero)

print("\nFunciones binarias:")
print("Suma de elementos:", suma_elementos)
print("Producto de elementos:", producto_elementos)
print("Suma uno al array:", suma_uno)
print("Elevado a uno:", elevado_a_uno)

print("\n*******************************")
print("\n")


## Ejercicio 3

# a) Creamos un objeto ndarray con números del 0 al 10. El tipo
# de los datos es tipo float64.

array_float64 = np.arange(11, dtype=np.float64)

# b) Calcularemos la media de los elementos de nuestro array de
# dos maneras:

#   - Usando el método que nos ofrece nuestro array.
#   - Usando el método que nos ofrece la librería numpy.

media_metodo_array = array_float64.mean()
media_metodo_numpy = np.mean(array_float64)

# c) Calcularemos ahora la suma acumulada de todos los elementos
# de nuestro array.

suma_acumulada = np.cumsum(array_float64)

# d) Crearemos a continuación un array con los valores:

values = ['Python', 'R', 'datos', 'R', 'ciencia', 'libreria',
          'Python']

#   - Aplicar una función para eliminar elementos duplicados
#   - Comprobar si los elementos de nuestro array existen en este
#   otro array:

new_values = ['Python', 'R']

unique_values = np.unique(values)

existencia_elementos = np.isin(values, new_values)

print("Array original:", array_float64)
print("\nMedia usando método del array:", media_metodo_array)
print("Media usando método de NumPy:", media_metodo_numpy)
print("Suma acumulada de elementos:", suma_acumulada)

print("\nValores originales:", values)
print("Valores únicos:", unique_values)
print("Existencia en nuevo array:", existencia_elementos)


print("\n*******************************")
print("\n")


## Ejercicio 4

# a) En este ejercicio trabajaremos con las distintas formas de
# indexación que numpy nos ofrece. Comenzamos creando un array
# con elementos del 0 al 8.

array_a = np.arange(9)

# b) Mostraremos el valor del elemento en la posición 3.
# Seguidamente modificaremos los valores desde la posición 4 a la
# 6 con el valor 20.

print("Array original:", array_a)
print("Valor en la posición 3:", array_a[3])
array_a[4:7] = 20

# c) Modificamos nuestro array para que sea una matriz 3 x 3.
# Mostramos los valores accediendo a la segunda fila y hasta la
# segunda columna.

array_matriz = array_a.reshape((3, 3))
print("Matriz 3 x 3:")
print(array_matriz)

print("Array modificado:", array_a)

print("Valores de la segunda fila y hasta la segunda columna:")
print(array_matriz[1, :2])

# d) En este apartado haremos uso del array:

science = np.array(['Python', 'R', 'datos', 'R', 'ciencia', 'libreria',
                    'Python', 'Python', 'R'])  
# Mostramos los valores de nuestro array que en 'values' son
# igual a 'Python'.

# El array a usar debe ser el del apartado a).

science = np.array(['Python', 'R', 'datos', 'R', 'ciencia', 'libreria', 'Python', 'Python', 'R'])
print("\nArray 'science':", science)

print("Valores en 'science' igual a 'Python':")
print(array_a[science == 'Python'])