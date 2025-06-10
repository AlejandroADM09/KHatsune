import modulo_saludar as saludo #Importamos el modulo y lo llamamos saludar. Podemos tambien modificar el nombre del nombre del modulo que le asignamos con la funcion as.

from modulo_saludar import saludar #Importamos la funcion saludar del modulo. Si queremos añadir mas funciones, las separamos con comas. Tambien podemos añadir todo el modulo con un *.


SALUDAR = saludo.saludar("Alejandro")


print(SALUDAR)


print(saludo.__name__) #Con esto podemos ver el nombre del modulo que hemos importado. En este caso, nos devolvera modulo_saludar.
print(saludo.__file__) #Con esto podemos ver la ruta del modulo que hemos importado. En este caso, nos devolvera la ruta del modulo modulo_saludar.py.





#Enrutamiento de modulos:
#Cuando esta dentro de una carpeta, llamamos a la carpeta de la siguiente manera:
import Modulos.modulo_saludar as saludo #Importamos el modulo si estuviera en la misma carpeta y lo llamamos saludar.
#Si el modulo se encuentra alojado en otra carpeta diferente, lo llamamos de la siguiente manera:
import sys
sys.path.append("C:/Users/andre/OneDrive/Escritorio/Python/Modulos") #Añadimos la ruta del modulo que queremos importar.
import modulo_saludar as saludo #Importamos el modulo y lo llamamos saludar.

#sys es una libreria que nos permite acceder a las variables y funciones del sistema operativo. En este caso, nos permite añadir la ruta del modulo que queremos importar.