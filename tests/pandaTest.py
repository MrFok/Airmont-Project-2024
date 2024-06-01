import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_excel('tests/musicTimes.xlsx')  
#creating data frame of excel sheet with song lengths
print(df.describe()) 

df.describe().to_csv('descriptiveStats.csv', index=True) 
#outputting the data from the describe function to a csv file

df = pd.read_csv('descriptiveStats.csv') 
#creating data frame from the csv file

df.set_index(df.columns[0], inplace=True)
#setting data frame index to the 0th column 

mean_values = df.loc['mean']
std_values = df.loc['std']
median_values = df.loc['50%']

plt.bar(mean_values.index, mean_values.values, color='blue')
plt.xlabel('Music Genres')
plt.ylabel('Average Song Length')
plt.show()

plt.bar(std_values.index, std_values.values, color='purple')
plt.xlabel('Music Genres')
plt.ylabel('Standard Deviation')
plt.show()

plt.bar(median_values.index, median_values.values, color='orange')
plt.xlabel('Music Genres')
plt.ylabel('Median Song Length')
plt.show()

# descriptiveStats = {
#     "Mean": [194.23, 260.73, 252.67, 196.93, 176.90],
#     "Median": [187.00, 267.50, 247.00, 193.50, 166.00],
#     "S.D": [39.36, 81.04, 54.01, 22.64, 55.10]
# }
# df = pd.DataFrame(descriptiveStats, index = ['Pop', 'Metal', 'Grunge',
#                                             'Country', 'Rap'])

# print(df)


# #x = np.array(['Pop','Metal','Grunge','Country','Rap'])
# #y = np.array([39.36, 81.04, 54.01, 22.64, 55.1])
# df['S.D'].plot(kind = 'bar')
# plt.title('Genre Standard Deviations')
# plt.ylabel('Seconds')
# plt.show()

# df['Mean'].plot(kind = 'bar')
# plt.title('Mean Song Length')
# plt.ylabel('Seconds')
# plt.show()

# df['Median'].plot(kind = 'bar')
# plt.title('Median Song Length')
# plt.ylabel('Seconds')
# plt.show()