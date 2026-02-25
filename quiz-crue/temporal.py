import pandas as pd

df = pd.read_csv("incidentes_crue_diarios.txt", sep="\t")
df["fecha"] = pd.to_datetime(df["fecha"])

df["año"] = df["fecha"].dt.year
df["mes"] = df["fecha"].dt.month
df["dia_semana"] = df["fecha"].dt.day_name()

promedio_2022 = df[df["año"] == 2022]["incidentes"].mean()
promedio_2023 = df[df["año"] == 2023]["incidentes"].mean()
diferencia = promedio_2023 - promedio_2022

promedio_dia = df.groupby("dia_semana")["incidentes"].mean()
orden_dias = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
promedio_dia = promedio_dia.reindex(orden_dias)

dia_mas_incidentes = promedio_dia.idxmax()

promedio_mes = df.groupby("mes")["incidentes"].mean().sort_values(ascending=False)
top3 = promedio_mes.head(3)
mes_mas_bajo = promedio_mes.sort_values().index[0]

print("\nPROMEDIO POR AÑO")
print(f"Promedio 2022: {promedio_2022:.2f}")
print(f"Promedio 2023: {promedio_2023:.2f}")
print(f"Diferencia (2023-2022): {diferencia:.2f}")

print("\nPROMEDIO POR DÍA DE LA SEMANA")
print(f"Lunes: {promedio_dia['Monday']:.2f}")
print(f"Martes: {promedio_dia['Tuesday']:.2f}")
print(f"Miércoles: {promedio_dia['Wednesday']:.2f}")
print(f"Jueves: {promedio_dia['Thursday']:.2f}")
print(f"Viernes: {promedio_dia['Friday']:.2f}")
print(f"Sábado: {promedio_dia['Saturday']:.2f}")
print(f"Domingo: {promedio_dia['Sunday']:.2f}")
print(f"Día con MÁS incidentes: {dia_mas_incidentes}")

print("\nPROMEDIO POR MES")
print(f"Mes #1 (más alto): {top3.index[0]}")
print(f"Mes #2: {top3.index[1]}")
print(f"Mes #3: {top3.index[2]}")
print(f"Mes más BAJO: {mes_mas_bajo}")