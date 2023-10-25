import pandas as pd

#Cargar el CSV

datos=pd.read_csv('peso_estatura_genero.csv')

#Cantidad de datos
print("Cantidad de datos:", len(datos))
print("primeras filas:")
print(datos.head())

#Analisis estadístico
estadisticas=datos.describe()
print(estadisticas)
