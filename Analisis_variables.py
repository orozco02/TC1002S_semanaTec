import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Cargar los datos
data = pd.read_csv('Financial Sample.csv')

# Boxplot 
sns.boxplot(data=data[['Units Sold', 'Manufacturing Price', 'Sale Price']])
plt.title('Boxplot de Units Sold, Manufacturing Price y Sale Price')
plt.show()

# Histograma de Units Sold
data['Units Sold'].hist()
plt.title('Histograma de Units Sold')
plt.xlabel('Units Sold')
plt.ylabel('Frecuencia')
plt.show()

# Histograma de Manufacturing Price
data['Manufacturing Price'].hist()
plt.title('Histograma de Manufacturing Price')
plt.xlabel('Manufacturing Price')
plt.ylabel('Frecuencia')
plt.show()

# Histograma de Sale Price
data['Sale Price'].hist()
plt.title('Histograma de Sale Price')
plt.xlabel('Sale Price')
plt.ylabel('Frecuencia')
plt.show()

# Mapa de calor
data['Manufacturing Price'] = data['Manufacturing Price'].str.replace('$', '').astype(float)
data['Sale Price'] = data['Sale Price'].str.replace('$', '').astype(float)
correlation = data[['Units Sold', 'Manufacturing Price', 'Sale Price']].corr()
sns.heatmap(correlation, annot=True)
plt.title('Mapa de calor de correlación')
plt.show()

#Clustering
data['Sale Price'] = data['Sale Price'].str.replace('[\$,]', '', regex=True).astype(float)
data_subset = data[['Sale Price', 'Units Sold']]
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
data_normalized = scaler.fit_transform(data_subset)
kmeans = KMeans(n_clusters=3, random_state=0)
data['Cluster'] = kmeans.fit_predict(data_normalized)
plt.scatter(data['Sale Price'], data['Units Sold'], c=data['Cluster'])
plt.title('Grupos de Productos')
plt.xlabel('Precio de Venta')
plt.ylabel('Unidades Vendidas')
plt.show()

#Diagrama de dispersión
plt.scatter(data['Units Sold'], data['Manufacturing Price'])
plt.title('Diagrama de dispersión entre Units Sold y Manufacturing Price')
plt.xlabel('Units Sold')
plt.ylabel('Manufacturing Price')
plt.show()
