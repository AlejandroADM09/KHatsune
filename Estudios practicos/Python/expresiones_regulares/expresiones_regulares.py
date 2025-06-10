import re

texto = '''Hola, este es un mensaje que usaremos a modo de ejemplo para el ejercicio que nos plantean.
Usaremos varias linea a modo de que podamos tener un texto largo y cuadriculado 9.
Jajajjaajja que boludos somos poniendo tanto texto 978.'''

#hay un parametro extrase que se llam a flags que añade funcionalidades a la busqueda

#resultado = re.search("Hola",texto) #busca la palabra Hola en el texto y devuelve un objeto Match
#resultado = re.findall("que",texto) #busca todas las palabras que en el texto y devuelve una lista


#\d busca numeros del 0 al 9 |#\D busca todo lo que no sea un numero del 0 al 9
#resultado = re.findall(r"\d", texto) 


#\w busca caracteres alfanumericos|#\W busca todo lo que no sea un caracter alfanumerico
#resultado = re.findall(r"\W", texto) 


#\s busca espacios, saltos de linea, tabs |#\S busca todo lo que no sea espacios, saltos de linea, tabs
#resultado = re.findall(r"\s", texto) 


#. busca todo menos saltos de linea
#resultado = re.findall(r".", texto) 


#\n busca saltos de linea
#resultado = re.findall(r"\n", texto)


#\  cancela caracteres especiales
#resultado = re.findall(r"\.", texto)  #busca el punto al final de la frase


#armando una cadena que busque un numero, seguido de un punto y un espacio
#resultado = re.findall(r'\d\.\s', texto)


#^ comprueba si el texto empieza con lo que le pasamos. Si no añadimos el parametro flags=re.MULTILINE, no contara con las lineas nuevas tras el salto de linea
#resultado = re.findall(r"^Hola", texto)


#$ comprueba si el texto termina con lo que le pasamos. Si no añadimos el parametro flags=re.MULTILINE, no contara con las lineas nuevas tras el salto de linea
#resultado = re.findall(r"\.$", texto)


#{n} busca n veces seguido el caracter que le pasamos | {n,m}  al menos n y como maximo m veces
#resultado = re.findall(r"\d{1}", texto)
#resultado = re.findall(r"\d{1,3}", texto)


# | busca una u otra cosa, como un OR
resultado = re.findall(r"\d{1,3}|mensaje", texto)

print(resultado)