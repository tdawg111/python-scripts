import pandas as pd

df = pd.read_csv('WGEM-ZAF_CPTOTSAXNZGY.csv') # create dataframe from csv
print(df.head())
#df.set_index('Date', inplace = True)

# write out dataframe to csv
#df.to_csv('newcsv2.csv')

# write out one column of the dataframe to csv
#df['Value'].to_csv('newcsv2.csv')

# create dataframe from csv and set the index to the first column
df = pd.read_csv('WGEM-ZAF_CPTOTSAXNZGY.csv', index_col = 0)
print(df.head())

df.columns = ['Inflation rate'] # rename all columns in dataframe
print(df.head())

df.to_csv('newcsv4.csv', header = False) # save to csv with no headers
# read csv with no headers, set column names and set index column
df = pd.read_csv('newcsv4.csv', names = ['Date', 'Inflation rate'], index_col = 0)
print(df.head())

df.to_html('example.html') # write out dataframe to an html file

# rename just one column in the dataframe
df.rename(columns = {'Inflation rate': 'Inflation %'}, inplace = True)
print(df.head())
