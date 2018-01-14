import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style

web_stats = {'Day':[1,2,3,4,5,6],
             'Visitors':[43,34,65,56,29,76],
             'Bounce Rate':[65,67,78,65,45,52]}

df = pd.DataFrame(web_stats) # create dataframe from dictionary
# set the dataframe index to be the day and replace the dataframe inplace
df.set_index('Day', inplace=True)

print(df.head())
# print a specific column in the dataframe
print(df['Visitors'])
#print(df.Visitors)
# print multiple columns in the dataframe
#print(df[['Visitors', 'Bounce Rate']])

style.use('fivethirtyeight')
df.plot()
plt.show()
