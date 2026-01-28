import pandas as pd
import numpy as np
ruta= r"C:\Curso de python\Portafolio-Python\Proyectos\datos_meteorologicos.csv"

df = pd.read_csv(ruta)
print(df)

print(df.info())
print(df.describe())
print(df.isnull().sum())
#transformar las fechas a date time 

df['Fecha']=pd.to_datetime(df['Fecha'],format='%d/%m/%Y')
print(df)
#convertir columnas del dataframe a arrays de numpy
columnaFecha=  df['Fecha'].to_numpy()
columnaTemp= df['Temperatura'].to_numpy()
columnaPrecipitacion=df['Precipitación'].to_numpy()
columnaHumedad= df['Humedad'].to_numpy()

#reemplazar los valroes nulos en los array por el prmedio de dicho 
print(np.isnan(columnaFecha).sum())
print(np.isnan(columnaTemp).sum())
print(np.isnan(columnaPrecipitacion).sum())
print(np.isnan(columnaHumedad).sum())

columnaTemp = np.where(np.isnan(columnaTemp),np.nanmean(columnaTemp), columnaTemp)
print(np.isnan(columnaTemp).sum())
columnaPrecipitacion = np.where(np.isnan(columnaPrecipitacion),np.nanmean(columnaPrecipitacion), columnaPrecipitacion)
print(np.isnan(columnaPrecipitacion).sum())
columnaHumedad= np.where(np.isnan(columnaHumedad),np.nanmean(columnaHumedad), columnaHumedad)
print(np.isnan(columnaHumedad).sum())

#obtener la temperatura promedio
meanTemp=np.mean(columnaTemp)
print(meanTemp)
#total de precipitaciones
totalPrecipitaciones= np.sum(columnaPrecipitacion)
print(totalPrecipitaciones)
#maxima humedad registrada
maxHum = np.max(columnaHumedad)
print(maxHum)
#La fecha mas calurosa
maxTemp = np.argmax(columnaTemp)
print('indice de la temperatura mas alta', maxTemp)
fechaMasCalurosa = columnaFecha[maxTemp]
print('la fecha mas calurosa es', fechaMasCalurosa)

#La fecha mas fria
minTemp = np.argmin(columnaTemp)
print('indice de la temperatura mas baja', minTemp)
fechaMasFria= columnaFecha[minTemp]
print('La fecha mas fria es: ', fechaMasFria)
#Exportar los resultados a un nuevo csv

resultados = pd.DataFrame({
    'Metrica': ['Temperatura promedio','Precipitacion total', 'Humedad maxima', 'Fecha más calurosa','Fecha más fria'],
    'Valor':[meanTemp,totalPrecipitaciones,maxHum,fechaMasCalurosa,fechaMasFria]
})

# Intenta guardar fuera de 'Documents' para probar permisos
# Fíjate en el 'OneDrive' en la ruta
resultados.to_csv(r'C:\Curso de python\Portafolio-Python\Proyectos\resultados analisis meteorologicos.csv')