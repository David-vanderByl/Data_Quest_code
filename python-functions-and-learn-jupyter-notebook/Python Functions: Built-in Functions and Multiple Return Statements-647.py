## 1. Interfering with the Built-In Functions ##

a_list = [1, 8, 10, 9, 7]
print(max(a_list))

def max(a_list: list):
    return "No max value returned"

max_val_test_0 = max(a_list)

print(max_val_test_0)

del max

print(max(a_list))

## 3. Default Arguments ##

def open_dataset(file_name = 'AppleStore.csv'):
    
    opened_file = open(file_name)
    from csv import reader
    read_file = reader(opened_file)
    data = list(read_file)
    
    return data

apps_data = open_dataset()

print(apps_data[1:4][1])

## 4. The Official Python Documentation ##

one_decimal = round(3.43,1)
print(one_decimal)

two_decimals = round(0.233321,2)
print(two_decimals)

five_decimals = round(921.2225227,5)
print(five_decimals)

## 5. Multiple Return Statements ##

def open_dataset(header = True, file_name='AppleStore.csv'):
    opened_file = open(file_name)
    from csv import reader
    read_file = reader(opened_file)
    data = list(read_file)
    
    if header == True:
        return data
    else:
        return data[1:]

apps_data = open_dataset(False)

## 6. Not Using the else Clause ##

def open_dataset(file_name='AppleStore.csv', header=True):        
    opened_file = open(file_name)
    from csv import reader
    read_file = reader(opened_file)
    data = list(read_file)
    
    if header:
        return data[1:]
    return data

apps_data = open_dataset('AppleStore.csv')