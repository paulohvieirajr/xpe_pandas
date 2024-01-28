import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./california_housing_test.csv')
df.plot(x='longitude', y='latitude', kind='bar')
plt.show()
