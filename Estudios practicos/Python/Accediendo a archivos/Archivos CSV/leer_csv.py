
import csv #Importamos la libreria csv para poder leer archivos csv


#with open("Accediendo a archivos\\Archivos CSV\\datos.csv") as fichero_prueba:
    #print(fichero_prueba.read()) #Leemos el contenido del archivo y lo guardamos en la variable fichero. Forma no optima
    #print(csv.reader(fichero_prueba)) #Leemos el contenido del archivo y lo guardamos en la variable fichero. Forma optima


with open("Accediendo a archivos\\Archivos CSV\\datos.csv") as fichero_prueba:
    reader = csv.reader(fichero_prueba) #Leemos el contenido del archivo y lo guardamos en la variable fichero.
    for row in reader: #Recorremos el contenido del archivo y lo guardamos en la variable fichero.
        print(row) #Imprimimos el contenido del archivo. Agregando un [] podemos indicar que fila queremos imprimir.
