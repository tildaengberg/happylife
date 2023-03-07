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

# Plot original dataset
fig2, ax2 = plt.subplots()

economy_plot = ax2.scatter(
    data_2019["Economy"], data_2019["Score"], c='#83B692')
health_plot = ax2.scatter(
    data_2019["Health"], data_2019["Score"], c='#F9ADA0')
freedom_plot = ax2.scatter(
    data_2019["Freedom"], data_2019["Score"], c='#F9627D')
generosity_plot = ax2.scatter(
    data_2019["Generosity"], data_2019["Score"], c='#C65B7C')
corruption_plot = ax2.scatter(
    data_2019["Corruption"], data_2019["Score"], c='#5B3758')

ax2.set_xlabel(
    "The extent to which the factor contributes to the happines score")
ax2.set_ylabel("Happiness score")
ax2.legend((economy_plot, health_plot, freedom_plot, generosity_plot,
           corruption_plot), ('Economy', 'Health', 'Freedom', 'Generosity', 'Corruption'))
ax2.set_title("Happiness scatter plot 2019")

plt.show()
