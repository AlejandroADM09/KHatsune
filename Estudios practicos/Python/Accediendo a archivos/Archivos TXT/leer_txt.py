#fichero_prueba = open("Python\\Accediendo a archivos\\Archivos TXT\\texto_de_prueba.txt", encoding="UTF-8")


#Abre el archivo sin leerlo
#fichero = fichero_prueba


#Leemos el contenido del archivo y lo guardamos en la variable fichero.
#fichero = fichero_prueba.read() 


#Leemos el fichero linea por linea
#fichero = fichero_prueba.readlines()

#Lee el numero de caracteres que le digamos hasta el salto de linea del la primera linea
#fichero = fichero_prueba.readline(x) 


#cerramos el archivo
#fichero_prueba.close()



#Forma optima de abrir archivos.txt

with open("Python\\Accediendo a archivos\\Archivos TXT\\texto_de_prueba.txt", encoding="UTF-8") as fichero_prueba:
    print(fichero_prueba.read()) #Leemos el contenido del archivo y lo guardamos en la variable fichero.


#No es necesario cerrar el archivo, ya que el bloque with se encarga de ello automáticamente.
