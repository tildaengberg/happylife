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
                             'Health (Life Expectancy)': 'Health', 'Trust (Government Corruption)': 'Absence of corruption'})
data_2016 = data_2016.rename(columns={'Happiness Rank': 'Rank', 'Happiness Score': 'Score', 'Economy (GDP per Capita)': 'Economy',
                             'Health (Life Expectancy)': 'Health', 'Trust (Government Corruption)': 'Absence of corruption'})
data_2017 = data_2017.rename(columns={'Happiness.Rank': 'Rank', 'Happiness.Score': 'Score', 'Economy..GDP.per.Capita.': 'Economy',
                             'Health..Life.Expectancy.': 'Health', 'Trust..Government.Corruption.': 'Absence of corruption'})
data_2018 = data_2018.rename(columns={'Overall rank': 'Rank', 'Country or region': 'Country', 'GDP per capita': 'Economy',
                             'Healthy life expectancy': 'Health', 'Freedom to make life choices': 'Freedom', 'Perceptions of corruption':  'Absence of corruption'})
data_2019 = data_2019.rename(columns={'Overall rank': 'Rank', 'Country or region': 'Country', 'GDP per capita': 'Economy',
                             'Healthy life expectancy': 'Health', 'Freedom to make life choices': 'Freedom', 'Perceptions of corruption': 'Absence of corruption'})

# sort columns
column_titles = ["Country", "Rank", "Score", "Economy",
                 "Health", "Freedom", "Generosity", "Absence of corruption"]
data_2015 = data_2015.reindex(columns=column_titles)
data_2016 = data_2016.reindex(columns=column_titles)
data_2017 = data_2017.reindex(columns=column_titles)
data_2018 = data_2018.reindex(columns=column_titles)
data_2019 = data_2019.reindex(columns=column_titles)
