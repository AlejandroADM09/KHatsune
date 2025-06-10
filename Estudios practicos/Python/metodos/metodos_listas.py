#Creando una lista con list()
lista= list(["queso","leche","pan"])


#Devuelve el numero de elementos en la lista
resultado = len(lista)

#agragando un elemento a la lista con .append()

lista.append("pescado")

#agragando un elemento a la lista en un indice especifico

lista.insert(2,"harina")

#agragando varios elementos a la lista

lista.extend(["jamon","atun","cebollas"])

#Eliminando un elemento de la lista por su indice

"lista.pop(x)"

#Eliminando un elemento de la lista por su valor

"lista.remove(jamon)"

#Eliminando todos los elementos de la lista

"lista.clear()"

#Revierte el orden de la lista

"lista.reverse()"

#Verificando si un elemento esta en la lista y en que posición se encuentra

entorando_objeto = lista.index("jamon")



print(entorando_objeto)