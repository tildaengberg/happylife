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

# plot bar graph
economy_mean_2019 = data_2019["Economy"].mean()
health_mean_2019 = data_2019["Health"].mean()
freedom_mean_2019 = data_2019["Freedom"].mean()
generosity_mean_2019 = data_2019["Generosity"].mean()
corruption_mean_2019 = data_2019["Absence of corruption"].mean()

# plot bar graph
economy_mean_2018 = data_2018["Economy"].mean()
health_mean_2018 = data_2018["Health"].mean()
freedom_mean_2018 = data_2018["Freedom"].mean()
generosity_mean_2018 = data_2018["Generosity"].mean()
corruption_mean_2018 = data_2018["Absence of corruption"].mean()

# plot bar graph
economy_mean_2017 = data_2017["Economy"].mean()
health_mean_2017 = data_2017["Health"].mean()
freedom_mean_2017 = data_2017["Freedom"].mean()
generosity_mean_2017 = data_2017["Generosity"].mean()
corruption_mean_2017 = data_2017["Absence of corruption"].mean()

# plot bar graph
economy_mean_2016 = data_2016["Economy"].mean()
health_mean_2016 = data_2016["Health"].mean()
freedom_mean_2016 = data_2016["Freedom"].mean()
generosity_mean_2016 = data_2016["Generosity"].mean()
corruption_mean_2016 = data_2016["Absence of corruption"].mean()

# plot bar graph
economy_mean_2015 = data_2015["Economy"].mean()
health_mean_2015 = data_2015["Health"].mean()
freedom_mean_2015 = data_2015["Freedom"].mean()
generosity_mean_2015 = data_2015["Generosity"].mean()
corruption_mean_2015 = data_2015["Absence of corruption"].mean()

# assignment starts here
economy_tot = [economy_mean_2015, economy_mean_2016, economy_mean_2017, economy_mean_2018, economy_mean_2019]
health_tot = [health_mean_2015, health_mean_2016, health_mean_2017, health_mean_2018, health_mean_2019]
freedom_tot = [freedom_mean_2015, freedom_mean_2016, freedom_mean_2017, freedom_mean_2018, freedom_mean_2019]
generosity_tot = [generosity_mean_2015, generosity_mean_2016, generosity_mean_2017, generosity_mean_2018, generosity_mean_2019]
corruption_tot = [corruption_mean_2015, corruption_mean_2016, corruption_mean_2017, corruption_mean_2018, corruption_mean_2019]
  
N = 5
ind = np.arange(N) 
width = 0.15

bar1 = plt.bar(ind, economy_tot, width, color = '#83B692')
bar2 = plt.bar(ind+width, health_tot, width, color = '#F9ADA0')
bar3 = plt.bar(ind+width*2, freedom_tot, width, color = '#F9627D')
bar4 = plt.bar(ind+width*3, generosity_tot, width, color = '#C65B7C')
bar5 = plt.bar(ind+width*4, corruption_tot, width, color = '#5B3758')
  
plt.xlabel("Year")
plt.ylabel('Contribution to happiness')
plt.title("The factors impact over time")
  
plt.xticks(ind+width,['2015','2016','2017','2018', '2019'])
plt.legend( (bar1, bar2, bar3, bar4, bar5), ('Economy', 'Health', 'Freedom', 'Generosity', 'Absence of corruption') )
plt.show()