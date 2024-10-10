# Proyecto: Videojuegos más jugados por número de jugadores.

El objetivo de este proyecto es aprender a usar AWS: el bucket de S3 y quicksight para crear un dashboard de informes interactivo.


## Tecnologías que se usaron

Web Scraping
Extracción y limpieza de datos
Implementación de dashboards

## Proceso de ETL

Dentro de la carpeta scripts, se encuentran los archivos `functions.py` y `reto-videojuegos.py`. Dentro del archivo `reto-videojuegos.py` se procesan los datos descargados y genera archivos limpios y transformados.
En la carpeta `input data` se encuentra el archivo csv que se ha creado a partir de la extracción y limpieza de los datos de una tabla que se encuentra en la página de wikipedia (fuente: https://es.wikipedia.org/wiki/Anexo:Videojuegos_m%C3%A1s_jugados_por_n%C3%BAmero_de_jugadores ).  

## Objetivo

Analizar la cantidad de cuentas registradas por cada año en videojuegos, el modelo de negocio que más cuentas registradas tiene y el videojuego que más cuentas registradas tiene.

## Visualizaciones

Se ha llegado a la conclusión que los juegos que más cuentas registradas tienen son Crossfire y Pubg, con 1 millón de cuentas registradas en cada juego. 

![Juegos más descargados](https://github.com/FrancaTortaroloo/reto-aws/blob/main/assets/Videojuegos%20con%20m%C3%A1s%20cuentas%20registradas.png)

El modelo de negocio que más cuentas registradas tiene es el gratuito.

![Modelo de negocio con más cuentas registradas](https://github.com/FrancaTortaroloo/reto-aws/blob/main/assets/Modelo%20de%20negocio%20con%20m%C3%A1s%20cuentas%20registradas.png)

`En conclusión`, si quieren lanzar un juego que tenga muchas cuentas registradas, tiene que ser uno de guerra ya que es el estilo del Pubg y Crossfire y del estilo competitivo, eso atrae más público. Por otro lado, si lo quieren hacer rentable, ¡a buscarse sponsors!

### NOTA: 

Dentro de la carpeta `assets` se puede ver el dashboard completo. 

![Dashboard completo](https://github.com/FrancaTortaroloo/reto-aws/blob/main/assets/Videojuegos%20m%C3%A1s%20jugados.pdf)

### Nota 2: 
En la esquina inferior del lado izquierdo se puede apreciar lo siguiente:

![botón de navegación](https://github.com/FrancaTortaroloo/reto-aws/blob/main/assets/Bot%C3%B3n%20de%20navegaci%C3%B3n.png)

Como es una imagen, no se puede distinguir que es un botón de navegación, en él se puede elegir el año y se puede ver qué juego tuvo más cuentas registradas en ese año. Como se puede ver en la imagen de abajo, en el año 2017 el juego con más cuentas registradas fue pubg

![Ejemplo botón de navegación](https://github.com/FrancaTortaroloo/reto-aws/blob/main/assets/Bot%C3%B3n%20de%20navegaci%C3%B3n%20apreciaci%C3%B3n.png)

