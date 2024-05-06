## CONTEXTO CASO

Valve, los ha contactado como equipo de análisis de datos y modelado de Machine Learning para analizar y realizar modelos predictivos sobre los datos.

En cada partida de Counter Strike: GO dos equipos de 5 jugadores (denominados terroristas y contra-terroristas) se enfrentan.

El objetivo del equipo terrorista es plantar una bomba con timer de 45 segundos en uno de dos sitios específicos dentro de un mapa. Por otro lado, el objetivo del equipo contra-terrorista es evitar que la bomba sea plantada o desactivarla antes de que esta explote cuando ya ha sido plantada. Los datos a utilizar corresponden a sobre 7000 partidas del juego (con un máximo de 10 jugadores c/u)

Los datos han sido extraídos de replays, los cuales son archivos propietarios con la información de cada una de las acciones realizadas por cada jugador dentro de una partida. Los replays han sido extraídos de la red utilizando un scrapper y pre-procesados utilizando un script.

En este caso, la data corresponde a un archivo CSV con 79.157 filas, cada una correspondiente a un jugador dentro de una partida. El archivo contiene 29 columnas correspondientes a variables que describen las acciones del jugador dentro del juego.



## Evaluacion 2

### Fase 1
Se recomienda investigar sobre el contexto de negocio, sobre los datos, uso de los campos en estadísticas de juegos, ver en qué se relacionan los contenidos revisados en la asignatura con lo planteado como caso de estudio.

Plantear hipótesis del negocio posibles para objetivos de tareas de regresión y de clasificación


Negocio: Valve, los ha contactado como equipo de análisis de datos y modelado de Machine Learning para analizar y realizar modelos predictivos sobre los datos.


### Fase 2
Se recomienda obtener estadísticos descriptivos para apoyar hipótesis inferenciales.

Reconocer la naturaleza de los datos y como tratarlos en etapas posteriores y dar ideas de como se podría transformar.

Identificar MissingValues, outliers, medidas de posición, medidas de dispersión etc.

### Fase 3
Se recomienda considerar todas las transformaciones necesarias para obtener la data lo más limpia posible.

Realizar tratamiento a todos los datos que consideren necesarios.


### Especifiaciones

Aplica estadística descriptiva e inferencial a los datos recolectados, considerando problemáticas, objetivos y tipo de negocio, para descubrir aspectos relevantes del negocio.

Realiza lectura de datos considerando técnicas de limpieza y uso de lenguajes de programación, orientados al análisis de datos, para descubrir aspectos relevantes del negocio.


### Metodología CRISP-DM

1) Business Understanding : Detallar y describir en el formato habilitado, todo el conocimiento y aspectos relevantes que tengan sobre el caso de estudio.
    - Identificar aspectos claves del uso de Machine Learning en el área de los videojuegos, analizar si los datos entregados son relevantes o si servirán para poder realizar predicciones en tareas de regresión y de clasificación


2) Data Understanding: Analizar y definir las características que contiene el dataset entregado, considerando tipos de datos, naturaleza de los datos, estadísticos, distribución, correlación, etc.
    - Todo lo necesario para poder entender como se compone la fuente de información entregada, y con ello apoyar el entendimiento del negocio, identificando cuales son las transformaciones que se deben realizar en la fase posterior.

3) Data Transformation: Transformar y ejecutar las rutinas de limpieza necesarias para que los objetivos planteados inicialmente puedan cumplirse.

    - Esto considera al menos tratamiento de NaN, outliers, scaling, normalización, estandarización, encoder, ingeniería de características, etc. siempre considerando los objetivos planteados y la selección de features significativos de acuerdo al target seleccionado, utilizando técnicas como la correlación de pearson


### Rubrica

1) Utiliza al menos 4 funciones necesarias para extraer elementos básicos de estadística descriptiva. Interpreta correctamente los elementos estadísticos obtenidos a partir de los datos. ✅

2) Interpreta los elementos estadísticos obtenidos a partir de los datos ✅

