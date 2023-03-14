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

# Get the average of each year
average_economy_2015 = data_2015["Economy"].mean()
average_economy_2016 = data_2016["Economy"].mean()
average_economy_2017 = data_2017["Economy"].mean()
average_economy_2018 = data_2018["Economy"].mean()
average_economy_2019 = data_2019["Economy"].mean()

average_health_2015 = data_2015["Health"].mean()
average_health_2016 = data_2016["Health"].mean()
average_health_2017 = data_2017["Health"].mean()
average_health_2018 = data_2018["Health"].mean()
average_health_2019 = data_2019["Health"].mean()

average_freedom_2015 = data_2015["Freedom"].mean()
average_freedom_2016 = data_2016["Freedom"].mean()
average_freedom_2017 = data_2017["Freedom"].mean()
average_freedom_2018 = data_2018["Freedom"].mean()
average_freedom_2019 = data_2019["Freedom"].mean()

average_generosity_2015 = data_2015["Generosity"].mean()
average_generosity_2016 = data_2016["Generosity"].mean()
average_generosity_2017 = data_2017["Generosity"].mean()
average_generosity_2018 = data_2018["Generosity"].mean()
average_generosity_2019 = data_2019["Generosity"].mean()

average_corruption_2015 = data_2015["Corruption"].mean()
average_corruption_2016 = data_2016["Corruption"].mean()
average_corruption_2017 = data_2017["Corruption"].mean()
average_corruption_2018 = data_2018["Corruption"].mean()
average_corruption_2019 = data_2019["Corruption"].mean()

# Plot the graphs in the same window
figure, axis = plt.subplots(2, 3)
figure.tight_layout(pad=2.0)
X = [2015, 2016, 2017, 2018, 2019]

Y1 = [average_economy_2015, average_economy_2016,
      average_economy_2017, average_economy_2018, average_economy_2019]
axis[0, 0].plot(X, Y1)
axis[0, 0].set_title("Economy")
axis[0, 0].set_ylim([0, 1])
axis[0, 0].set_ylabel("Contribution to happines score")
axis[0, 0].set_xlabel("Year")

Y2 = [average_health_2015, average_health_2016,
      average_health_2017, average_health_2018, average_health_2019]
axis[0, 1].plot(X, Y2)
axis[0, 1].set_title("Health")
axis[0, 1].set_ylim([0, 1])
axis[0, 1].set_ylabel("Contribution to happines score")
axis[0, 1].set_xlabel("Year")

Y3 = [average_freedom_2015, average_freedom_2016,
      average_freedom_2017, average_freedom_2018, average_freedom_2019]
axis[0, 2].plot(X, Y3)
axis[0, 2].set_title("Freedom")
axis[0, 2].set_ylim([0, 1])
axis[0, 2].set_ylabel("Contribution to happines score")
axis[0, 2].set_xlabel("Year")

Y4 = [average_generosity_2015, average_generosity_2016,
      average_generosity_2017, average_generosity_2018, average_generosity_2019]
axis[1, 0].plot(X, Y4)
axis[1, 0].set_title("Generosity")
axis[1, 0].set_ylim([0, 1])
axis[1, 0].set_ylabel("Contribution to happines score")
axis[1, 0].set_xlabel("Year")

Y5 = [average_corruption_2015, average_corruption_2016,
      average_corruption_2017, average_corruption_2018, average_corruption_2019]
axis[1, 1].plot(X, Y5)
axis[1, 1].set_title("Corruption")
axis[1, 1].set_ylim([0, 1])
axis[1, 1].set_ylabel("Contribution to happines score")
axis[1, 1].set_xlabel("Year")

plt.show()
