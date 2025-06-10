import pandas as pd

df = pd.read_csv("Accediendo a archivos/Archivos CSV/datos.csv") #Leemos el contenido del acsv y lo guardamos en la variable df (dataframe).
df2 = pd.read_csv("Accediendo a archivos/Archivos CSV/datos.csv")

#print(df) #Imprimimos el contenido del archivo.
#print(df["nombre"]) #Imprimimos el contenido de la columna nombre.
#print(df["nombre"][0]) #Imprimimos el contenido de la columna nombre y la fila 0.


#Ordenador el dataframe de forma ordenada por edad
df_ordenado = df.sort_values(by= "edad") #Ordenamos el dataframe por la columna edad.


#Ordenador el dataframe de forma ordenada por edad invertida
df_ordenado_invertido = df.sort_values(by= "edad", ascending=False) #Ordenamos el dataframe por la columna edad de manera invertida.

#accedinedo a las primer fila con head()
df_head = df.head(1) #Accedemos a la primer fila del dataframe.

#accedinedo a las ultimas filas con tail()
df_tail = df.tail(3) #Accedemos a la ultima fila del dataframe.

#Concatenando dataframes
df_concatenando = pd.concat([df,df2])

#Sacando la cantidad de filas por columnas que tiene el dataframe
df_shape = df.shape #Sacamos la cantidad de filas y columnas que tiene el dataframe.
#desempaquetamos la variable para poder obtener la cantidad de filas y columnas por separado
filas, columnas = df_shape #Desempaquetamos la variable df_shape para poder obtener la cantidad de filas y columnas por separado.


#accediendo al dato especifico de la fila a traves de loc
df_loc = df.loc[4, "nombre"] #Accedemos al dato especifico de la fila 3 y la columna apellido.
df_loc2 = df.loc[:, "nombre"] #Accedemos a todos los datos de la columna nombre.
df_loc3 = df.loc[2, :] #Accedemos a todos los datos de la fila 2.

#accediendo al dato especifico de la fila a traves de iloc
df_iloc = df.iloc[4, 1] #Accedemos al dato especifico de la fila 4 y columna 1.
df_iloc2 = df.iloc[:, 1] #Accedemos a todos los datos de la columna 1.
df_iloc3 = df.iloc[2, :] #Accedemos a todos los datos de la fila 2.

#Reemplazamos el apellido Gomez por Navarro en el dataframe.
df['apellido'].replace('Gomez', 'Navarro', inplace=True) 

#Eliminamos las filas que tienen valores nulos.
df = df.dropna() 

#Eliminamos las filas duplicadas.
df = df.drop_duplicates() 

#Guardamos el dataframe modificado en un nuevo archivo csv.
df.to_csv("Accediendo a archivos/Archivos CSV/datos_modificados.csv") 


print(df_loc3)


