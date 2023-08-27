## 1. Returning Multiple Variables ##

def pythagorean(a, b):
    a_squared = a**2
    b_squared = b**2
    c_squared = a_squared + b_squared
    
    return a_squared, b_squared, c_squared

print(pythagorean(5,12))

## 2. Tuples ##

def open_dataset(file_name='AppleStore.csv', header=True):        
    opened_file = open(file_name)
    from csv import reader
    read_file = reader(opened_file)
    data = list(read_file)
    
    if header:
        return data[0], data[1:]
    else:
        return data

all_data = open_dataset()
header = all_data[0]
apps_data = all_data[1]

## 3. More About Tuples ##

def open_dataset(file_name='AppleStore.csv', header=True):        
    opened_file = open(file_name)
    from csv import reader
    read_file = reader(opened_file)
    data = list(read_file)
    
    header = data[0]
    apps_data = data[1:]
    
    return [header,apps_data]

header, apps_data = open_dataset()