import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_excel('tests/musicTimes.xlsx')

print(df.describe())

descriptiveStats = {
    "Mean": [194.23, 260.73, 252.67, 196.93, 176.90],
    "Median": [187.00, 267.50, 247.00, 193.50, 166.00],
    "S.D": [39.36, 81.04, 54.01, 22.64, 55.10]
}
df = pd.DataFrame(descriptiveStats, index = ['Pop', 'Metal', 'Grunge',
                                            'Country', 'Rap'])

print(df)


#x = np.array(['Pop','Metal','Grunge','Country','Rap'])
#y = np.array([39.36, 81.04, 54.01, 22.64, 55.1])
df['S.D'].plot(kind = 'bar')
plt.title('Genre Standard Deviations')
plt.ylabel('Seconds')
plt.show()

df['Mean'].plot(kind = 'bar')
plt.title('Mean Song Length')
plt.ylabel('Seconds')
plt.show()

df['Median'].plot(kind = 'bar')
plt.title('Median Song Length')
plt.ylabel('Seconds')
plt.show()