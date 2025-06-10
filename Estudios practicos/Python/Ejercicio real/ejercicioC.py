#Creando una sucesion de fibonachi 

#sucesion
#Suma el numero anterior a la suma
#Parara cuando el valor sea igual o inferior
#Mostrar en una lista la serie de numeros usada hasta el valor que queremos



# Creando una sucesión de Fibonacci

# Inicializamos la lista con los dos primeros números de Fibonacci


# Generamos los siguientes números de la secuencia hasta un límite
def sumatorio_fibonachi(num):
    fibonacci = [0,1]
    for i in range(num):  # Generar 8 números adicionales
        siguiente = fibonacci[-1] + fibonacci[-2]  # Suma de los dos últimos números
        fibonacci.append(siguiente)
    return fibonacci

def sumatorio_final_fibonachi(num):
    Listado = []
    for i in range(num):
        resultado = sumatorio_fibonachi(i)
        if resultado[-1] <= num: Listado.append(resultado)
    return Listado


# Imprimimos la lista completa
print(sumatorio_final_fibonachi(100))




