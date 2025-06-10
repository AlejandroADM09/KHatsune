#creando diccionarios con dic()
diccionario = dict(nombre="lucas",apellido="dalto")


#las listas no pueden ser claves y usamos frozenset

#creando diccionarios con fromkeys(), asigna cada palabra el valor despues de la coma
diccionario = dict.fromkeys ("nombre" , "apellido")

#creando diccionarios com el fromkeys() de valor none
diccionario = dict.fromkeys (["nombre" , "apellido"])

#creando diccionarios com el fromkeys() asignando el valor despues de la coma a los elementos en el corchete

diccionario = dict.fromkeys (["nombre" , "apellido"], "hola guapos")

print(diccionario)