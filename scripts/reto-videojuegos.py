#%%
import functions as func
import pandas as pd
#%%
print('Visualizo la extracción')

df_videojuegos = func.extraer_tabla("https://es.wikipedia.org/wiki/Anexo:Videojuegos_m%C3%A1s_jugados_por_n%C3%BAmero_de_jugadores")
print(df_videojuegos)

# %%
df = pd.DataFrame(df_videojuegos)

df

#%%
#Exploración de datos

df_explorar = func.exploracion_datos(df)
#%%
df_explorar
#%%
# Procesar el DataFrame para extraer año y mes
df_procesado = func.procesar_lanzamientos(df)

# Mostrar una muestra del DataFrame procesado
print(df_procesado.sample(4))
# %%
# Eliminar la columna original 'Fecha de lanzamiento' y la columna Ref que no me servirán
df = df.drop(columns=['Fecha de lanzamiento','Ref.'])
#comprobar que se hayan eliminado
df
# %%
# Aplicar la función limpiar numeros a la columna 'Número'
df['Número'] = df['Número'].apply(func.limpiar_numero)

#%% 
#comprobar que se hayan cambiado los datos
df
#%%
#reemplazar valores de str a valores int

df['Número'] = df['Número'].apply(func.reemplazar_valores)
#%%
#comprobar el cambio
df.sample(5)

#%%
#guardar en csv

df.to_csv('videojuegos-limpio.csv')

