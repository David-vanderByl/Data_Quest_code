## 1. Introduction ##

# Gettting the dimemsions/shape of each dataframe
shape_2015 = happiness2015.shape
print('The dimensions of the 2015 dataframe is: ', shape_2015, '\n')

shape_2016 = happiness2016.shape
print('The dimensions of the 2016 dataframe is: ', shape_2016, '\n')

shape_2017 = happiness2015.shape
print('The dimensions of the 2017 dataframe is: ', shape_2017, '\n')
print('Note: dimensions/shapes presented as (rows, column)')

## 2. Identifying Missing Values ##

# getting the sum of NaN entries in each dataframe
missing_2015 = happiness2015.isnull().sum()
print('NaN entries in 2015 dataframe \n')
print(missing_2015, '\n')

missing_2016 = happiness2016.isnull().sum()
print('NaN entries in 2016 dataframe \n')
print(missing_2016, '\n')

missing_2017 = happiness2017.isnull().sum()
print('NaN entries in 2017 dataframe \n')
print(missing_2017, '\n')

## 3. Correcting Data Cleaning Errors that Result in Missing Values ##

happiness2017.columns = happiness2017.columns.str.replace('.', ' ').str.replace('\s+', ' ').str.strip().str.upper()

happiness2015.columns = happiness2015.columns.str.replace('(', '').str.replace(')', '').str.strip().str.upper()
happiness2016.columns = happiness2016.columns.str.replace('(', '').str.replace(')', '').str.strip().str.upper()

combined = pd.concat([happiness2015, happiness2016, happiness2017], ignore_index=True)
missing = combined.isnull().sum()

## 4. Visualizing Missing Data ##

regions_2017 = combined[combined['YEAR']==2017]['REGION']
missing = regions_2017.isnull().sum()

## 5. Using Data From Additional Sources to Fill in Missing Values ##

combined = pd.merge(left=combined, right=regions, on='COUNTRY', how='left')
combined = combined.drop('REGION_x', axis = 1)
missing = combined.isnull().sum()

## 6. Identifying Duplicates Values ##

combined['COUNTRY'] = combined['COUNTRY'].str.upper()
dups = combined.duplicated(['COUNTRY', 'YEAR'])
combined_dups = combined[dups]

## 7. Correcting Duplicates Values ##

combined['COUNTRY'] = combined['COUNTRY'].str.upper()

combined = combined.drop_duplicates(['COUNTRY', 'YEAR'])

## 8. Handle Missing Values by Dropping Columns ##

columns_to_drop = ['LOWER CONFIDENCE INTERVAL', 'STANDARD ERROR', 'UPPER CONFIDENCE INTERVAL', 'WHISKER HIGH', 'WHISKER LOW']

combined = combined.drop(columns_to_drop, axis = 1)
missing = combined.isnull().sum()

## 9. Handle Missing Values by Dropping Columns Continued ##

combined = combined.dropna(thresh=159, axis=1)
missing = combined.isnull().sum()

## 11. Handling Missing Values with Imputation ##

happiness_mean = combined['HAPPINESS SCORE'].mean()
print(happiness_mean)
combined['HAPPINESS SCORE UPDATED'] = combined['HAPPINESS SCORE'].fillna(happiness_mean)
print(combined['HAPPINESS SCORE UPDATED'].mean())

## 12. Dropping Rows ##

combined = combined.dropna()
missing = combined.isnull().sum()