# src/main.py

import pandas as pd
import matplotlib.pyplot as plt
import os


# 実質GDP(value)
## CSVファイルのパス
csv_path = os.path.join("data", "processed", "gdp", "realGDP_value_total.csv")

## CSVの読み込み
df = pd.read_csv(csv_path)

## グラフ描画
plt.figure(figsize=(8, 5))
plt.plot(df["Year"], df["GDP"], marker='o', linestyle='-')

plt.title("Real GDP of Japan")
plt.xlabel("Year")
plt.ylabel("GDP (Billion yen)")
plt.grid(True)
plt.tight_layout()
plt.show()


# # 実質GDPのうち、家計(value)
# ## CSVファイルのパス
# csv_path = os.path.join("data", "processed", "gdp", "realGDP_value_private.csv")

# ## CSVの読み込み
# df = pd.read_csv(csv_path)

# ## グラフ描画
# plt.figure(figsize=(8, 5))
# plt.plot(df["Year"], df["Private"], marker='o', linestyle='-')

# plt.title("Real GDP of Japan")
# plt.xlabel("Year")
# plt.ylabel("Household consumption as a factor of real GDP (Billion yen)")
# plt.grid(True)
# plt.tight_layout()
# plt.show()


# # 実質GDPのうち、政府(value)
# ## CSVファイルのパス
# csv_path = os.path.join("data", "processed", "gdp", "realGDP_value_government.csv")

# ## CSVの読み込み
# df = pd.read_csv(csv_path)

# ## グラフ描画
# plt.figure(figsize=(8, 5))
# plt.plot(df["Year"], df["Government"], marker='o', linestyle='-')

# plt.title("Real GDP of Japan")
# plt.xlabel("Year")
# plt.ylabel("Government consumption as a factor of real GDP (Billion yen)")
# plt.grid(True)
# plt.tight_layout()
# plt.show()


# # 実質GDPのうち、純輸出(value)
# ## CSVファイルのパス
# csv_path = os.path.join("data", "processed", "gdp", "realGDP_value_exports.csv")

# ## CSVの読み込み
# df = pd.read_csv(csv_path)

# ## グラフ描画
# plt.figure(figsize=(8, 5))
# plt.plot(df["Year"], df["NetExports"], marker='o', linestyle='-')

# plt.title("Real GDP of Japan")
# plt.xlabel("Year")
# plt.ylabel("Net Exports as a factor of real GDP (Billion yen)")
# plt.grid(True)
# plt.tight_layout()
# plt.show()
