## 3. Populations and Samples ##

question1 = 'population'
question2 = 'population'
question3 = 'sample'
question4 = 'population'
question5 = 'sample'

## 4. Sampling Error ##

import pandas as pd
wnba = pd.read_csv('wnba.csv')


parameter = wnba['Games Played'].max()
sample = wnba['Games Played'].sample(30, random_state = 1)
statistic = sample.max()
sampling_error = parameter - statistic

## 5. Simple Random Sampling ##

import pandas as pd
import matplotlib.pyplot as plt

wnba = pd.read_csv('wnba.csv')


sample_means = []
population_mean = wnba['PTS'].mean()

for i in range(100):
    sample = wnba['PTS'].sample(10, random_state=i)
    sample_means.append(sample.mean())

plt.scatter(range(1,101), sample_means)
plt.axhline(population_mean)
plt.show()

## 7. Stratified Sampling ##

wnba['Pts_per_game'] = wnba['PTS'] / wnba['Games Played']

# Stratifying the data in five strata
stratum_G = wnba[wnba.Pos == 'G']
stratum_F = wnba[wnba.Pos == 'F']
stratum_C = wnba[wnba.Pos == 'C']
stratum_GF = wnba[wnba.Pos == 'G/F']
stratum_FC = wnba[wnba.Pos == 'F/C']

points_per_position = {}
for stratum, position in [(stratum_G, 'G'), (stratum_F, 'F'), (stratum_C, 'C'),
                (stratum_GF, 'G/F'), (stratum_FC, 'F/C')]:
    
    sample = stratum['Pts_per_game'].sample(10, random_state = 0) # simple random sampling on each stratum
    points_per_position[position] = sample.mean()
    
position_most_points = max(points_per_position, key = points_per_position.get)

## 8. Proportional Stratified Sampling ##

# Q1: 
# Make a copy of the wnba DataFrame (wnba_pro_strat_samp) - this is not actually used in the code.
# Create stratum labels for the different intervals of games played.
strata_labels = ['under_12', 'btw_13_22', 'over_23']

# Create a new column in the wnba DataFrame indicating the stratum each 
# player belongs to based on the number of games played.
# The intervals are (-1, 12], (12, 22], and (22, max(Games Played)].
wnba['Games Played Interval'] = pd.cut(
                    wnba['Games Played'],
                    bins=[-1, 12, 22, wnba['Games Played'].max()], 
                    labels=strata_labels
)

# Group the players by their respective stratum.
stratified_group = wnba.groupby(by='Games Played Interval')

# Create an empty dictionary to store the group DataFrames.
group_dict = {}

# Loop through the stratum groups and create a DataFrame for each stratum.
for group_name, group_df in stratified_group:
    
    # create a DataFrame for the group
    group_df = pd.DataFrame(group_df)
    
    # add the group DataFrame to the dictionary
    group_dict[group_name] = group_df

# Count the number of players in each stratum for each position group
# This will be used to calculate the sample size for each stratum.
group_totals = stratified_group['Games Played Interval'].count()

# Calculate the sample size for each stratum based on its proportion of the 
# total number of players and a total sample size of 10.
stratum_sample_size = (round(group_totals / group_totals.sum(), 1)).tolist()
ss = [int(x * 10) for x in stratum_sample_size]


# Q2:
# Create an empty list to store the means of the samples generated in the loop.
proportional_sampling_means = []

# Loop through the random sampling process 100 times.
for i in range(100):
    # Take random samples from each stratum based on the sample size 
    # calculated above and a given seed.
    sample_under_12 = group_dict[strata_labels[0]]['PTS'].sample(ss[0], random_state=i)
    sample_btw_13_22 = group_dict[strata_labels[1]]['PTS'].sample(ss[1], random_state=i)
    sample_over_23 = group_dict[strata_labels[2]]['PTS'].sample(ss[2], random_state=i)
    
    # Concatenate the samples into one final sample.
    final_sample = pd.concat([sample_under_12, sample_btw_13_22, sample_over_23])
    
    # Append the mean of the final sample to the list of means.
    proportional_sampling_means.append(final_sample.mean())
    
    
# Plot the means of the samples against the number of times the 
# mrandom sampling process was performed.
plt.scatter(range(1,101), proportional_sampling_means)
plt.axhline(wnba['PTS'].mean())
plt.show()

## 10. Cluster Sampling ##

clusters = pd.Series(wnba['Team'].unique()).sample(4, random_state = 0)

sample = pd.DataFrame()

for cluster in clusters:
    data_collected = wnba[wnba['Team'] == cluster]
    sample = sample.append(data_collected)

sampling_error_height = wnba['Height'].mean() - sample['Height'].mean()
sampling_error_age = wnba['Age'].mean() - sample['Age'].mean()
sampling_error_BMI = wnba['BMI'].mean() - sample['BMI'].mean()
sampling_error_points = wnba['PTS'].mean() - sample['PTS'].mean()