3) Obtiene coeficiente de correlación por sí solo entre las características o bien la matriz de Correlación de Pearson. ✅

4) Interpreta los valores obtenidos identificando valores de correlación directa e inversa. ✅

5) Con el uso de estadísticos obtiene KPI relevantes como cantidad de derrotas, cantidad de triunfos, cantidad de jugadores, promedio de tiempo de partida, etc. ❓

6) Identifica cuando el dato es numérico continuo, discreto, o variable categórica nominal u ordinal. ✅

7) Trabaja los missing values (valores NaN) y los datos outliers, considerando las mejores prácticas con respecto al uso de los datos.
 - **Datos outlier**: Valor que se sale del promedio (Valor atipico). ✅

8) Identifica cuales son características significativas para el contexto del objetivo que el equipo se planteó de negocio. (Hipotesis) ✅

9) Utiliza técnicas de transformación de datos adecuada de acuerdo a la naturaleza de estos. (UTF 8) ✅

10) Utiliza las técnicas de transformación necesarias, ya sea de scaling, normalización o encoding dejando listos los datos para la fase de Modeling (Grafico) ✅❓falta scaling
### Hipótesis de negocio para regresión: 

1. El tiempo de juego de un jugador influye en su rendimiento en la partida.
2. La cantidad de kills de un jugador influye en la victoria de su equipo.
3. La cantidad de muertes de un jugador influye en la victoria de su equipo.
4. La cantidad de headshots de un jugador influye en la victoria de su equipo.
5. La cantidad de bombas plantadas por un jugador influye en la victoria de su equipo.
6. La cantidad de bombas desactivadas por un jugador influye en la victoria de su equipo.
7. La cantidad de rondas ganadas por un jugador influye en la victoria de su equipo.
8. La cantidad de rondas perdidas por un jugador influye en la victoria de su equipo.
9. La cantidad de rondas jugadas por un jugador influye en la victoria de su equipo.
10. La cantidad de partidas jugadas por un jugador influye en la victoria de su equipo.


### Hipótesis de negocio para clasificación:

1. Un jugador que juega más de 100 horas es un jugador experimentado.
2. Un jugador que tiene más de 1000 kills es un jugador experimentado.
3. Un jugador que tiene más de 1000 muertes es un jugador experimentado.
4. Un jugador que tiene más de 100 headshots es un jugador experimentado.
5. Un jugador que ha plantado más de 100 bombas es un jugador experimentado.
6. Un jugador que ha desactivado más de 100 bombas es un jugador experimentado.
7. Un jugador que ha ganado más de 100 rondas es un jugador experimentado.
8. Un jugador que ha perdido más de 100 rondas es un jugador experimentado.
9. Un jugador que ha jugado más de 100 rondas es un jugador experimentado.
10. Un jugador que ha jugado más de 100 partidas es un jugador experimentado.


### Tipos de variables pt6


1) Map: Cualitativa, Nominal
2) Equipo: Cualitativa, Nominal
3) Team_ID: Cuantitativa, Discreta
4) Match_ID: Cuantitativa, Discreta
5) Round_ID: Cuantitativa, Discreta
6) Round_W: Cualitativa, Nominal
7) Match_W: Cualitativa, Nominal
8) Survived: Cualitativa, Nominal
9) AbnormalMatch: Cualitativa, Nominal
10) TimeAlive: Cuantitativa, Continua
11) TravelledDistance: Cuantitativa, Continua
12) RLethalGrenadesThrown: Cuantitativa, Discreta
13) RNonLethalGrenadesThrown: Cuantitativa, Discreta
14) PrimaryAssaultRifle: Cuantitativa, Discreta
15) PrimarySniperRifle: Cuantitativa, Discreta
16) PrimaryHeavy: Cuantitativa, Discreta
17) PrimarySMG: Cuantitativa, Discreta
18) PrimaryPistol: Cuantitativa, Discreta
19) FirstKillTime: Cuantitativa, Continua
20) RoundKills: Cuantitativa, Discreta
21) RoundAssists: Cuantitativa, Discreta
22) RoundHeadshots: Cuantitativa, Discreta
23) RoundFlankKills: Cuantitativa, Discreta
24) RoundStartingEquipmentValue: Cuantitativa, Discreta
25) TeamStartingEquipmentValue: Cuantitativa, Discreta
26) MatchKills: Cuantitativa, Discreta
27) MatchFlankKills: Cuantitativa, Discreta
28) MatchAssists: Cuantitativa, Discreta
29) MatchHeadshots: Cuantitativa, Discreta


