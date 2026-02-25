import pandas as pd
import numpy as np
from scipy import stats

df = pd.read_csv("incidentes_crue_diarios.txt", sep="\t")
df["fecha"] = pd.to_datetime(df["fecha"])

incidentes = df["incidentes"]

media = incidentes.mean()
mediana = incidentes.median()
moda = stats.mode(incidentes, keepdims=True)[0][0]

desviacion = incidentes.std()
varianza = incidentes.var()
cv = (desviacion / media) * 100
rango = incidentes.max() - incidentes.min()

q1 = incidentes.quantile(0.25)
q2 = incidentes.quantile(0.50)
q3 = incidentes.quantile(0.75)
iqr = q3 - q1
p95 = incidentes.quantile(0.95)

max_valor = incidentes.max()
min_valor = incidentes.min()
dia_max = df.loc[df["incidentes"].idxmax(), "fecha"]
dia_min = df.loc[df["incidentes"].idxmin(), "fecha"]

print("\nMEDIDAS DE TENDENCIA CENTRAL")
print(f"Media de incidentes: {media:.2f}")
print(f"Mediana: {mediana:.2f}")
print(f"Moda (valor más frecuente): {moda}")

print("\nMEDIDAS DE DISPERSIÓN")
print(f"Desviación estándar: {desviacion:.2f}")
print(f"Varianza: {varianza:.2f}")
print(f"Coeficiente de variación (CV): {cv:.2f}%")
print(f"Rango (max - min): {rango}")

print("\nCUARTILES Y PERCENTILES")
print(f"Q1 (percentil 25): {q1:.2f}")
print(f"Q2 (mediana): {q2:.2f}")
print(f"Q3 (percentil 75): {q3:.2f}")
print(f"Rango intercuartílico (IQR): {iqr:.2f}")
print(f"Percentil 95: {p95:.2f}")

print("\nVALORES EXTREMOS")
print(f"Día con MÁS incidentes: {dia_max.date()}")
print(f"Valor máximo: {max_valor}")
print(f"Día con MENOS incidentes: {dia_min.date()}")
print(f"Valor mínimo: {min_valor}")