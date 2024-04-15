

# CONTEXTO CASO

# Valve, los ha contactado como equipo de análisis de datos y modelado de Machine Learning para analizar y realizar modelos predictivos sobre los datos.

# En cada partida de Counter Strike: GO dos equipos de 5 jugadores (denominados terroristas y contra-terroristas) se enfrentan.

# El objetivo del equipo terrorista es plantar una bomba con timer de 45 segundos en uno de dos sitios específicos dentro de un mapa. Por otro lado, el objetivo del equipo contra-terrorista es evitar que la bomba sea plantada o desactivarla antes de que esta explote cuando ya ha sido plantada. Los datos a utilizar corresponden a sobre 7000 partidas del juego (con un máximo de 10 jugadores c/u)

# Los datos han sido extraídos de replays, los cuales son archivos propietarios con la información de cada una de las acciones realizadas por cada jugador dentro de una partida. Los replays han sido extraídos de la red utilizando un scrapper y pre-procesados utilizando un script.

# En este caso, la data corresponde a un archivo CSV con 79.157 filas, cada una correspondiente a un jugador dentro de una partida. El archivo contiene 29 columnas correspondientes a variables que describen las acciones del jugador dentro del juego.



# Fase 1

# Se recomienda investigar sobre el contexto de negocio, sobre los datos, uso de 
# los campos en estadísticas de juegos, ver en qué se relacionan los contenidos 
# revisados en la asignatura con lo planteado como caso de estudio.
# Plantear hipótesis del negocio posibles para objetivos de tareas de regresión y de clasificación


# Negocio: Valve, los ha contactado como equipo de análisis de datos y modelado de Machine Learning para analizar y realizar modelos predictivos sobre los datos.

# Hipótesis de negocio para regresión: 

# 1. El tiempo de juego de un jugador influye en su rendimiento en la partida.
# 2. La cantidad de kills de un jugador influye en la victoria de su equipo.
# 3. La cantidad de muertes de un jugador influye en la victoria de su equipo.
# 4. La cantidad de headshots de un jugador influye en la victoria de su equipo.
# 5. La cantidad de bombas plantadas por un jugador influye en la victoria de su equipo.
# 6. La cantidad de bombas desactivadas por un jugador influye en la victoria de su equipo.
# 7. La cantidad de rondas ganadas por un jugador influye en la victoria de su equipo.
# 8. La cantidad de rondas perdidas por un jugador influye en la victoria de su equipo.
# 9. La cantidad de rondas jugadas por un jugador influye en la victoria de su equipo.
# 10. La cantidad de partidas jugadas por un jugador influye en la victoria de su equipo.


# Hipótesis de negocio para clasificación:

# 1. Un jugador que juega más de 100 horas es un jugador experimentado.
# 2. Un jugador que tiene más de 1000 kills es un jugador experimentado.
# 3. Un jugador que tiene más de 1000 muertes es un jugador experimentado.
# 4. Un jugador que tiene más de 100 headshots es un jugador experimentado.
# 5. Un jugador que ha plantado más de 100 bombas es un jugador experimentado.
# 6. Un jugador que ha desactivado más de 100 bombas es un jugador experimentado.
# 7. Un jugador que ha ganado más de 100 rondas es un jugador experimentado.
# 8. Un jugador que ha perdido más de 100 rondas es un jugador experimentado.
# 9. Un jugador que ha jugado más de 100 rondas es un jugador experimentado.
# 10. Un jugador que ha jugado más de 100 partidas es un jugador experimentado.


# Obtener datos de un CSV y mostrarla
import pandas as pd
data = pd.read_csv('db/dbcs.csv')
print(data.head())