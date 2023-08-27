## 2. Bar Plots ##

import matplotlib.pyplot as plt

wnba['Exp_ordinal'].value_counts().iloc[[3,0,2,1,4]].plot.bar()
plt.show()

## 3. Horizontal Bar Plots ##

# freqy table for Exp_ordinal
Exp_ordinal_ft = wnba['Exp_ordinal'].value_counts().iloc[[3,0,2,1,4]]

Exp_ordinal_ft.plot.barh(title = 'Number of players in WNBA by level of experience')
plt.show()

## 4. Pie Charts ##

wnba['Exp_ordinal'].value_counts().plot.pie()
plt.show()

## 5. Customizing a Pie Chart ##

wnba['Exp_ordinal'].value_counts().plot.pie(figsize = (6,6), 
                                            autopct = '%.2f%%'
                                           )
plt.title('Percentage of players in WNBA by level of experience')
plt.ylabel('')
plt.show()

## 6. Histograms ##

wnba['PTS'].plot.hist()
plt.show()

## 7. The Statistics Behind Histograms ##

wnba['Games Played'].plot.hist()
plt.show()

## 9. Binning for Histograms ##

wnba['Games Played'].plot.hist(range = (1,32), bins = 8,
                               title = 'The distribution of players by games played')
plt.xlabel('Games played')
plt.show()

## 10. Skewed Distributions ##

assists_distro = 'right skewed'
ft_percent_distro = 'left skewed'

## 11. Symmetrical Distributions ##

axs = wnba[['Age', 'Height', 'MIN']].hist(layout=(2, 2), figsize=(10, 5), bins=15)
plt.show()
normal_distribution = 'Height'