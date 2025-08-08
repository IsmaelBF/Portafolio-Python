import pandas as pd 
df_tienda1 =  pd.read_csv(r'Datos_Ventas_Tienda.csv')
print(df_tienda1)

df_tienda2 = pd.read_csv(r'Datos_Ventas_Tienda2.csv')
print(df_tienda2)

df_global_tienda = pd.concat([df_tienda1,df_tienda2],ignore_index=True)
print(df_global_tienda)

print(df_global_tienda.info())

print(df_global_tienda.describe())

print(df_global_tienda.isnull().sum())

#transformar las fechas a datetime
df_global_tienda['Fecha']= pd.to_datetime(df_global_tienda['Fecha'])
print(df_global_tienda)


#producto mas vendido
print("\nProducto mas vendido")
df_ventas_por_producto = df_global_tienda.groupby('Producto')['Cantidad'].sum()#se agrupa por producto y se suma la cantidad de cada producto 
print(df_ventas_por_producto.sort_values(ascending=False).head(1))

#mes con mas ventas
print('\nMes con mas ventas')
df_ventas_por_mes = df_global_tienda.groupby(df_global_tienda['Fecha'].dt.to_period('M'))['Total Venta'].sum()#lo agrupamos por mes, con el metodo to period
print(df_ventas_por_mes.sort_values(ascending=False).head(1))

#otra manera de hacer las ventas por mes 
meses= []
for f in df_global_tienda['Fecha']:#se crea una lista con los numeros de los meses de cada fecha
    meses.append(f.month)

df_global_tienda['Meses'] = meses#se agrega la lista a la columna nueva de meses
print('\nOTRO METODO',df_global_tienda)

ventas_por_mes = df_global_tienda.groupby('Meses')['Total Venta'].sum().sort_values(ascending=False) #se agrupa por mes y se imprime el mas alto
print('\nMes con mas ventas',ventas_por_mes.head(1))

#analizar las ventas por categoria
ventas_por_categoria = df_global_tienda.groupby('Producto')['Total Venta'].sum()
print('\nVentas por categoria',ventas_por_categoria)

# guardar dataframe en la pc 
df_global_tienda.to_csv(r'C:\Users\Ryzen5\Documents\Portafolio-Python\Proyectos\Dataframe de tienda.csv')
