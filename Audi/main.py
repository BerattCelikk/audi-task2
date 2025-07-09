import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 

df_top = pd.read_excel("TOP_consumers_engine_2024.xlsx",header=None)
print(df_top.head())



df_water = pd.read_excel("Water_consumption_AH_2024.xlsx",header=None)
print(df_water.head())

print(df_top.info())
print(df_water.info())

consumption = df_water.iloc[3,1:16]
years =df_water.iloc[2,1:16]


consumption = pd.to_numeric(consumption,errors="coerce")
years = pd.to_numeric(years,errors="coerce")

dataframe_water_model = pd.DataFrame({
    "Years" : years,
    "Consumption":consumption
})

dataframe_water_model = dataframe_water_model.dropna()

print(dataframe_water_model)

plt.figure(figsize=(16,8))
sns.lineplot(data =dataframe_water_model,x ="Years",y="Consumption")
plt.xlabel("Years")
plt.ylabel("Consumption")
plt.title("Water Data Model")
plt.grid(True)
plt.show()

print(years)
print(consumption)