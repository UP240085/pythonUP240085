#1 Declare an empty list
print("1- Declare an empty list")
Emptylist = []

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
full_stack = front_end + back_end
print(full_stack)
