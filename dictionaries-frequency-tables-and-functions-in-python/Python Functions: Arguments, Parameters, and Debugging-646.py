## 1. Extract Values from Any Column ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)


def extract(data_set, col):
    list = []
    for row in data_set:
#        if row[col] not in list:
        list.append(row[col])
        
    return list

genres = extract(apps_data[1:], 11)
print(genres)
        

## 2. Creating Frequency Tables ##

# CODE FROM THE PREVIOUS SCREEN
opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

def extract(index):
    column = []    
    for row in apps_data[1:]:
        value = row[index]
        column.append(value)    
    return column

genres = extract(11)

def freq_table(column):
    freq_table = {}
    for key in column:
        if key in freq_table:
            freq_table[key] += 1
        else:
            freq_table[key] = 1
            
    return freq_table

genres_ft = freq_table(genres)





    

## 3. Writing a Single Function ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)


def freq_table(data_set: list, col: int):
    freq_table = {}
    
    for row in data_set:
        key = row[col]    
        
        if key in freq_table:
            freq_table[key] += 1
        else:
            freq_table[key] = 1
            
    return freq_table

ratings_ft = freq_table(apps_data[1:], 7)
print(ratings_ft)

## 4. Reusability and Multiple Parameters ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

# INITIAL FUNCTION
def freq_table(data_set: list, index: int):
    frequency_table = {}
    
    for row in data_set:
        value = row[index]
        if value in frequency_table:
            frequency_table[value] += 1
        else:
            frequency_table[value] = 1
            
    return frequency_table

ratings_ft = freq_table(apps_data[1:], 7)
print(ratings_ft)

## 5. Keyword and Positional Arguments ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

def freq_table(data_set, index):
    frequency_table = {}
    
    for row in data_set:
        value = row[index]
        if value in frequency_table:
            frequency_table[value] += 1
        else:
            frequency_table[value] = 1
        
    return frequency_table

data_set = apps_data[1:]
content_ratings_ft = freq_table(data_set, 10)
ratings_ft = freq_table(data_set = data_set, index = 7)
genres_ft = freq_table(index = 11, data_set = data_set)

## 6. Combining Functions ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

def extract(data_set, index):
    column = []    
    for row in data_set[1:]:
        value = row[index]
        column.append(value)    
    return column

def find_sum(a_list):
    a_sum = 0
    for element in a_list:
        a_sum += float(element)
    return a_sum

def find_length(a_list):
    length = 0
    for element in a_list:
        length += 1
    return length

def mean(data_set: list, index: int):
    a_list = extract(data_set, index)
    return find_sum(a_list)/find_length(a_list)

avg_price = mean(apps_data, 4)
print(avg_price)

## 7. Debugging Functions ##

def extract(data_set:list, index:int):
    column = []
    for row in data_set:
        value = row[index]
        column.append(value)   
    return column

def find_sum(a_list):
    a_sum = 0
    for element in a_list:
        a_sum += float(element)
    return a_sum

def find_length(a_list):
    length = 0
    for element in a_list:
        length += 1
    return length

def mean(data_set: list, index: int):
    column = extract(data_set, index)
    return find_sum(column) / find_length(column)


avg_price = mean(apps_data[1:], 4)
avg_rating = mean(apps_data[1:], 7)