import pandas as pd
import datetime
import pandas_datareader.data as web
import matplotlib.pyplot as plt
from matplotlib import style

style.use('seaborn')

start = datetime.datetime(2017, 1, 1)
end = datetime.datetime.now()

df = web.DataReader("DIVTRX", "google", start, end)

print(df.tail(10))
df[['Open', 'Close']].plot()
plt.legend()
plt.show()
