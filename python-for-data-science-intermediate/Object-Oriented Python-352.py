## 1. Introduction ##

l = [1, 2, 3]
s = "string"
d = {"a": 1, "b": 2}

print(type(l))
print(type(s))
print(type(d))
print(type(1))

## 3. Defining a Class ##

class MyClass:
    pass

## 4. Instantiating a Class ##

class MyClass:
    pass

#"Instantiate an object of that class."
my_instance = MyClass()

print(type(my_instance))

## 5. Creating Methods ##

class MyClass:
    def first_method():
        return "This is my first method"
    
    
my_instance = MyClass() 

## 6. Understanding "self" ##

class MyClass:
    def first_method(self):
        return "This is my first method"
    
    
my_instance = MyClass() 
result = my_instance.first_method()
print(result)

## 7. Creating a Method that Accepts an Argument ##

class MyClass:
    
    def first_method(self):
        return "This is my first method"
    
    def return_list(self, input_list:list):
        return input_list
    
my_instance = MyClass()

result = my_instance.return_list([1,2,3])
print(result)
    
    # Add method here

## 8. Attributes and the Init Method ##

class MyList:
    
    def __init__(self, initial_data: list):
        self.data = initial_data
        
my_list = MyList([1,2,3,4,5])

print(my_list.data)

## 9. Creating an Append Method ##

class MyList:

    def __init__(self, initial_data):
        self.data = initial_data
        
    def append(self, new_item):
        self.data = self.data + [new_item]
    
my_list = MyList([1,2,3,4,5])
print(my_list.data)

my_list.append(6)
print(my_list.data)


    

## 10. Creating and Updating an Attribute ##

class MyList:

    def __init__(self, initial_data):
        self.data = initial_data
        # Calculate the initial length
        self.length = 0
        for item in self.data:
            self.length += 1

    def append(self, new_item):
        self.data = self.data + [new_item]

        # Update list length attribute: method 1
        #self.length = 0
        #for item in self.data:
        #    self.length += 1
            
        # OR more simply like this: method 2
        self.length += 1
            
my_list = MyList([1, 1, 2, 3, 5])
print(my_list.length)

my_list.append(8)
print(my_list.length)