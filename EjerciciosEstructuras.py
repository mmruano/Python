# Dada una lista de números, escribe un programa que encuentre
# e imprima el número más grande y el número más pequeño.
# Además, muestra la suma de todos los elementos en la lista.

numbers = [15, 7, 22, 45, 98, 10, 35]

max = max(numbers)
min = min(numbers)
sum = sum(numbers)

print(numbers)
print(f"El número más grande es {max}")
print(f"El número más pequeña es {min}")
print(f"La suma de todos los números es {sum}")

print("\n*******************************")
print("\n")


# Crea un diccionario que represente un libro. El diccionario 
# debe contener información como el título, el autor, el año de
# publicación y el número de páginas.

# Luego, escribe un programa que imprima cada detalle del libro
# en líneas separadas.

book = {
    "title": "The Python Programming Language",
    "author": "Guido van Rossum",
    "year": 2009,
    "pages": 500
}

for x, y in book.items():
    print(f"{x}: {y}")

print("\n*******************************")
print("\n")


# Dadas dos listas, conviértelas en conjuntos y realiza las
# siguientes operaciones:

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

# 1. Encuentra e imprime los elementos comunes en ambos conjuntos.

print(set(list1) & set(list2))

# 2. Encuentra e imprime los elementos que son exclusivos de
# cada conjunto (no comunes).

print(set(list1) ^ set(list2))

print("\n*******************************")
print("\n")


# Dada una lista de listas que representan pares (nombre, edad),
# escribe un programa que encuentre e imprima el nombre y la edad
# de la persona más joven y la persona más vieja.

people = [["Alice", 25], ["Bob", 30], ["Charlie", 22], ["David", 35], ["Eva", 28]]

maxEdad = max(people)
minEdad = min(people)

print(maxEdad)
print(minEdad)

print("\n*******************************")
print("\n")


# Crea un diccionario que almacene información sobre estudiantes
# y sus calificaciones. Luego, escribe un programa que calcule e
# imprima el promedio de calificaciones para cada estudiante.

students = {
    "Alice": [85, 90, 92],
    "Bob": [78, 89, 84],
    "Charlie": [90, 92, 88],
    "David": [85, 79, 92]
}

for x, y in students.items():
    med = students[x] = sum(y) / float(len(y))
    print(f"{x}: {med}")

print("\n*******************************")
print("\n")


# Dada una lista de estudiantes con sus calificaciones, crea un
# diccionario que almacene la información de los estudiantes que
# aprobaron (calificación mayor o igual a 70) en un formato
# {'nombre': 'calificación'}.

# Luego, imprime este diccionario.

aprobados = {nombre: calificacion for nombre, calificacion in students if calificacion >= 70}
print(aprobados)

print("\n*******************************")
print("\n")


# Dados dos conjuntos y una lista, crea una nueva lista que
# contenga elementos que están en la lista pero no en ninguno
# de los conjuntos.

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
my_list = [3, 7, 2, 8, 10]

conjunto_union = set1.union(set2)

nueva_lista = [elemento for elemento in my_list if elemento not in conjunto_union]

print(nueva_lista)

print("\n*******************************")
print("\n")


# Crea una estructura de datos que represente una biblioteca.

# La biblioteca debe contener información sobre libros, autores 
# y la cantidad de copias disponibles.

# Luego, escribe un programa que muestre todos los libros de un
# autor específico y la cantidad total de copias disponibles
# para ese autor.

library = {
    "books": [
        {"title": "Book1", "author": "Author1", "copies": 5},
        {"title": "Book2", "author": "Author2", "copies": 3},
        {"title": "Book3", "author": "Author1", "copies": 8},
        # ... más libros
    ]
}

author_to_search = "Author1"

def books_by_author(books, author_name):
    return [book for book in books if book["author"] == author_name]

def total_copies_by_author(books, author_name):
    return sum(book["copies"] for book in books_by_author(books, author_name))

author_books = books_by_author(library, author_to_search)
if author_books:
    print(f"Libros del autor '{author_to_search}':")
    for book in author_books:
        print(f"Título: {book['title']}, Copias disponibles: {book['copies']}")
    
    total_copies = total_copies_by_author(library, author_to_search)
    print(f"\nCantidad total de copias disponibles para '{author_to_search}': {total_copies}")
else:
    print(f"No se encontraron libros del autor '{author_to_search}' en la biblioteca.")