#1 Declare an empty list
print("1- Declare an empty list")
Emptylist = []
print(Emptylist)

#2 Declare a list with more than 5 items
print("2- Declare a list with more than 5 items")
list = [1,2,3,4,5,6,7,8,9,10]

#3 Find the length of your list
print("3- Find the length of your list")
print(len(list))

#4 Get the first item, the middle item and the last item of the list
print("4- Get the first item, the middle item and the last item of the list")
print(list[0])
print(list[len(list)//2])
print(list[-1])

#5 Declare a list called mixed_data_types, put your(name), age, height, marital status, and address
print("5- Declare a list called mixed_data_types, put your(name), age, height, marital status, and address")
mixed_data_types = ["Brandon", 18, 1.66, "Soltero", "Simon Bolivar #149"]
print(mixed_data_types)

#6 Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon
print("6- Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon")
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

#7 Print the list using print()
print("7- Print the list using print()")
print(it_companies)

#8 Print the number of companies in the list
print("8- Print the number of companies in the list")
print(len(it_companies))

#9 Print the first, middle and last company
print("9- Print the first, middle and last company")
print(it_companies[0])
print(it_companies[len(it_companies)//2])
print(it_companies[-1])

#10 Print the list after modifying one of the companies
print("10- Print the list after modifying one of the companies")
it_companies[0] = "Facebook and Meta"
print(it_companies)

#11 Add an IT company to it_companies
print("11- Add an IT company to it_companies")
it_companies.append("It company")
print(it_companies)

#12 Insert an IT company in the middle of the companies list
print("12- Insert an IT company in the middle of the companies list")
it_companies.insert(len(it_companies)//2, "It company")
print(it_companies)

#13 Change one of the it_companies names to uppercase (IBM excluded!)
print("13- Change one of the it_companies names to uppercase (IBM excluded!)")
it_companies[0] = it_companies[0].upper()
print(it_companies)

#14 Join the it_companies with a string '#; '
print("14- Join the it_companies with a string '#; '")
print("#; ".join(it_companies))

#15 Check if a certain company exists in the it_companies list
print("15- Check if a certain company exists in the it_companies list")
check = "Facebook"
exist = "FACEBOOK AND META"
if check in it_companies:
    print(f"{check} exists in the list")
else:
    print(f"{check} doesn't exist in the list")
if exist in it_companies:
    print(f"{exist} exists in the list")
else:
    print(f"{exist} doesn't exist in the list")

#16 Sort the list using sort() method
print("16- Sort the list using sort() method")
it_companies.sort()
print(it_companies)

#17 Reverse the list in descending order using reverse() method
print("17- Reverse the list in descending order using reverse() method")
it_companies.reverse()
print(it_companies)

#18 Slice out the first 3 companies from the list
print("18- Slice out the first 3 companies from the list")
three_companies = it_companies[0:3] 
print(three_companies)

#19 Slice out the last 3 companies from the list
print("19- Slice out the last 3 companies from the list")
three_companies = it_companies[-3:]
print(three_companies)

#20 Slice out the middle IT company or companies from the list
print("20- Slice out the middle IT company or companies from the list")
middle_companie = it_companies[len(it_companies)//2]
print(middle_companie)

#21 Remove the first IT company from the list
print("21- Remove the first IT company from the list")
it_companies.pop(0)
print(it_companies)

#22 Remove the middle IT company or companies from the list
print("22- Remove the middle IT company or companies from the list")
middle = (len(it_companies)//2)
del it_companies[middle:middle+2]
print(it_companies)

#23 Remove the last IT company from the list
print("23- Remove the last IT company from the list")
it_companies.pop()
print(it_companies)

#24 Remove all IT companies from the list
print("24- Remove all IT companies from the list")
it_companies.clear()
print(it_companies)

#25 Destroy the IT companies list
print("25- Destroy the IT companies list")
del it_companies

#26 Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
print("26- Join the following lists:")
print(front_end)
print(back_end)
join_list = front_end + back_end
print(join_list)

#27 After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack then insert Python and SQL after Redux
print("27- After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack then insert Python and SQL after Redux")
full_stack = join_list.copy()
print(full_stack)
full_stack.insert(full_stack.index("Redux")+1, "Python")
full_stack.insert(full_stack.index("Python")+1, "SQL")
print(full_stack)

#Exercise level 2
print("Exercise level 2")

#1 The following is a list of 10 students ages:
print("1- The following is a list of 10 students ages:")
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 23]
print(ages)

#Sort the list and find the min and max age
#Add the min age and the max age again to the list
#Find the median age (one middle item or two middle items divided by two)
#Find the average age (sum of all items divided by their number )
#Find the range of the ages (max minus min)
#Compare the value of (min - average) and (max - average), use abs() method
print("Sort the list and find the min and max age")
ages.sort()
print(ages)
print("Find the min age")
print(ages[0])
print("Find the max age")
print(ages[-1])
print("Add the min age and the max age again to the list")
min=ages[0]
max=ages[-1]
ages.append(min)
ages.append(max)
print(ages)
print("Find the median age")
ages.sort() 
print(ages)
len_ages = len(ages)
print (f"El número de datos es: {len_ages}")
median = (ages[len_ages//2] + ages[len_ages//2-1]) / 2
print(median)
print("Find the average age")
ages
n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11, n12 = ages
average = (n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8 + n9 + n10 + n11 + n12) / len_ages
print(average)
print("Find the range of the ages, max - min")
print(f"El menor es: {min}")
print(f"El mayor es: {max}")
range = max - min
print(f"El rango es: {range}")
print("Compare the value of (min - average) and (max - average), use abs() method")
min_average = abs (min - average)
print(f"Valor 1: {min_average}")
max_average = abs (max - average)
print(f"Valor 2: {max_average}")
print(f"El valor 2 es igual al 1: {max_average==min_average}")
print(f"El valor 2 no es igual al 1: {max_average!=min_average}")
print(f"El valor 2 es mayor que el 1: {max_average>min_average}")
print(f"El valor 2 es menor que el 1: {max_average<min_average}")

#Find the middle country(ies) in the countries list
print("Find the middle country(ies) in the countries list")
import countries as c
print(c.countries)
countries = c.countries
len_countries = len(countries)
print(len_countries)
#Divide the countries list into two equal lists if it is even if not one more country for the first half.
#['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.