### Hipotesis
Cual es la cantidad de rondas que ganan ambos equipos en los cuatro mapas

#### Creemos que los terroristas ganan mas rondas por las kills que hacen por partida en los mapas de (inferno, dust y mirage).




#### Creemos que los CT ganaron mas rondas en todas las partidas en dust_2 por la cantidad de kills contra los terroristas (Correcto)

Se pueden extraer dos conclusiones principales de este gráfico:
- Existe una correlación débilmente positiva entre el número total de asesinatos por ronda y el número de asesinatos por parte de los equipos T y CT. Esto significa que a medida que aumenta el número total de asesinatos por ronda, el número de asesinatos por ambos equipos también tiende a aumentar. El coeficiente de correlación para el lado T es de 0.77, y para el lado CT es de 0.87.
- El equipo CT tiende a tener un mayor número de asesinatos por ronda que el equipo T. Esto se refleja en el hecho de que los puntos de datos del lado CT generalmente están por encima de los puntos de datos del lado T en el diagrama de dispersión.


 #### Creemos que en el mapa de Dust 2 los CT ganan mas por el tiempo de vida y distancia recorrdia (Falso)

##### Análisis del gráfico de los Terroristas:

Distribución de los puntos: Los puntos se encuentran dispersos por todo el gráfico, sin una tendencia clara. Esto indica que no existe una correlación significativa entre el tiempo de vida y la distancia recorrida para los Terroristas.

Interpretación: Este resultado sugiere que la supervivencia de los Terroristas en Dust2 no está directamente relacionada con la distancia que recorren por el mapa. Es decir, no hay una ventaja clara en recorrer más o menos distancia para este equipo.

##### Análisis del gráfico de los Contra-Terroristas:

Distribución de los puntos: Los puntos se concentran en la parte inferior izquierda del gráfico, lo que indica una tendencia negativa. Esto significa que, a mayor distancia recorrida por los Contra-Terroristas, menor es su tiempo de vida promedio.

Interpretación: Este resultado sugiere que los Contra-Terroristas que recorren distancias más largas en Dust2 tienden a morir más rápido que aquellos que se mantienen en posiciones más estáticas. Esto podría deberse a que, al moverse más, se exponen a mayor riesgo de ser detectados y eliminados por los Terroristas.

##### Relación con el número de rondas ganadas:

Aunque la dispersión del tiempo de vida y la distancia recorrida no muestra una correlación directa con el número de rondas ganadas, sí se puede observar una cierta relación indirecta. Si bien los Terroristas no tienen una ventaja clara en cuanto a la relación entre estas dos variables, los Contra-Terroristas sí parecen tener una desventaja. Al morir más rápido cuando recorren distancias más largas, los Contra-Terroristas podrían tener menos oportunidades de defender sus posiciones y ganar rondas.

##### Conclusión:

Si bien la dispersión del tiempo de vida y la distancia recorrida no es un factor determinante en el resultado de las rondas en Dust2, sí se puede observar una cierta tendencia que podría favorecer a los Terroristas. La mayor supervivencia de los Terroristas al recorrer distancias similares o menores, en comparación con los Contra-Terroristas, podría ser un factor que contribuya a su mayor número de rondas ganadas en este mapa.

Es importante destacar que este análisis se basa en una única muestra de datos, y que los resultados podrían variar al considerar un conjunto de datos más amplio. 


