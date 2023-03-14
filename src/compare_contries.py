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
luxembourg_2019 = data_2019.loc[data_2019['Country']
                                == 'Luxembourg', 'Score'].item()
luxembourg_2018 = data_2018.loc[data_2018['Country']
                                == 'Luxembourg', 'Score'].item()
luxembourg_2017 = data_2017.loc[data_2017['Country']
                                == 'Luxembourg', 'Score'].item()
luxembourg_2016 = data_2016.loc[data_2016['Country']
                                == 'Luxembourg', 'Score'].item()
luxembourg_2015 = data_2015.loc[data_2015['Country']
                                == 'Luxembourg', 'Score'].item()

burundi_2019 = data_2019.loc[data_2019['Country'] == 'Burundi', 'Score'].item()
burundi_2018 = data_2018.loc[data_2018['Country'] == 'Burundi', 'Score'].item()
burundi_2017 = data_2017.loc[data_2017['Country'] == 'Burundi', 'Score'].item()
burundi_2016 = data_2016.loc[data_2016['Country'] == 'Burundi', 'Score'].item()
burundi_2015 = data_2015.loc[data_2015['Country'] == 'Burundi', 'Score'].item()


data1 = {'Score': [luxembourg_2015, luxembourg_2016, luxembourg_2017,
                   luxembourg_2018, luxembourg_2019], 'Year': ['2015', '2016', '2017', '2018', '2019']}
data_luxembourg = pd.DataFrame(data1)

data2 = {'Score': [burundi_2015, burundi_2016, burundi_2017, burundi_2018,
                   burundi_2019], 'Year': ['2015', '2016', '2017', '2018', '2019']}
data_burundi = pd.DataFrame(data2)

data3 = {'Score': [data_2015['Score'].mean(), data_2016['Score'].mean(), data_2017['Score'].mean(
), data_2018['Score'].mean(), data_2019['Score'].mean()], 'Year': ['2015', '2016', '2017', '2018', '2019']}
data_mean = pd.DataFrame(data3)

plt.plot(data_luxembourg['Year'], data_luxembourg['Score'],
         label='Luxembourg', color='#F9627D')
plt.plot(data_burundi['Year'], data_burundi['Score'],
         label='Burundi', color='#5B3758')
plt.plot(data_mean['Year'], data_mean['Score'],
         label='Mean', linestyle="--", color='grey')
plt.ylim((0, 10))
plt.ylabel("Happiness score")
plt.xlabel("Year")

plt.legend()

# test

plt.show()


# luxembourg is the richest country while burundi is the poorest
