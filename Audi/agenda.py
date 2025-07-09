import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Dosyaları oku
df_water = pd.read_excel("Water_consumption_AH_2024.xlsx", header=None)

# Veri sütunları 4. sütundan başlıyor (ilk 4 sütun: açıklamalar)
start_col = 4
num_months = 12  # Excel'de Ocak–Aralık

months = list(range(1, 13))  # 1–12

records = []

# Satır 4'ten sonra veriler başlıyor
for i in range(4, df_water.shape[0]):
    row = df_water.iloc[i]
    production_hall = row[1]
    short_name = row[2]
    unit = row[3]

    for idx, month in enumerate(months):
        col_idx = start_col + idx
        if col_idx >= df_water.shape[1]:
            break
        value = row[col_idx]

        if pd.notna(value):
            try:
                records.append({
                    "Production_Hall": str(production_hall).strip(),
                    "Short_Name": str(short_name).strip(),
                    "Unit": str(unit).strip(),
                    "Month": month,
                    "Consumption_m3": float(value)
                })
            except:
                continue

# Detaylı veri tablosu
df_detailed = pd.DataFrame(records)

# Ay isimleriyle etiketle
month_names = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]
df_detailed["Month_Name"] = df_detailed["Month"].apply(lambda x: month_names[x-1])

# Ay bazında toplam tüketim
monthly_total = df_detailed.groupby("Month_Name")["Consumption_m3"].sum().reindex(month_names).reset_index()

# Çizgi grafik (Line Chart)
plt.figure(figsize=(12,6))
sns.lineplot(data=monthly_total, x="Month_Name", y="Consumption_m3", marker="o", linewidth=2.5, color="darkblue")

plt.title("Ocak–Aralık Arası Toplam Su Tüketimi", fontsize=16)
plt.xlabel("Ay", fontsize=14)
plt.ylabel("Toplam Tüketim (m³)", fontsize=14)
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()
