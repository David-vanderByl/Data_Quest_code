## 2. Introduction to the Data ##

import pandas as pd

happiness2015 = pd.read_csv("World_Happiness_2015.csv")

first_5 = happiness2015.head()
happiness2015.info()

## 3. Using Loops to Aggregate Data ##

# empty dictionary for aggregated data
mean_happiness = {} 

 # this could be done in the first line of the loop
regions = happiness2015["Region"].unique()

# looping over unique regions
for region in regions:
    
    # dataframe of rows of current unique region
    region_group = happiness2015[happiness2015["Region"] == region]
    
    # Calculating the mean happiness of current region
    region_mean = region_group['Happiness Score'].mean()
    
    # Assigning value of mean region happiness to region as key in dictionary
    mean_happiness[region] = region_mean

## 5. Creating GroupBy Objects ##

# Creating a map to group rows by unique region
grouped = happiness2015.groupby("Region")

# Selecting rows of only the Australia and New Zealand region
aus_nz = grouped.get_group("Australia and New Zealand")
aus_nz

## 6. Exploring GroupBy Objects ##

grouped = happiness2015.groupby('Region')


north_america = happiness2015.iloc[[4,14]]
na_group = grouped.get_group('North America')
equal = north_america == na_group

## 7. Common Aggregation Methods with Groupby ##

grouped = happiness2015.groupby('Region')

# Calculating the mean of the grouped regions
means = grouped.mean(numeric_only=True)
means

## 8. Aggregating Specific Columns with Groupby ##

# Creating a map to group rows by unique region
grouped = happiness2015.groupby('Region')

# Selecting only the "Happiness Score" column from the groupedBy region dataframe
happy_grouped = grouped["Happiness Score"]

# Calculating the mean of the happiness score by region
happy_mean = happy_grouped.mean()
happy_mean

## 9. Introduction to the Agg() Method ##

# importing numpy(np) for math functions 
import numpy as np

# Creating a map to group rows by unique region
grouped = happiness2015.groupby('Region')

# Selecting only the "Happiness Score" column from the groupedBy region dataframe
happy_grouped = grouped['Happiness Score']

# Function that calculates the difference between the mean and max values
def dif(group):
    return (group.max() - group.mean())

# Using the mean and max functions with the agg() method
happy_mean_max = happy_grouped.agg([np.mean, np.max])
print(happy_mean_max, '\n')

# using the function created above to get the diff between mean and max
mean_max_dif = happy_grouped.agg(dif)
print(mean_max_dif)

## 11. Aggregation with Pivot Tables ##

pv_happiness = happiness2015.pivot_table(values='Happiness Score', index='Region', aggfunc=np.mean, margins=True)


pv_happiness.plot(kind='barh', xlim=(0,10), title='Mean Happiness Scores by Region', legend=False)
plt.show()
world_mean_happiness = happiness2015['Happiness Score'].mean()

## 12. Aggregating Multiple Columns and Functions with Pivot Tables ##

grouped = happiness2015.groupby('Region')[['Happiness Score','Family']]
happy_family_stats = grouped.agg([np.min, np.max, np.mean])
pv_happy_family_stats = happiness2015.pivot_table(['Happiness Score', 'Family'], 'Region', aggfunc=[np.min, np.max, np.mean], margins=True)