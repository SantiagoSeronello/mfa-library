
import pandas as pd
import datetime as dt
from datetime import timedelta

def hola(a):
   print(a)

def Start_End_Date(df, metrics):
  # Paso start y end a formato fecha
  df['Start'] = pd.to_datetime(df['Start'], format="%Y/%m/%d")
  df['End'] = pd.to_datetime(df['End'], format="%Y/%m/%d")

  # computo diferencia de dias
  df = df.assign(diferencia_dias = df["End"] - df["Start"])

  # guardo un df con los same days
  same_days = df[df["diferencia_dias"] == dt.timedelta(days=0)]

  # Filtro los casos distintos de same days
  df["diferencia_dias"] = df["diferencia_dias"] / pd.Timedelta("1 day") + 1
  dif_dias = df[df["diferencia_dias"] > 1]

  # abro los casos entre la cantidad de dias del periodo
  dif_dias = dif_dias.loc[dif_dias.index.repeat(dif_dias["diferencia_dias"])]
  dif_dias = dif_dias.reset_index(drop=True)

  dif_dias["diferencia_dias"] = dif_dias["diferencia_dias"].astype(int)

  # ordeno en base a todas las columnas para establecer los dias para cada periodo
  dif_dias = dif_dias.sort_values(by=list(dif_dias.columns)).reset_index(drop=True)

  # Inicializa la columna 'week' con NaN
  dif_dias['week'] = pd.NaT

  # Itera sobre las filas del dataframe
  for i in range(len(dif_dias)):
      if i == 0 or not dif_dias.iloc[i, :-1].equals(dif_dias.iloc[i-1, :-1]):
          dif_dias.at[i, 'week'] = dif_dias.at[i, 'Start']
      else:
          dif_dias.at[i, 'week'] = dif_dias.at[i-1, 'week'] + timedelta(days=1)

  metrics = ["LIQUIDO_f", "INS_F", "GRP_F"]

  for i in metrics:
    dif_dias[i] = dif_dias[i] / dif_dias["diferencia_dias"]

  same_days["week"] = same_days["Start"]
  same_days["diferencia_dias"] = same_days["diferencia_dias"].astype(int)

  resultado = pd.concat([same_days, dif_dias])
