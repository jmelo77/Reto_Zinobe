# RETO ZINOBE

## Introducción

+ [Python 3.7.6](https://www.python.org/downloads/release/python-376/).
+ Se utilizo la libreria [Pandas](https://pypi.org/project/pandas/).
+ Para las pruebas unitarias se utilizo la libreria [Unittest](https://pypi.org/project/unittest/) y la aplicación Postman.    

## Prerequisitos

+ Instalar [Python 3.7.6](https://www.python.org/downloads/release/python-376/)

Habilitar entorno virtual de 
Python y luego instalar las dependencias del proyecto.

```commandline
python -m venv venv
.\venv\Scripts\activate
python -m pip install -r requirements.txt
```

## Diseño de la Solución. 

+ Hacer una petición al servicio API Rest https://restcountries.com/v3.1/all para recibir como respuesta un JSON con toda la información de los países.
+ Tomar el diccionario de países y crear un dataframe con la librería pandas.
+ Encriptar en SHA1 el idioma de los paises.
+ Convertir el dataframe mencionado antes en una archivo JSON, con el comando .to_json().
+ Convertir el dataframe mencionado antes en una base de datos sqlite, con el comando .to_sql().

## Proceso ETL

![alt text](https://github.com/jmelo77/Reto_Zinobe/blob/main/etl.png)
