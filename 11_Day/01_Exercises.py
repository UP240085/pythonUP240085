#Declare a function add_two_numbers. It takes two parameters and it returns a sum.
print("Declare a function add_two_numbers. It takes two parameters and it returns a sum.")
def add_two_numbers(a, b):
    return a + b
print(add_two_numbers(3, 4))

#Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
print("Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.")
def area_of_circle(r):
    pi = 3.14
    return pi * r * r
print(area_of_circle(5))

#Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.
print("Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.")
def add_all_nums(*args):
    for arg in args:
        if arg == str(arg):
            return "All arguments must be numbers"
    return sum(args)
print(add_all_nums(1, 2, 3, 4, 5, 6))

#Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
print("Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.")
def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
print(convert_celsius_to_fahrenheit(0))

#Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
print("Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.")
def check_season(month):
    if month in ["September", "October", "November"]:
        return "Autumn"
    elif month in ["December", "January", "February"]:
        return "Winter"
    elif month in ["March", "April", "May"]:
        return "Spring"
    elif month in ["June", "July", "August"]:
        return "Summer"
    else:
        return "This is not a valid month"
print(check_season("January"))

#Write a function called calculate_slope which return the slope of a linear equation
print("Write a function called calculate_slope which return the slope of a linear equation")
def calculate_slope(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)   #Formula for slope
print(calculate_slope(1, 2, 3, 4))

#Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
print("Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.")
#The quadratic formula is x = [-b ± sqrt(b^2 - 4ac)] / (2a).
#The term inside the square root, b^2 - 4ac, is called the discriminant.
#If it's positive, there are two real roots.
#If it's zero, there's one real root.
#If it's negative, there are two complex roots.

def solve_quadratic_eqn(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        root1 = (-b + discriminant**0.5) / (2*a)
        root2 = (-b - discriminant**0.5) / (2*a)
        return (root1, root2)
    elif discriminant == 0:
        root = -b / (2*a)
        return (root,)
    else:
        real_part = -b / (2*a)
        imaginary_part = (-discriminant)**0.5 / (2*a)
        return (complex(real_part, imaginary_part), complex(real_part, -imaginary_part))
print(solve_quadratic_eqn(1, -3, 2))

#Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
print("Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.")
def print_list(lst):
    for item in lst:
        print(item)
print_list([1, 2, 3, 4, 5])

#Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).4
print("Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).")
def reverse_list(lst):
    reversed_lst = []
    for item in lst:
        reversed_lst.insert(0, item)
    return reversed_lst
print(reverse_list([1, 2, 3, 4, 5]))

#Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
print("Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items")
def capitalize_list_items(lst):
    for item in range(len(lst)):
        lst[item] = lst[item].capitalize()
    return lst
print(capitalize_list_items(['apple', 'banana', 'cherry']))

#Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
print("Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.")
test = [0, 1, 2, 3]
def add_item(lst, item):
    lst.append(item)
    return lst
print(add_item(test, 4))

#Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
print("Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.")
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
def remove_item(lst, item):
    lst.remove(item)
    return lst
print(remove_item(food_staff, 'Mango'))

#Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
print("Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.")
def sum_of_numbers(n):
    total = 0
    for i in range(n + 1):
        total += i
    return total
print(sum_of_numbers(10))

#Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
print("Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.")
def sum_of_odds(n):
    total = 0
    for i in range(n + 1):
        if i % 2 != 0:
            total += i
    return total
print(sum_of_odds(10))

#Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that range.
print("Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that range.")
def sum_of_even(n):
    total = 0
    for i in range(n + 1):
        if i % 2 == 0:
            total += i
    return total
print(sum_of_even(10))

