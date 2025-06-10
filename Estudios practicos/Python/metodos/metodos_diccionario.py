diccionario = {
    "nombre" : "Alejandro",
    "edad" : "20 años",
    "fecha de nacimiento" : "23/07/2024"
}


#Nos devuelve las claves del diccionario y tambien nos sirve para iterar

"claves = diccionario.keys()"

#Nos devuelve el valor de la clave que le indiquemos

claves = diccionario.get("nombre")

#Elimina todo del diccionario

"diccionario.clear()"

#Elimina un elemento de un diccionario

"diccionario.pop(nombre)"

#Obteniendo un elemento dic_items iterable

diccionario_iterable = diccionario.items()


print (diccionario_iterable)