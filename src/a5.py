import pandas as pd
import matplotlib.pyplot as plt
from sklearn import preprocessing
import numpy as np
import geopandas as gpd
import plotly.express as px

# read files
data_2015 = pd.read_csv('data/2015.csv')
data_2016 = pd.read_csv('data/2016.csv')
data_2017 = pd.read_csv('data/2017.csv')
data_2018 = pd.read_csv('data/2018.csv')
data_2019 = pd.read_csv('data/2019.csv')
country_coordinates = pd.read_csv('data/country-coord.csv')

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

# modify data to find max values for each row in dataset
mod_2019 = data_2019.drop(["Rank", "Score", "Country"], axis=1)

# find max values
max_values = mod_2019.max(axis=1)

# find the corresponding factors to each countries
factors = mod_2019.idxmax(axis=1)

# create new dataframe with country, max value and factor
df = pd.DataFrame({'Country': data_2019["Country"],
                   'Max value': max_values,
                   'Factor': factors
                   })

# read geojson file
gdf_original = gpd.read_file('data/countries.geojson')

# rename column in geojson file
gdf = gdf_original.rename(
    columns={'ADMIN': 'Country'})

# merge the two datasets where the countries match
merged_df = gdf.merge(df, on="Country")

# plot the world map
fig = px.choropleth(merged_df,
                    geojson=merged_df.geometry,
                    locations=merged_df.index,
                    color="Factor",
                    projection="natural earth",
                    hover_name="Country",
                    title="Most important factor for happiness",
                    color_discrete_map={'Health': '#83B692',
                                        'Economy': '#F9627D',
                                        'Generosity': '#F9ADA0',
                                        'Freedom': '#5B3758'})
fig.show()
