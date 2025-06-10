import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



df = pd.read_csv('Archivos_graficos\\beber_agua.csv')


#creando un grafico lineal
sns.lineplot(x="fecha", y="vasos de agua", data=df)

#creando un grafico de barras
sns.barplot(x="fecha", y="vasos de agua", data=df)

#creando un grafico de dispersion
sns.scatterplot(x="fecha", y="vasos de agua", data=df)

#creando un grafico de dispersion
sns.boxplot(x="fecha", y="vasos de agua", data=df)

#Colocamnos un punto en el grafico lineal
plt.plot("2023-01-09",5, "o")


#Creamos el grafico
plt.show()