# -*- coding: utf-8 -*-
"""
@author: Maciek
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# 1.1. Wczytaj dane z pliku lab2.csv
df = pd.read_csv('lab2.csv', sep=";")


# 1.2. Sprawdź podstawowe informacje o zbiorze danych (df.info(), df.describe(),
#df.head()).
print("Informacje o DataFrame:")
print(df.info())
print("\nStatystyki opisowe:")
print(df.describe())
print("\nPierwsze wiersze:")
print(df.head())

# 1.3. Usuń brakujące wartości poprzez wykorzystanie dropna.
df = df.dropna()

# 1.4. Posortuj dane w zbiorze rosnąco po kolumnie x
df = df.sort_values(by='x', ascending=True)

# 1.5. Wykonaj podstawową wizualizację: utwórz wykres zależności y(x).
plt.figure(figsize=(10, 8))
plt.plot(df['x'], df['y'], marker='o', linestyle='-')
#sns.lineplot(data=df, x='x', y='y', marker='o')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Wykres zależności y od x')
plt.grid(True)
plt.show()

# 3.1. Zadeklaruj dwuwymiarową tablicę ndarray o wymiarach 4x5. Uzupełnij ją
# wybranymi liczbami całkowitymi.
array = np.array([[1,  2,  3,  4,  5],
                  [6,  7,  8,  9, 10],
                  [11, 12, 13, 14, 15],
                  [16, 17, 18, 19, 20]])

# 3.2. Zadeklaruj zmienną przechowującą element z tablicy, który znajduje się
# w drugim wierszu w kolumnie 5. 
element_3_2 = array[1, 4]
print("3.2 Element w 2. wierszu, 5. kolumnie:", element_3_2)

# 3.3. Zadeklaruj zmienną przechowującą element z tablicy, który znajduje się
#w trzecim wierszu w kolumnie 3. Wybierz element wykorzystując numerację
#ujemną.
element_3_3 = array[-2, -3]
print("3.3 Element w 3. wierszu, 3. kolumnie (ujemna numeracja):", element_3_3)

# 3.4. Zadeklaruj zmienną przechowującą cały drugi wiersza tablicy
wiersz_drugi = array[1, :]
print("3.4 Drugi wiersz:", wiersz_drugi)

# 3.5. Zadeklaruj zmienną przechowującą całą czwartą kolumnę tablicy
kolumna_czwarta = array[:, 3]
print("3.5 Czwarta kolumna:", kolumna_czwarta)

# 3.6. Zadeklaruj zmienną przechowującą ostatnie 3 elementy wiersza
#pierwszego
ostatnie_trzy = array[0, -3:]
print("3.6 Ostatnie 3 elementy pierwszego wiersza:", ostatnie_trzy)

# 3.7. Zadeklaruj zmienną przechowującą pierwsze 2 elementy kolumny drugiej
pierwsze_dwa = array[:2, 1]
print("3.7 Pierwsze 2 elementy drugiej kolumny:", pierwsze_dwa)

# 3.8. Zadeklaruj zmienną przechowującą obszar obejmujący wiersz drugi i trzeci
#oraz kolumnę czwartą i piątą
obszar = array[1:3, 3:5]
print("3.8 Obszar (2. i 3. wiersz, 4. i 5. kolumna):")
print(obszar)

# 3.9. Zadeklaruj zmienną przechowującą wszystkie nieparzyste wiersze tablicy
nieparzyste_wiersze = array[[0, 2], :]
print("3.9 Wszystkie nieparzyste wiersze:")
print(nieparzyste_wiersze)
