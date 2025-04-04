#Open you python interactive shell and try all the examples covered in this section
#SyntaxError
#print"Hello World" #SyntaxError: Missing parentheses in call to 'print'. Did you mean print("Hello World")?
print("Hello World") #Corrected

#NameError
#print(hello) #NameError: name 'hello' is not defined
hello = "Hello World" #Corrected
print(hello) #Corrected

#IndexError
#my_list = [1, 2, 3]
#print(my_list[3]) #IndexError: list index out of range
my_list = [1, 2, 3] #Corrected
print(my_list[2]) #Corrected

#ModuleNotFoundError
#import non_existent_module #ModuleNotFoundError: No module named 'non_existent_module'
import math #Corrected
print(math.sqrt(16)) #Corrected

#AttributeError
my_string = "Hello"
#my_string = "Hello"
#print(my_string.uppercase()) #AttributeError: 'str' object has no attribute 'uppercase'
print(my_string.upper()) #Corrected

#KeyError
my_dict = {"name": "Alice"}
#print(my_dict["age"]) #KeyError: 'age'
print(my_dict["name"]) #Corrected

#TypeError

my_number = "5"
#print(my_number + 5) #TypeError: unsupported operand type(s) for +: 'str' and 'int'
my_number = 5
print(my_number + 5) #Corrected

#ImportError
#from math import reduce #ImportError: cannot import name 'non_existent_function' from 'math'
#except ImportError:
print("ImportError: Cannot import non_existent_function from math")

#ValueError
my_list = [1, 2, 3]
#print(my_list.index(4)) #ValueError: 4 is not in list
print(my_list.index(3)) #Corrected

#ZeroDivisionError
my_number = 10
#print(my_number / 0) #ZeroDivisionError: division by zero
my_number = 10
print(my_number / 2) #Corrected
