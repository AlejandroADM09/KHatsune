with open("Python\\Accediendo a archivos\\Archivos TXT\\texto_de_prueba.txt",'w', encoding="UTF-8") as fichero_prueba:
    fichero_prueba.write("Soy la segunda linea del texto de prueba.\n")
    fichero_prueba.writelines("Soy la tercera linea del texto de prueba.\n")
    fichero_prueba.write("Soy la cuarta linea del texto de prueba.\n")
    fichero_prueba.write("Soy la quinta linea del texto de prueba.\n")
#siempre sobreescribe el archivo, no lo modifica.


with open("Python\\Accediendo a archivos\\Archivos TXT\\texto_de_prueba.txt",'a', encoding="UTF-8") as fichero_prueba:
    fichero_prueba.write("Soy la sesta linea del texto de prueba.\n")
    fichero_prueba.writelines("Soy la setima linea del texto de prueba.\n")
    fichero_prueba.write("Soy la octava linea del texto de prueba.\n")
    fichero_prueba.write("Soy la novena linea del texto de prueba.\n")
#siempre modifica añadiendo el contenido.