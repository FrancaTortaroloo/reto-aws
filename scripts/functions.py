#%%
# antes de empezar importamos las librerías que vamos a usar. 
# Importar librerías para web scraping y manipulación de datos
# -----------------------------------------------------------------------
from bs4 import BeautifulSoup
import requests

# Importar librerías para manipulación y análisis de datos
# -----------------------------------------------------------------------
import pandas as pd

# Importar librerías para procesamiento de texto
# -----------------------------------------------------------------------
import re

# %%
#funcion para extraer la tabla

def extraer_tabla(url):
    #solicitud HTTP a la página
    response = requests.get(url)
    #crear el objeto BS para analizar el HTML
    soup = BeautifulSoup(response.text, 'html.parser')
    #extraer la primera tabla, es la que necesito
    tablas = soup.find_all('table')
    tabla = tablas[0] 
    #extraer los encabezados
    headers = [header.text.strip() for header in tabla.find_all('th')]
    #extraer las filas de la tabla
    rows = []
    for row in tabla.find_all('tr'):
        cells = row.find_all('td')
        if len(cells) > 0:
            rows.append([cell.text.strip() for cell in cells])
    #crear df con encabezados y filas
    df = pd.DataFrame(rows, columns=headers)
    return df

#%%
# ver la forma del df
def exploracion_datos(df):
    print('_____________ INFORMACIÓN GENERAL DEL DATAFRAME ____________\n')
    print(df.info())

    print('___________________ FORMA DEL DATAFRAME ____________________\n')
    
    print(f"El número de filas que tenemos es de {df.shape[0]}.\nEl número de columnas es de {df.shape[1]}\n")
    

    print('_______________ NULOS, ÚNICOS Y DUPLICADOS _________________\n')
    
    print('La cantidad de valores NULOS por columna es de:\n')
    print(df.isnull().sum())
    print('____________________________________________________________\n')

    print('La cantidad de valores ÚNICOS por columna es de:\n')
        
    for columna in df.columns:
        cantidad_valores_unicos = len(df[columna].unique())
    
        print(f'La columna {columna}: {cantidad_valores_unicos}')

    """ Otra forma más rápida de obtener la lista de valores únicos por columna es usando df.nunique()"""

    print('____________________________________________________________\n')

    print('La cantidad de valores DUPLICADOS por columna es de:\n')

    """En análisis posteriores hemos detectado que hay columnas con valores duplicados que nos interesa filtrar, 
    así que vamos a realizar otro bucle for para iterar por todas las columnas del DF y obtener los duplicados de cada una de ellas."""

    for columna in df.columns:
        cantidad_duplicados = df[columna].duplicated().sum()
    
        print(f'La columna {columna}: {cantidad_duplicados}')

    try:
        print('____________________ RESUMEN ESTADÍSTICO ____________________')
        print('____________________ Variables Numéricas __________________\n')
        print(df.describe().T)
    
        print('___________________ Variables Categóricas _________________\n')
        print(df.describe(include='object').T)
    except ValueError as e:
        if 'No objects to concatenate' in str(e):
            print('No hay variables categóricas en el DataFrame.')
        else:
            raise e


#%%
# cambiar columna de fecha de lanzamiento y dividir en 2 columnas una con el mes y la otra con el año
# Función para extraer el nombre del mes
def extraer_mes(fecha):
    # Buscar el nombre del mes (en español)
    meses = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']
    for mes in meses:
        if mes in fecha.lower():
            return mes
    return ''

def procesar_lanzamientos(df):
    # Extraer el año y el mes de lanzamiento
    df['Año de lanzamiento'] = df['Fecha de lanzamiento'].apply(lambda x: x.split('-')[0][-4:])  # Extraer el año
    df['Mes de lanzamiento'] = df['Fecha de lanzamiento'].apply(extraer_mes)  # Extraer el mes
    return df
#%%
# Función para limpiar los datos, conservando solo el número y la palabra "millones"
def limpiar_numero(texto):
    # Eliminar las notas al pie que están entre corchetes
    texto = re.sub(r'\[.*?\]', '', texto).strip()
    
    # Buscar el patrón que consiste en un número seguido de "millones"
    match = re.search(r'(\d+\s*millones)', texto)
    
    # Si encontramos el patrón, lo devolvemos, si no, devolvemos el texto original (o lo que necesites)
    return match.group(1) if match else texto

#%%
#reemplazar valores de 100 millones de str a int

#hacer un diccionario para reemplazar los valores de str a int

valores_dict = {
    '1000 millones': 1000000000,
    '700 millones': 700000000,
    '600 millones': 600000000,
    '505 millones': 505000000,
    '500 millones': 500000000,
    '400 millones': 400000000,
    '380 millones': 380000000,
    '350 millones': 350000000,
    '310 millones': 310000000,
    '300 millones': 300000000,
    '6 millones': 6000000,
    '1 millones': 1000000,
    '280 millones': 280000000,
    '202 millones': 202000000,
    '200 millones': 200000000,
    '160 millones': 160000000,
    '150 millones': 150000000,
    '120 millones': 120000000,
    '101 millones': 101000000,
    '100 millones': 100000000,
    '83 millones': 83000000,
    '80 millones': 80000000,
    '75 millones': 75000000,
    '62 millones': 62000000,
    '60 millones': 60000000,
    '58 millones': 58000000,
    '56 millones': 56000000,
    '50 millones': 50000000,
    '46 millones': 46000000,
    '43 millones': 43000000,
    '9 millones': 9000000,
    '35 millones': 35000000,
    '33 millones': 33000000,
    '34 millones': 34000000,
    '32,5 million\u200b': 32500000,  # Nota: Aquí un valor con decimal y posible typo con "million"
    '30 millones': 30000000,
    '3 millones': 3000000,
    '26 millones': 26000000,
    '29 millones': 29000000,
    '27 millones': 27000000,
    '25 millones': 25000000,
    '23 millones': 23000000,
    '20 millones': 20000000,
    '18 millones': 18000000,
    '17 millones': 17000000,
    '2 millones': 2000000,
    '15 millones': 15000000,
    '14 millones': 14000000,
    '5 millones': 5000000,
    '11 millones': 11000000,
    '10 millones': 10000000,
    '10  millones': 10000000  # Corrigiendo espacios extra
}

#funcion para reemplazar valores

def reemplazar_valores(valor):
    # Si el valor está en el diccionario, devuelve el número
    if valor in valores_dict:
        return valores_dict[valor]
    # Si no está, devuelve el valor original o un valor por defecto
    else:
        return valor

#%%

