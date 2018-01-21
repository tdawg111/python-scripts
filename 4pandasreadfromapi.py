import pandas as pd
import quandl

# read api key from text file
api_key = open('quandlapikey.txt', 'r').read()

# codes can be found on the quandl website
df = quandl.get('FMAC/HPI_TX', authtokem = api_key)
print(df.head())

# create a list of dataframes from a webpage
us_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
print(us_states[0])

# iterate through the first dataframe, the first column, starting from the second row
for abbv in us_states[0][0][1:]:
    #print(abbv)
    print('FMAC/HPI_' + abbv)
