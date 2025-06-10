#Pedir un listado a una clase y ordenar los datos segun las edades de los alumnos


def obterner_compañeros(cantidad_de_compañeros):
    listados = []
    for i in range(cantidad_de_compañeros):
        nombre = input("Nombre del alumno: ") 
        edad = int(input ("Edad del alumno: "))
        listado = (nombre,edad)
        listados.append(listado)
    listados.sort(key=lambda x:x[1])
    asistente = listados[0][0]
    profesor = listados[-1][0]
    return asistente,profesor


asistente,profesor = obterner_compañeros(3)
    
    
   


print(f"El profesor de la clase es {profesor} y su asistente es {asistente}.")

