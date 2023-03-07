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
bhutan_2019 = data_2019.loc[data_2019['Country'] == 'Bhutan', 'Score'].item()
bhutan_2018 = data_2018.loc[data_2018['Country'] == 'Bhutan', 'Score'].item()
bhutan_2017 = data_2017.loc[data_2017['Country'] == 'Bhutan', 'Score'].item()
bhutan_2016 = data_2016.loc[data_2016['Country'] == 'Bhutan', 'Score'].item()
bhutan_2015 = data_2015.loc[data_2015['Country'] == 'Bhutan', 'Score'].item()

nicaragua_2019 = data_2019.loc[data_2019['Country'] == 'Nicaragua', 'Score'].item()
nicaragua_2018 = data_2018.loc[data_2018['Country'] == 'Nicaragua', 'Score'].item()
nicaragua_2017 = data_2017.loc[data_2017['Country'] == 'Nicaragua', 'Score'].item()
nicaragua_2016 = data_2016.loc[data_2016['Country'] == 'Nicaragua', 'Score'].item()
nicaragua_2015 = data_2015.loc[data_2015['Country'] == 'Nicaragua', 'Score'].item()


data1 = {'Score':[bhutan_2015,bhutan_2016,bhutan_2017,bhutan_2018,bhutan_2019], 'Year':['2015', '2016', '2017', '2018', '2019']}
data_bhutan = pd.DataFrame(data1)

data2 = {'Score':[nicaragua_2015,nicaragua_2016,nicaragua_2017,nicaragua_2018,nicaragua_2019], 'Year':['2015', '2016', '2017', '2018', '2019']}
data_nicaragua = pd.DataFrame(data2)

data3 = {'Score':[data_2015['Score'].mean(),data_2016['Score'].mean(),data_2017['Score'].mean(),data_2018['Score'].mean(),data_2019['Score'].mean()], 'Year':['2015', '2016', '2017', '2018', '2019']}
data_mean = pd.DataFrame(data3)

plt.plot(data_bhutan['Year'], data_bhutan['Score'], label = 'Bhutan', color='#83B692')
plt.plot(data_nicaragua['Year'], data_nicaragua['Score'], label = 'Nicaragua', color ='#F9ADA0')
plt.plot(data_mean['Year'], data_mean['Score'], label = 'Mean', linestyle="--", color = 'grey')

plt.ylim((0,10))
plt.legend()
plt.show()


# nicaragua and bhutan is equally rich but differ in corruption