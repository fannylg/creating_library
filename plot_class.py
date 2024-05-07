# plot_functions.py

# Importamos las librerias necesarias para la ejecución de las funciones
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Definimos la función para graficar histogramas
def histogramas(df, vcon):
    for variable in vcon:
        plt.figure(figsize=(8, 6))
        df[variable].hist(color='skyblue', bins=20)
        plt.title(f'Histograma de {variable}')
        plt.xlabel(f'{variable}')
        plt.ylabel('Frecuencia')
        plt.grid(axis='y', alpha=0.75)
        plt.show()

# Definimos la función para graficar boxplots
def boxplots(df, vcon):
    for variable in vcon:
        plt.figure(figsize=(10, 6))
        sns.boxplot(x=df[variable], color='skyblue')
        plt.title(f'Boxplot de {variable}')
        plt.xlabel('Valores')
        plt.ylabel(f'{variable}')
        plt.show()

# Definimos la función para graficar barras verticales
def plot_horizontal_bar(df, vard):
    for variable in vard:
        plt.figure(figsize=(10, 6))
        plt.barh(df.index, df[vard], color='skyblue')
        plt.xlabel(vard)
        plt.ylabel('Indice')
        plt.title('grafico de barras horizontal de ' + vard, fontsize=16)
        plt.gca().invert_yaxis()
        plt.show()

# Definimos la función para graficar serie de tiempo  
def plot_serie_temporal(df, varc):
    plt.figure(figsize=(10, 6))
    for col in varc:
        plt.plot(df['Date'], df[col], label=col)
        plt.xlabel('Fecha', fontsize=14)
        plt.ylabel('Valor', fontsize=14)
        plt.title('Gráfico de Líneas para Series Temporales Unidimensionales', fontsize=16)
        plt.legend()
        plt.grid(True)
        plt.show()

# Definimos la función para graficar dotplot
def plot_dotplot(df, vard):
    for col in varc:
        sns.set_style("whitegrid")
        plt.figure(figsize=(10, 6))
        plt.plot(df[vard].value_counts().index, df[vard].value_counts().values, 'o', color='orange')
        plt.title('Dotplot de la variable discreta {}'.format(vard))
        plt.xlabel('Valores')
        plt.ylabel('Frecuencia')
        plt.show()

# Definimos la función para graficar heatmap
def plot_heatmap(df,variables_continuas):
    df_corr=df[variables_continuas].corr()
    sns.heatmap(df_corr,cmap='RdYlGn',annot = True)

# Definimos la función para graficar heatmap de variables categóricas
def plot_heatmap_cat(df):
  col1=input('Coloca el nombre la variable 1: ')
  col2=input('Coloca el nombre la variable 2: ')
  df_hm=pd.crosstab(index=df[col1],columns=df[col2])
  sns.heatmap(df_hm,cmap='RdYlGn',annot = True,fmt=".2f")

# Definimos la función para graficar violinplot
def plot_violine(df, varc, vard):
    for col in varc:
        plt.plot(df['Date'], df[col], label=col)
        plt.figure(figsize=(10, 6))
        sns.violinplot(x=df[varc], y=df[vard], color='skyblue')
        plt.title('Violinplot de ' + vard + ' vs ' + varc, fontsize=16)
        plt.xlabel(varc)
        plt.ylabel(vard)
        plt.show()

# Definimos la funcion para graficar la densidad de las variables continuas
def plot_densidad(df,varc):
  for col in varc:
    sns.kdeplot(x=df[col],fill=True)
    plt.title(f'Grafica de densidad de : {col}')
    plt.show()

