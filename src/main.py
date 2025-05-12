# src/main.py

import matplotlib.pyplot as plt

# Imaginary data
years = [2018, 2019, 2020, 2021, 2022]
gdp = [500, 520, 480, 530, 550]

plt.plot(years, gdp, marker='o')
plt.title("Japan GDP")
plt.xlabel("Year")
plt.ylabel("GDP (trilion yen)")
plt.grid(True)
plt.tight_layout()
plt.show()
