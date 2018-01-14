import pandas as pd
import datetime
import pandas_datareader.data as web
import matplotlib.pyplot as plt
from matplotlib import style

style.use('seaborn') # the style to use for graph plotting

start = datetime.datetime(2017, 1, 1)
end = datetime.datetime.now()

# You will need to find your own API to pull finance data from
df = web.DataReader("DIVTRX", "google", start, end)

# Print the dataframe to console.
#print(df)
print(df.head()) # prints the first 5 rows
#print(df.tail(10)) # prints the last 10 rows

# Plot the graph using the data from the dataframe
#df[['Open', 'Close']].plot() # list the columns to plot
#plt.legend() # display the legend
#plt.show() # display the graph on screen
