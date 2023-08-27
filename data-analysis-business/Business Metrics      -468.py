## 2. What's a Good Metric? ##

ans1 = "no"
ans21 = "no"
ans22 = "yes"

## 3. Introduction to the Net Promoter Score ##

"""
    Function: categorize

    Description:
    Categorizes a score into one of three categories: Detractor, Passive, or Promoter.

    Input:
    - score (float): The score to be categorized.

    Output:
    - (str): The category of the score.

    Author: David van der Byl

    Date: -/-/23
"""

def categorize(score: float) -> str:
    # If the score is less than 7, classify as Detractor
    if score < 7:
        return "Detractor"
    # If the score is greater than 8, classify as Promoter
    elif score > 8:
        return "Promoter"
    # If the score is between 7 and 8 (inclusive), classify as Passive
    else:
        return "Passive"
    return None

## 4. Net Promoter Score ##

import pandas as pd

df = pd.read_csv("nps.csv", parse_dates=["event_date"])

# Q1: 

# Extract the year and month from the "event_date" column and create a new "yearmonth" column
year = df["event_date"].dt.year
month = df["event_date"].dt.month
# Multiply the year by 100 and add the month to create a yyyymm format
df["yearmonth"] = 100 * year + month 



# Q2: 

# Categorize the scores into Detractor, Passive, or Promoter categories using the "categorize" function
df["category"] = df["score"].apply(categorize)



# Q3: 

# Calculate the NPS (Net Promoter Score) for each month and store the results in a pivot table
nps = df.pivot_table(index="yearmonth",
                     columns="category",
                     aggfunc="size")

# Calculate the total number of responses for each month
nps["total_responses"] = nps.sum(axis="columns")

# Calculate the NPS for each month as the difference between the number of promoters and detractors, divided by the total number of responses
nps["nps"] = (nps["Promoter"] - nps["Detractor"]) / nps["total_responses"]

# Convert the NPS to an integer percentage and store the results in a new column
nps["nps"] = (nps["nps"] * 100).astype(int)

# Return the pivot table with the NPS results
nps

## 6. Customer Churn ##

import pandas as pd

# Q1: Read in data from the "muscle_labs.csv" file and 
# parse the "end_date" and "start_date" columns as datetime objects
subs = pd.read_csv("muscle_labs.csv", parse_dates=["end_date", "start_date"])

# Q2: Create a new column "churn_month" that represents the year 
# and month of the subscription end date in yyyymm format
subs["churn_month"] = (100*subs["end_date"].dt.year + subs["end_date"].dt.month).astype(int)

# Q3: Group the subscriptions by churn month and count 
# the total number of churned subscribers each month
monthly_churn = pd.DataFrame({"total_churned": subs.groupby("churn_month").size()})

monthly_churn.head()

## 7. Date Wrangling ##

years = list(range(2011,2015))
months = list(range(1,13))
yearmonths = [y*100+m for y in years for m in months]
yearmonths = yearmonths[:-1]

churn = pd.DataFrame({"yearmonth": yearmonths})


# Q1:
churn = pd.merge(churn, 
                 monthly_churn, 
                 "left", 
                 left_on="yearmonth", 
                 right_index=True
                )

# Q3:
churn.fillna(0, inplace=True)

# Q4:
churn["total_churned"] = churn["total_churned"].astype(int)
churn.head()

## 8. Churn Rate ##

import datetime as dt

# arange = __import__("numpy").arange
# Ellipse = __import__("matplotlib").patches.Ellipse
# ax = churn.plot(x="yearmonth", y="churn_rate", figsize=(12,6), rot=45, marker=".")
# start, end = ax.get_xlim()
# ax.get_xticks()
# ax.set_xticks(arange(2, end, 3))
# ax.set_xticklabels(yearmonths[2::3])
# circle = Ellipse((35, churn.loc[churn.yearmonth == "201312", "churn_rate"].iloc[0]),
#                  5, 0.065, color='sandybrown', fill=False
#                    )
# ax.add_artist(circle)
# ax.xaxis.label.set_visible(False)
# ax.spines['top'].set_visible(False)
# ax.spines['right'].set_visible(False)
# ax.get_legend().remove()
import datetime as dt

# Q1:
def get_customers(yearmonth: int) -> int:
    """
    Returns the number of active customers for a given yearmonth
    
    Args:
    - yearmonth: an integer representing the year and month in the format yyyymm
    
    Returns:
    - An integer representing the number of active customers for the given yearmonth
    
    Author: [Your Name]
    Date: [Current Date]
    """
    
    year = yearmonth // 100
    month = yearmonth - year * 100
    date = dt.datetime(year, month, 1)

    return ((subs["start_date"] < date) & 
            (date <= subs["end_date"])
           ).sum()

# Q2:
churn["total_customers"] = churn["yearmonth"].apply(get_customers)

# Q3:
churn["churn_rate"] = churn["total_churned"] / churn["total_customers"]

# Q4:
churn["yearmonth"] = churn["yearmonth"].astype(str)

arange = __import__("numpy").arange
Ellipse = __import__("matplotlib").patches.Ellipse
ax = churn.plot(x="yearmonth", y="churn_rate", figsize=(12,6), rot=45, marker=".")
start, end = ax.get_xlim()
ax.get_xticks()
ax.set_xticks(arange(2, end, 3))
ax.set_xticklabels(yearmonths[2::3])
circle = Ellipse((35, churn.loc[churn.yearmonth == "201312", "churn_rate"].iloc[0]),
                 5, 0.065, color='sandybrown', fill=False
                   )
ax.add_artist(circle)
ax.xaxis.label.set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.get_legend().remove()