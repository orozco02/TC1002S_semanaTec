import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Cargar los datos
data = pd.read_csv('Financial Sample.csv')

# Eliminar símbolos de moneda 
data['Manufacturing Price'] = data['Manufacturing Price'].str.replace('[\$,]', '', regex=True).astype(float)
data['Sale Price'] = data['Sale Price'].str.replace('[\$,]', '', regex=True).astype(float)

model = LinearRegression()

X = data[['Manufacturing Price']]
Y = data['Units Sold']

# Ajustar el modelo lineal a los datos
model.fit(X, Y)

# Realizar predicciones del modelo
Y_pred = model.predict(X)

# Graficar los datos y la línea de regresión
plt.scatter(X, Y, label='Datos reales')
plt.plot(X, Y_pred, color='red', label='Regresión lineal')
plt.xlabel('Manufacturing Price')
plt.ylabel('Units Sold')
plt.legend()
plt.show()

data = data.drop(['Year', 'Month Name'], axis=1)

from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

#clustering
X = data[['Units Sold', 'Sale Price']]

for k in range(2, 11):
    kmeans = KMeans(n_clusters=k, random_state=0)
    kmeans.fit(X)
    inertia = kmeans.inertia_
    silhouette_avg = silhouette_score(X, kmeans.labels_)
    print(f'k={k}, Inercia: {inertia}, Coeficiente de silueta: {silhouette_avg}')

kmeans = KMeans(n_clusters=5, random_state=0)  # Ajusta el valor de k
kmeans.fit(X)
centros = kmeans.cluster_centers_
print("Centros de los clusters:")
print(centros)
