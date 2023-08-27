## 1. Introduction ##

import pandas as pd
hn = pd.read_csv("hacker_news.csv")

## 2. The Regular Expression Module ##

import re

titles = hn["title"].tolist()
python_mentions = 0
pattern = "[Pp]ython"

for t in titles:
    if re.search(pattern, t):
        python_mentions += 1

## 3. Counting Matches with pandas Methods ##

pattern = '[Pp]ython' # regex pattern

titles = hn['title'] # pandas series of title column

# summing all the instances of pattern in titles
python_mentions = titles.str.contains(pattern).sum()
python_mentions # display the sum of instances

## 4. Using Regular Expressions to Select Data ##

# Regex pattern
pattern = '[Rr]uby'

# Pandas series of titles
titles = hn['title']

# Pandas series of titles containing ruby or Ruby
ruby_titles = titles[titles.str.contains(pattern)]
ruby_titles

## 5. Quantifiers ##

# boolean mask checking for email or e-mail
email_bool = titles.str.contains("e-?mail")

# summing instances
email_count = email_bool.sum()
email_count

# creating series of instances 
email_titles = titles[email_bool]

## 6. Character Classes ##

# regex expression for search tags of single word
pattern = '\[\w+\]'

# series of tags in titles series
tag_titles = titles[titles.str.contains(pattern)]

# number of tags
tag_count = tag_titles.shape[0]

## 7. Accessing the Matching Text with Capture Groups ##

# Regex expression for searching tags of single word
pattern = r'\[(\w+)\]'

# creating a frequency table of all the tags in title column
tag_freq = titles.str.extract(pattern, expand=False).value_counts()
tag_freq

## 8. Negative Character Classes ##

def first_10_matches(pattern):
    """
    Return the first 10 story titles that match
    the provided regular expression
    """
    all_matches = titles[titles.str.contains(pattern)]
    first_10 = all_matches.head(10)
    return first_10
pattern = r"[Jj]ava[^Ss]"
java_titles = titles[titles.str.contains(pattern)]

## 9. Word Boundaries ##

pattern = r"\b[Jj]ava\b"
java_titles = titles[titles.str.contains(pattern)]

## 10. Matching at the Start and End of Strings ##

pattern_beginning = r"^\[\w+\]"
beginning_count = titles.str.contains(pattern_beginning).sum()

pattern_ending =  r"\[\w+\]$"
ending_count = titles.str.contains(pattern_ending).sum()

## 11. Challenge: Using Flags to Modify Regex Patterns ##

import re

email_tests = pd.Series(['email', 'Email', 'e Mail', 'e mail', 'E-mail',
              'e-mail', 'eMail', 'E-Mail', 'EMAIL', 'emails', 'Emails',
              'E-Mails'])
pattern = r"\be[\-\s]?mails?\b"
email_mentions = titles.str.contains(pattern, flags=re.I).sum()