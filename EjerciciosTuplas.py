## Ejercicio1

# Escribe un programa que lea una cadena y devuelva un
# diccionario con la cantidad de apariciones de cada carácter
# en la cadena.

dict = {}
cadena = input("Dame una cadena:")
for caracter in cadena:
	if caracter in dict:
		dict[caracter]+=1
	else:
		dict[caracter]=1	

for campo,valor in dict.items():
	print (campo,"->",valor)

print("\n*******************************")
print("\n")


## Ejercicio2

# Vamos a crear un programa en python donde vamos a declarar un
# diccionario para guardar  los precios de las distintas frutas.

# El programa pedirá el nombre de la fruta  y la cantidad que se
# ha vendido y nos mostrará el precio final de la fruta a partir 
# de los datos guardados en el diccionario.

# Si la fruta no existe nos dará un error. Tras cada consulta
# el programa nos preguntará si queremos hacer otra consulta.

precios = {"manzana": 2, "naranja": 1.5, "platano": 4, "piña": 3}
while True:
    fruta = input("Dime la fruta que has vendido:")
    if fruta.lower() not in precios:
        print("Fruta no existe.")
    else:
        cantidad = int(input("Dime la cantidad de frutas que has vendido:"))
        print("El precio es de %f" % (cantidad * precios[fruta]))
    opcion = input("¿Quieres vender otra fruta (s/n)")
    while opcion.lower() != "s" and opcion.lower() != "n":
        opcion = input("¿Quieres vender otra fruta (s/n)")
    if opcion.lower() == "n":
        break