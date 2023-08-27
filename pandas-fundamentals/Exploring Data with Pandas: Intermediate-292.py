## 1. Introduction ##

import pandas as pd
# read the data set into a pandas dataframe
f500 = pd.read_csv("f500.csv", index_col=0)
f500.index.name = None

# replace 0 values in the "previous_rank" column with NaN
f500.loc[f500["previous_rank"] == 0, "previous_rank"] = np.nan

f500_selection = f500[['rank', 'revenues', 'revenue_change']].head()

## 2. Reading CSV files with pandas ##

f500 = pd.read_csv('f500.csv')

f500.loc[f500["previous_rank"] == 0, "previous_rank"] = np.nan

## 3. Using iloc to select by integer position ##

fifth_row = f500.iloc[4]
company_value = f500.iloc[0,0]

## 4. Using iloc to select by integer position continued ##

first_three_rows = f500.iloc[:3]
first_seventh_row_slice = f500.iloc[[0,6],:5]

## 5. Using pandas methods to create boolean masks ##

prev_rank_isnull_bool = f500["previous_rank"].isnull()
null_previous_rank = f500[prev_rank_isnull_bool][["company","rank", "previous_rank"]]

## 6. Working with Integer Labels ##

null_previous_rank = f500[f500["previous_rank"].isnull()]

top5_null_prev_rank = null_previous_rank.iloc[:5]

## 7. Pandas Index Alignment ##

previously_ranked = f500[f500["previous_rank"].notnull()]


rank_change = previously_ranked["previous_rank"] - previously_ranked["rank"]


f500['rank_change'] = rank_change

## 8. Using Boolean Operators ##

large_revenue = f500['revenues'] > 100000
negative_profits = f500['profits'] < 0

combined = large_revenue & negative_profits

big_rev_neg_profit = f500[combined]

## 9. Using Boolean Operators Continued ##

filter_brazil_venezuela = (f500["country"] == "Brazil") | (f500["country"] == "Venezuela")
brazil_venezuela = f500[filter_brazil_venezuela]

filter_tech_outside_usa = (f500["sector"] == "Technology") & ~(f500["country"] == "USA")
tech_outside_usa = f500[filter_tech_outside_usa].head()

## 10. Sorting Values ##

japenese_comp = f500[f500["country"] == "Japan"]

sort_japenese_comp = japenese_comp.sort_values('employees', ascending=False)

top_japanese_employer = sort_japenese_comp.iloc[0]['company']

## 11. Using Loops with pandas ##

# Create an empty dictionary to store the results
avg_rev_by_country = {}

# Create an array of unique countries
countries = f500["country"].unique()

# Use a for loop to iterate over the countries
for c in countries:
    # Use boolean comparison to select only rows that
    # correspond to a specific country
    selected_rows = f500[f500["country"] == c]
    # Calculate the mean average revenue for just those rows
    mean = selected_rows["revenues"].mean()
    # Assign the mean value to the dictionary, using the
    # country name as the key
    avg_rev_by_country[c] = mean
    
# Another example    
top_employer_by_country = {}

countries = f500["country"].unique()

for c in countries:
    
    selected_rows = f500[f500['country'] == c]
    
    sorted_rows = selected_rows.sort_values('employees', ascending=False)
    
    top_employer = sorted_rows.iloc[0]
    
    employer_name = top_employer['company']
    
    top_employer_by_country[c] = employer_name
    
    

## 12. Challenge: Calculating Return on Assets by Sector ##

f500["roa"] = f500["profits"] / f500["assets"]


# aggregatin data by sector
top_roa_by_sector = {}

sectors = f500["sector"].unique()

for sector in sectors:
    
    # selection rows with the same sector name
    is_sector_bool = f500['sector'] == sector
    
    # selecting companies in sector
    sector_companies = f500.loc[is_sector_bool]
    
    # sorting companies in ascending order based on return on assets
    sorted_companies = sector_companies.sort_values('roa', ascending = False)
    
    # Getting top company 
    top_company = sorted_companies.iloc[0]
    
    # getting top roa company name
    company_name = top_company['company']
    
    # adding to dictionary with sector key names and values that are the sector 
    # highest return on assets
    top_roa_by_sector[sector] = company_name
    