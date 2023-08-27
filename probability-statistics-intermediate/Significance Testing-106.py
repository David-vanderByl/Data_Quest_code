## 3. Statistical Significance ##

import numpy as np
import matplotlib.pyplot as plt
mean_group_a = np.mean(weight_lost_a)
mean_group_b = np.mean(weight_lost_b)

## 4. Test Statistic ##

import numpy as np
import matplotlib.pyplot as plt

mean_group_a = np.mean(weight_lost_a)
mean_group_b = np.mean(weight_lost_b)

mean_difference = mean_group_b - mean_group_a
print(mean_difference)

## 5. Permutation Test ##

# the null mean difference
mean_difference = 2.52

# creating an empty list for mean differences
mean_differences = []

for i in range(0, 1000):
    group_a = []
    group_b = []
    
    for value in all_values:
        rand_num = np.random.rand()  # generates a num of [0, 1)
        if rand_num >= 0.5:
            group_a.append(value)
        else:
            group_b.append(value)
            
    iteration_mean_difference = np.mean(group_b) - np.mean(group_a)
    mean_differences.append(iteration_mean_difference)
    
    
plt.hist(mean_differences)
plt.show()

## 7. Dictionary Representation of a Distribution ##

sampling_distribution = {}
for df in mean_differences:
    if sampling_distribution.get(df, False):
        sampling_distribution[df] = sampling_distribution[df] + 1
    else:
        sampling_distribution[df] = 1

## 8. P Value ##

frequencies = []
for sp in sampling_distribution.keys():
    if sp >= 2.52:
        frequencies.append(sampling_distribution[sp])
p_value = np.sum(frequencies) / 1000