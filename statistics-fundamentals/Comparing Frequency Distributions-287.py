## 2. Grouped Bar Plots ##

import matplotlib.pyplot as plt
plt.figure().set_figwidth(8)


import seaborn as sns
sns.set_theme()
sns.countplot(x = 'Exp_ordinal', hue = 'Pos', data = wnba,
              order = ['Rookie', 'Little experience', 'Experienced', 'Very experienced', 'Veteran'],
              hue_order = ['C', 'F', 'F/C', 'G', 'G/F']
             )
plt.show()

## 3. Challenge: Do Older Players Play Less? ##

sns.set_theme()


sns.countplot(x = 'age_mean_relative', hue = 'min_mean_relative', data = wnba)
plt.show()
result = 'rejection'

## 4. Comparing Histograms ##

wnba[wnba.Age >= 27]['MIN'].plot.hist(histtype = 'step', label = 'Old', legend = True)
wnba[wnba.Age < 27]['MIN'].plot.hist(histtype = 'step', label = 'Young', legend = True)
plt.axvline(497, label = 'Average')
plt.legend()
plt.show()

## 5. Kernel Density Estimate Plots ##

wnba[wnba.Age >= 27]['MIN'].plot.kde(label = 'Old', legend = True)
wnba[wnba.Age < 27]['MIN'].plot.kde(label = 'Young', legend = True)
plt.axvline(497, label = 'Average')
plt.legend()
plt.show()

## 7. Strip Plots ##

sns.set_theme()



sns.stripplot(x = 'Pos', y = 'Weight', data = wnba, jitter = True)
plt.show()

print('''The patterns we see are strikingly similar to those we saw for heights. This can be easily
explained by the fact that there's a strong positive relation between a player's height and her
weight: the taller the player, the heavier she is; the shorter the player, the lighter she is.''')

## 8. Box plots ##

sns.set_theme()

sns.boxplot(x = 'Pos', y = 'Weight', data = wnba)
plt.show()

## 9. Outliers ##

sns.set_theme()
upper_quartile = wnba['Games Played'].describe()['75%']
lower_quartile = wnba['Games Played'].describe()['25%']

# innerquartile range
iqr = upper_quartile - lower_quartile
print('The innerquartile range is: ', iqr)

whis = 1.5

lower_bound = lower_quartile - (iqr * whis)
print('The lower bound is: ', lower_bound)

upper_bound = upper_quartile + (iqr * whis)
print('The upper bound is: ', upper_bound)

outliers_low = sum(wnba['Games Played'] < lower_bound) 
print('The number of lower outliers are: ', outliers_low)

outliers_high = sum(wnba['Games Played'] > upper_bound)
print('The number of upper outliers are: ', outliers_high)

sns.boxplot(wnba['Games Played'])
plt.show()