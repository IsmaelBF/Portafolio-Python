import pandas as pd

df=pd.read_csv(r"medallas.csv")
print(df)

#usar metodos basicos explorar el data frame
print("shape")
print(df.shape)
print("columns")
print(df.columns)
print("info")
print(df.info())
print("describe")
print(df.describe())

#Limpieza de datos
print("valores faltantes contados por columnas")
print(df.isnull().sum())

#reemplazar los valores nulos en las medallas con 0
valores_nuevos = {"Oro":0,"Plata":0,"Bronce":0}
df_rellenado = df.fillna(valores_nuevos)
print(df_rellenado.isnull().sum())
print(df_rellenado)
#convertir los valores float a valores enteros
df_rellenado["Oro"]= df_rellenado["Oro"].astype(int)
df_rellenado["Plata"]= df_rellenado["Plata"].astype(int)
df_rellenado["Bronce"]= df_rellenado["Bronce"].astype(int)

#ordenar el dataframe por paises con mas medallas de oro
df_descendente = df_rellenado.sort_values(by="Oro",ascending=False)
print("Los paises con mas medallas de oro son")
print(df_descendente.head(3)) 

#Obetener los paises que ganaron mas de 10 medllas en total
filtro = df_rellenado["Total"]>10
paises_con_mas_de_10_medallas= df_rellenado[filtro]
print(paises_con_mas_de_10_medallas.sort_values("Total",ascending=False))