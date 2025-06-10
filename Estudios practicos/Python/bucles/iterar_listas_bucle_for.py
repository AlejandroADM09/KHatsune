#Esto tambien se puede aplicar a tuplas y conjuntos

lista = ["gato","perro","cocodrilo","loro","pez"]
numeros = [1,2,3,4,5]
cadena= "hola master"

#Recorriendo la lista animales
for animal in lista:
    print(f"Ahora el animal va a ser {animal}")

#Recorriendo la lista numeros y multiplicandolos por 10
for numero in numeros:
    resultado = numero * 10
    print(resultado)

#Podemos recorrer dos lista o jugar con ellas con el comando zip() | Si las listas no tienen la misma longitud, el valor restante no se muestra
for numero,animal in zip(lista,numeros):
    print (f"asignando un numero a un animal: {animal}:{numero}")

#Con range() nos da el numero de valores que le indicamos ej: si le dimos range(10,20), nos da valores del 10 al 19, no del 11-20 o 10-20|ej range(10)= 0,1,2,3..9
#enumera de manera ascendente, no descendente
for num in range(0,10):
    print(num)

#Forma optima para recorrer una lista con su indice
for num in enumerate(numeros):
    print(num)

#Forma optima y bonita para recorrer una lista con su indice
for num in enumerate(lista):
    indice = num[0]
    valor = num[1]
    print(f"el indice es: {indice} y el animal es: {valor}")


#si le agragamos el parametro else, siempre se ejecutara a pesar de que el for no funcione
for num in enumerate(lista):
    indice = num[0]
    valor = num[1]
    print(f"el indice es: {indice} y el animal es: {valor}")
else:
    print ("se termnino el bucle master")


#Saltar elementos de una lista
for animal in lista:
    if animal == "cocodrilo":
        continue
    print(f"me gusta mucho el {animal}")


#terminar el bucle (los else los salta tambien, por eso no lo ponemos)
for animal in lista:
    print(f"me gusta mucho el {animal}")
    if animal == "perro":
        break
    
print("es mi animal favorito")

#recorrer cada elemento de una cadena
for letra in cadena:
    print(letra)

#for en una sola linea de codigo
multiplicando_numeros = [x+3 for x in numeros]


print(multiplicando_numeros)