cadena1 = "Hola Mundo, esto es una prueba que quiero realizar con los metodos de cadena"
cadena2 = "184120946123641096036394653945639261065"
cadena3 = "sfjhbasiohgfabiorfbaierbfgiwerbgiesbibsdbisdbviheb"
cadena4 = "hola"


#Convierte todo a mayuscula

mayusculas = cadena1.upper()

#Convierte todo a minuscula

minusculas = cadena1.lower()

#La primera con mayusculas

primera_con_mayusculas = cadena1.capitalize()

#Busca y retorna la posicion del objeto que buscamos; El error que lanza si no lo encuentra es (-1)

find = cadena1.find("Mundo")

#Busca y retorna la posicion del objeto que buscamos; El error que lanza si no lo encuentra es una excepcion

index = cadena1.index("Hola")

#Verifica si es un texto con solo numeros

isnumeric = cadena2.isnumeric()

#Verifica si es un texto alfanumerico, solo letras sin espacios

isalfa = cadena3.isalpha()

#Nos cuenta las veces que se encuentra el valor indicado en la cadena

contar = cadena1.count("a")

#Verifica que la cadena empiece por el valor que le indicamos 

verificacion = cadena1.startswith("Hola")

#Verifica que la cadena etermine por el valor que le indicamos

verificacion2 = cadena1.endswith("cadena")

#Remplaza el valor de la cadena original por otro valor

replace = cadena1.replace("a","e")

#Separa la cadena creando una lista segun el elemento que elijamos

separar = cadena1.split(" ")

print(separar)

