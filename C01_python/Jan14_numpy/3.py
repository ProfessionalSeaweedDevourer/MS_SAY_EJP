import numpy as np
import pandas as pd

subway = pd.read_csv('C01_python/Jan14_numpy/subway.csv', encoding='utf-8')

print(subway.head())

# '적자'인 역: 승차인원 (5열) < 하차인원 (6열)
mask = subway.iloc[:, 5] < subway.iloc[:, 6]
print(subway[mask])

