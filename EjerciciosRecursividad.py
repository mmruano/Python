## Ejercicio 1: Factorial de un Número:

# Desarrolla una función recursiva para calcular el factorial
# de un número entero positivo n.

# Ejemplo: 5! = 5 * 4 * 3 * 2 * 1 = 120.

def factorial(n):
    r = 1
    i = 2
    while i <= n:
        r *= i
        i += 1

print("\n*******************************")
print("\n")


## Ejercicio 2: Implementa una función recursiva para calcular
# la suma de los primeros n números naturales.

# Ejemplo: sumaNaturales(3) = 1 + 2 + 3 = 6.

def sumaNaturales(n):
    r = 1
    i = 2
    while i <= n:
        r += i
        i += 1

print("\n*******************************")
print("\n")


## Ejercicio 3: Fibonacci:

# Crea una función recursiva para calcular el término n de la
# secuencia de Fibonacci.

# Ejemplo: fibonacci(5) = 3 (la secuencia comienza con
# 0, 1, 1, 2, 3).

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
print("\n*******************************")
print("\n")


## Ejercicio 4: Torres de Hanoi:

# Resuelve el problema de las Torres de Hanoi utilizando una
# función recursiva. Dado un número de discos n, mueve los discos
# de un poste a otro siguiendo las reglas del juego.

# Las Torres de Hanoi es un famoso problema matemático y de
# lógica que implica mover una torre de discos de un poste a
# otro, siguiendo ciertas reglas. La torre consta de tres postes
# (A, B, y C) y varios discos de diferentes tamaños, colocados
# uno sobre otro en orden decreciente de tamaño en el poste A.

# Reglas del Problema:  

# Solo puedes mover un disco a la vez.
# Solo puedes mover el disco superior de cada poste.
# No se puede colocar un disco más grande sobre uno más pequeño.

# Objetivo:
# El objetivo es mover la torre completa de discos desde el
# poste A al poste C, utilizando el poste B como auxiliar.

def moverTorre(altura,origen, destino, intermedio):
    if altura >= 1:
        moverTorre(altura-1,origen,intermedio,destino)
        moverDisco(origen,destino)
        moverTorre(altura-1,intermedio,destino,origen)

def moverDisco(desde,hacia):
    print("mover disco de",desde,"a",hacia)

moverTorre(3,"A","B","C")

print("\n*******************************")
print("\n")


## Ejercicio 5: Potencia de un Número:

# Escribe una función recursiva para calcular a elevado a la
# potencia b.

# Ejemplo: potencia(2, 3) = 2^3 = 8.