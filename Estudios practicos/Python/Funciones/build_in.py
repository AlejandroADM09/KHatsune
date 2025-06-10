numeros = {1,2,3,4,5,10,34,5,6,32}

#Encontrando el numero mas grande de una lista

numero_mas_grande = max(numeros)

print(numero_mas_grande)

#Encontrando el numero menor de una lista

numero_mas_pequeño = min(numeros)

print(numero_mas_pequeño)

#Para redondear usamos la funcion round
#numero = round(12.32452452)  print(numero) = 12
#Si le añadimos una coma a nuestra solucion, podemos indicarle el numero de decimales que queremos indicar en la solucion
#numero = round(12.34567890,2)  print(numero) = 12.34

#Retorna False --> 0, vacio, False, None

resultado_bool = bool(1)

print(resultado_bool)

#Retorna True, si todos los valores son verdaderos; Valores iterables | Retorna false si hay un valor = 0, none, vacio, false

resultado_all = all([1,4,True,[]])

print(resultado_all)

#Sumna todos los valores de un iterable

sum_total = sum(numeros)

print(sum_total)

#Devuelve la lista de atributos validos del elemento

print(dir(numeros))

#Devuelve el numero de caracteres en una cadena

print(len(numeros))

#Devuelve el tipo de cadena

print(type(numeros))