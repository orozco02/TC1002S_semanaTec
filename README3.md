Óscar Sergio Orozco Vázquez - A01634257

1¿Qué para qué variables fue más conveniente usar: modelo lineal o polilineal?

En el análisis proporcionado, se utilizó un modelo de regresión lineal para predecir las "Units Sold" en función del "Manufacturing Price". En este caso, un modelo lineal se utilizó debido a que se está evaluando cómo el precio de fabricación afecta directamente a las unidades vendidas en un escenario de datos de la vida real. 

2¿Crees que estos clusters puedan ser representativos de los datos? ¿Por qué?

Los clusters creados a través del algoritmo K-Means se basan en las variables "Units Sold" y "Sale Price". En este caso, los clusters podrían considerarse representativos ya que las unidades vendidas y los precios de venta están relacionados entre si.

3¿Cómo obtuviste el valor de k a usar?

El valor de "k" se determinó probando varios valores (desde 2 hasta 10) y evaluando la inercia y el coeficiente de silueta para cada valor de "k". 

4¿Los centros serían más representativos si usaras un valor más alto? ¿Más bajo?

Si usas un valor más alto de "k", los centros serán más representativos de subgrupos más específicos de tus datos, mientras que un valor más bajo de "k" agrupará datos de manera más general.

5¿Qué distancia tienen los centros entre sí? 

Centros de los clusters:
[[ 577.          125.61413043]
 [1967.28963415  118.95121951]
 [1281.578125    125.82291667]
 [3824.21428571   96.52380952]
 [2666.41007194  101.39568345]]
 
6¿Qué pasaría con los centros si tuviéramos muchos datos anómalos en el análisis de cajas y bigotes?

La presencia de datos anómalos puede afectar los centros de los clusters. Esto puede resultar en que los centros de los clusters estén sesgados.

7Basándonos en los centros de los clusters y en el modelo de regresión lineal, podemos obtener ciertas conclusiones:

El modelo de regresión lineal sugiere una relación entre el "Manufacturing Price" y las "Units Sold". A medida que el precio de fabricación aumenta, las unidades vendidas tienden a disminuir.
Los clusters creados podrían representar diferentes grupos de productos o situaciones de venta en función de las unidades vendidas y los precios de venta.
Los datos se pueden dividir en cinco clusters con centros que varían en términos de unidades vendidas y precios de venta.
La elección del valor "k" puede influir en la interpretación de los clusters y en su utilidad para la toma de decisiones.
