import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

df.plot()

df.plot(kind = 'scatter', x = 'Duration', y = 'Calories')

# A histogram needs only one column.

# A histogram shows us the frequency of each interval,
# e.g. how many workouts lasted between 50 and 60 minutes?
df["Duration"].plot(kind = 'hist')
plt.show()