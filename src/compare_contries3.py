import pandas as pd
import matplotlib.pyplot as plt
from sklearn import preprocessing
import numpy as np

# read files
data_2015 = pd.read_csv('data/2015.csv')
data_2016 = pd.read_csv('data/2016.csv')
data_2017 = pd.read_csv('data/2017.csv')
data_2018 = pd.read_csv('data/2018.csv')
data_2019 = pd.read_csv('data/2019.csv')

# drop NA values
data_2015 = data_2015.dropna()
data_2016 = data_2016.dropna()
data_2017 = data_2017.dropna()
data_2018 = data_2018.dropna()
data_2019 = data_2019.dropna()

# clean tables from unnecessary cloumns
data_2015.drop(["Region", "Standard Error", "Family",
               "Dystopia Residual"], axis=1, inplace=True)
data_2016.drop(["Region", "Lower Confidence Interval", "Upper Confidence Interval",
               "Family", "Dystopia Residual"], axis=1, inplace=True)
data_2017.drop(["Whisker.high", "Whisker.low", "Family",
               "Dystopia.Residual"], axis=1, inplace=True)
data_2018.drop(["Social support"], axis=1, inplace=True)
data_2019.drop(["Social support"], axis=1, inplace=True)

# rename column labels
data_2015 = data_2015.rename(columns={'Happiness Rank': 'Rank', 'Happiness Score': 'Score', 'Economy (GDP per Capita)': 'Economy',
                             'Health (Life Expectancy)': 'Health', 'Trust (Government Corruption)': 'Corruption'})
data_2016 = data_2016.rename(columns={'Happiness Rank': 'Rank', 'Happiness Score': 'Score', 'Economy (GDP per Capita)': 'Economy',
                             'Health (Life Expectancy)': 'Health', 'Trust (Government Corruption)': 'Corruption'})
data_2017 = data_2017.rename(columns={'Happiness.Rank': 'Rank', 'Happiness.Score': 'Score', 'Economy..GDP.per.Capita.': 'Economy',
                             'Health..Life.Expectancy.': 'Health', 'Trust..Government.Corruption.': 'Corruption'})
data_2018 = data_2018.rename(columns={'Overall rank': 'Rank', 'Country or region': 'Country', 'GDP per capita': 'Economy',
                             'Healthy life expectancy': 'Health', 'Freedom to make life choices': 'Freedom', 'Perceptions of corruption':  'Corruption'})
data_2019 = data_2019.rename(columns={'Overall rank': 'Rank', 'Country or region': 'Country', 'GDP per capita': 'Economy',
                             'Healthy life expectancy': 'Health', 'Freedom to make life choices': 'Freedom', 'Perceptions of corruption': 'Corruption'})

# sort columns
column_titles = ["Country", "Rank", "Score", "Economy",
                 "Health", "Freedom", "Generosity", "Corruption"]
data_2015 = data_2015.reindex(columns=column_titles)
data_2016 = data_2016.reindex(columns=column_titles)
data_2017 = data_2017.reindex(columns=column_titles)
data_2018 = data_2018.reindex(columns=column_titles)
data_2019 = data_2019.reindex(columns=column_titles)

# the assignment starts here
minvalue2015 = data_2015['Score'].min()
minvalueindex2015 = data_2015['Score'].idxmin()

minvalue2016 = data_2016['Score'].min()
minvalueindex2016 = data_2016['Score'].idxmin()

minvalue2017 = data_2017['Score'].min()
minvalueindex2017 = data_2017['Score'].idxmin()

minvalue2018 = data_2018['Score'].min()
minvalueindex2018 = data_2018['Score'].idxmin()

minvalue2019 = data_2019['Score'].min()
minvalueindex2019 = data_2019['Score'].idxmin()

maxvalue2015 = data_2015['Score'].max()
maxvalueindex2015 = data_2015['Score'].idxmax()

maxvalue2016 = data_2016['Score'].max()
maxvalueindex2016 = data_2016['Score'].idxmax()

maxvalue2017 = data_2017['Score'].max()
maxvalueindex2017 = data_2017['Score'].idxmax()

maxvalue2018 = data_2018['Score'].max()
maxvalueindex2018 = data_2018['Score'].idxmax()

maxvalue2019 = data_2019['Score'].max()
maxvalueindex2019 = data_2019['Score'].idxmax()

