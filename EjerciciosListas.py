### Ejercicios


## Ejercicio 1

# Realizar un programa que inicialice una lista con 10 valores
# aleatorios (del 1 al 10) y posteriormente muestre en pantalla
# cada elemento de la lista junto con su cuadrado y su cubo.

import random

listNumRandom = []

for i in range(10):
    n = random.randint(1, 10)
    listNumRandom.append(n)

for n in listNumRandom:
    cuadrado = n ** 2
    cubo = n ** 3
    print(f"{n}, {n}^2 = {cuadrado}, {n}^3 = {cubo}")

print("\n*******************************")
print("\n")


## Ejercicio 2

# Crea una lista e inicializala con 5 cadenas de caracteres leídas
# por teclado. Copia los elementos de la lista en otra lista pero
# en orden inverso, y muestra sus elementos por la pantalla.

listChar = []

for i in range(5):
    caracter = str(input(f"Escribe el {i + 1}º caractér: "))
    listChar.append(caracter)

listCharReverso = listChar[::-1]

print(listCharReverso)

print("\n*******************************")
print("\n")


## Ejercicio 3

# Se quiere realizar un programa que lea por teclado las 5 notas
# obtenidas por un alumno (comprendidas entre 0 y 10).
# A continuación debe mostrar todas las notas, la nota media,
# la nota más alta que ha sacado y la menor.

notas = []

for i in range(5):
    nota = float(input(f"Introduce la nota {i + 1}: "))
    notas.append(nota)

for i, nota in enumerate(notas, start=1):
    print(f"Nota {i + 1}: {nota}")

ave = sum(notas) / len(notas)
max = max(notas)
min = min(notas)

print(f"Nota media: {ave:.2f}")
print(f"Nota más alta: {max}")
print(f"Nota más baja: {min}")

print("\n*******************************")
print("\n")


## Ejercicio 4

# Programa que declare una lista y la vaya llenando de números
# hasta que introduzcamos un número negativo. Entonces se debe
# imprimir el vector (sólo los elementos introducidos).

listNum = []

while True:
    num = int(input("Introduce un número (ingresa un número negativo para terminar): "))

    if num < 0:
        break;
    else:
        listNum.append(num)

print("Lista de números ingresados:", listNum)

print("\n*******************************")
print("\n")


## Ejercicio 5

# Hacer un programa que inicialice una lista de números con
# valores aleatorios (10 valores), y posterior ordene los
# elementos de menor a mayor.

listNumOrdenado = []

for i in range(10):
    n = random.randint(1, 10)
    listNumOrdenado.append(n)

listNumOrdenado.sort

print(listNumOrdenado)

print("\n*******************************")
print("\n")


## Ejercicio 6

# Crea un programa que pida un número al usuario un número de
# mes (por ejemplo, el 4) y diga cuántos días tiene (por ejemplo,
# 30) y el nombre del mes. Debes usar listas. Para simplificarlo
# vamos a suponer que febrero tiene 28 días.

listNumMes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

listNombreMes = ["Error", "Enero", "Febrero", "Marzo", "Abril", "Mayo",
                 "Junio", "Julio", "Agosto", "Septiembre",
                 "Octubre", "Noviembre", "Diciembre"]

n = int(input("Introduce un número del mes: "))

if 1 <= n <= 12:
    dias = listNumMes[n]
    nombreMes = listNombreMes[n]
    print(f"El mes de {nombreMes} tiene {dias} dias.")
else:
    print("Error, el número tiene que ser entre el 1 y el 12.")

print("\n*******************************")
print("\n")


## Ejercicio 7

# Programa que declare tres listas ‘lista1’, ‘lista2’ y ‘lista3’
# de cinco enteros cada uno, pida valores para ‘lista1’ y ‘lista2’
# y calcule lista3=lista1+lista2.

lista1 = []
lista2 = []
lista3 = []

for i in range (5):
    n = int(input(f"Rellena el {i + 1}º de la primera lista: "))
    lista1.append(n)

for i in range (5):
    n =  int(input(f"Rellena el {i + 1}º de la segunda lista: "))
    lista2.append(n)

for i in range(5):
    suma = lista1[i] + lista2[i]
    lista3.append(suma)

print(f"Lista 1: {lista1}")
print(f"Lista 2: {lista2}")
print(f"Lista 3: {lista3}")

print("\n*******************************")
print("\n")


## Ejercicio 8

# Diseñar el algoritmo correspondiente a un programa, que:

# Crea una tabla bidimensional de longitud 5x15 y nombre ‘marco’.
# Carga la tabla con dos únicos valores 0 y 1, donde el valor
# uno ocupará las posiciones o elementos que delimitan la tabla,
# es decir, las más externas, mientras que el resto de los
# elementos contendrán el valor 0.

#  111111111111111  
#  100000000000001  
#  100000000000001  
#  100000000000001  
#  111111111111111  

# Visualiza el contenido de la matriz en pantalla.

marco = [[0 for _ in range(15)] for _ in range(5)]

for fila in range (5):
    for columna in range (15):
        if fila == 0 or fila == 4 or columna == 0 or columna == 14:
            marco[fila][columna] = 1

for fila in marco:
    print(fila)

print("\n*******************************")
print("\n")


## Ejercicio 9

# Crear un programa que añada números a una lista hasta que
# introducimos un número negativo. A continuación debe crear
# una nueva lista igual que la anterior pero eliminando los
# números duplicados. Muestra esta segunda lista para comprobar
# que hemos eliminados los duplicados.

listNum = []

while True:
    num = int(input("Introduce un número (ingresa un número negativo para terminar): "))

    if num < 0:
        break;
    else:
        listNum.append(num)

listNumSinDuplicados = list(set(listNum))

print("Lista de números ingresados:", listNum)
print("Lista de números ingresados sin duplicados:", listNumSinDuplicados)

print("\n*******************************")
print("\n")


## Ejercicio 10

# Escriba un programa que permita crear una lista de palabras
# y que, a continuación de tres opciones:

# Contar: Me pide una cadena, y me dice cuantas veces aparece
# en la lista

# Modificar: Me pide una cadena, y otra cadena a modificar, y
# modifica todas las apariciones de la primera por la segunda
# en la lista.

# Eliminar: Me pide una cadena, y la elimina de la lista.

# Mostrar: Muestra la lista de cadenas

# Terminar

while(True):
    listPalabras = []
    palabra = input(str("Introduce una palabra: "))

    if palabra == int:
        break;
    else:
        listPalabras.append(palabra)

while(True):
    print("Elige una opción:")

    print("\nContar: Me pide una cadena, y me dice cuantas veces aparece en la lista")
    print("\nModificar: Me pide una cadena, y otra cadena a modificar, y modifica todas las apariciones de la primera por la segunda en la lista.")
    print("\nEliminar: Me pide una cadena, y la elimina de la lista.")
    print("\nMostrar: Muestra la lista de cadenas.")
    print("\nTerminar")

    op = input(str(""))
    
    if(op == "Contar"):
        cadena = input(str("Qué cadena quieres contar?: "))
        print(listPalabras.count(cadena))

    if(op == "Modificar"):
        cadena = input(str("Qué cadena quieres modificar?: "))
        cadena2 = input(str("Con que cadena quieres reemplazarlo?: "))
        reemplazar = listPalabras.index(cadena)
        listPalabras[reemplazar] = cadena2

    if(op == "Eliminar"):
        cadena = input(str("Qué cadena quieres eliminar?: "))
        listPalabras.remove(cadena)

    if(op == "Mostrar"):
        print(listPalabras)

    if(op == "Terminar"):
        break;