print(   )
print(   )
print('The least happy country 2015 was: ', data_2015['Country'].iloc[minvalueindex2015])
print('The least happy country 2016 was: ', data_2015['Country'].iloc[minvalueindex2016])
print('The least happy country 2017 was: ', data_2015['Country'].iloc[minvalueindex2017])
print('The least happy country 2018 was: ', data_2015['Country'].iloc[minvalueindex2018])
print('The least happy country 2019 was: ', data_2015['Country'].iloc[minvalueindex2019])
print(   )
print('The happiest country 2015 was: ', data_2015['Country'].iloc[maxvalueindex2015])
print('The happiest country 2016 was: ', data_2015['Country'].iloc[maxvalueindex2016])
print('The happiest country 2017 was: ', data_2015['Country'].iloc[maxvalueindex2017])
print('The happiest country 2018 was: ', data_2015['Country'].iloc[maxvalueindex2018])
print('The happitest country 2019 was: ', data_2015['Country'].iloc[maxvalueindex2019])
print(   )
print(   )


gdp = pd.read_csv('data/gdp_ppp_per_capita.csv')

switzerland_2019 = gdp.loc[gdp['Country Name'] == 'Switzerland', '2019'].item()
switzerland_2018 = gdp.loc[gdp['Country Name'] == 'Switzerland', '2018'].item()
switzerland_2017 = gdp.loc[gdp['Country Name'] == 'Switzerland', '2017'].item()
switzerland_2016 = gdp.loc[gdp['Country Name'] == 'Switzerland', '2016'].item()
switzerland_2015 = gdp.loc[gdp['Country Name'] == 'Switzerland', '2015'].item()

data1 = {'Score':[switzerland_2015,switzerland_2016,switzerland_2017,switzerland_2018,switzerland_2019], 'Year':['2015', '2016', '2017', '2018', '2019']}
data_switzerland = pd.DataFrame(data1)

benin_2019 = gdp.loc[gdp['Country Name'] == 'Benin', '2019'].item()
benin_2018 = gdp.loc[gdp['Country Name'] == 'Benin', '2018'].item()
benin_2017 = gdp.loc[gdp['Country Name'] == 'Benin', '2017'].item()
benin_2016 = gdp.loc[gdp['Country Name'] == 'Benin', '2016'].item()
benin_2015 = gdp.loc[gdp['Country Name'] == 'Benin', '2015'].item()

data2 = {'Score':[benin_2015,benin_2016,benin_2017,benin_2018,benin_2019], 'Year':['2015', '2016', '2017', '2018', '2019']}
data_benin = pd.DataFrame(data2)

togo_2019 = gdp.loc[gdp['Country Name'] == 'Togo', '2019'].item()
togo_2018 = gdp.loc[gdp['Country Name'] == 'Togo', '2018'].item()
togo_2017 = gdp.loc[gdp['Country Name'] == 'Togo', '2017'].item()
togo_2016 = gdp.loc[gdp['Country Name'] == 'Togo', '2016'].item()
togo_2015 = gdp.loc[gdp['Country Name'] == 'Togo', '2015'].item()

data3 = {'Score':[togo_2015,togo_2016,togo_2017,togo_2018,togo_2019], 'Year':['2015', '2016', '2017', '2018', '2019']}
data_togo = pd.DataFrame(data3)

burundi_2019 = gdp.loc[gdp['Country Name'] == 'Burundi', '2019'].item()
burundi_2018 = gdp.loc[gdp['Country Name'] == 'Burundi', '2018'].item()
burundi_2017 = gdp.loc[gdp['Country Name'] == 'Burundi', '2017'].item()
burundi_2016 = gdp.loc[gdp['Country Name'] == 'Burundi', '2018'].item()
burundi_2015 = gdp.loc[gdp['Country Name'] == 'Burundi', '2019'].item()

data4 = {'Score':[burundi_2015,burundi_2016,burundi_2017,burundi_2018,burundi_2019], 'Year':['2015', '2016', '2017', '2018', '2019']}
data_burundi = pd.DataFrame(data4)


plt.plot(data_switzerland['Year'], data_switzerland['Score'], label = 'Switzerland')
plt.plot(data_benin['Year'], data_benin['Score'], label = 'Benin')
plt.plot(data_togo['Year'], data_togo['Score'], label = 'Togo')
plt.plot(data_burundi['Year'], data_burundi['Score'], label = 'Burundi')

#plt.ylim((0,10))
plt.legend()
plt.show()


