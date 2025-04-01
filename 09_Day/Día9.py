#Conditionals
#Exercises: Level 1

#1- Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. 
print("1- Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years.")
age = int(input("Enter your age: "))
if age >= 18:
    print("You are old enough to drive")
else:
    print(f"Wait for {18 - age} years")

#2- Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. 
print("2- Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age.")
my_age = 18
your_age = int(input("Enter your age: "))
if my_age > your_age:
    print(f"I am {my_age - your_age} years older than you")
elif my_age < your_age:
    print(f"You are {your_age - my_age} years older than me")
else:
    print("We are the same age")

#3- Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b
print("3- Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b")
a = (input("Enter the first number: "))
b = (input("Enter the second number: "))
if a > b:
    print("a is greater than b")
elif a < b:
    print("a is smaller than b")
else:
    print("a is equal to b")

#Exercises: Level 2

#1- Write a code which gives grade to students according to their scores:
print("1- Write a code which gives grade to students according to their scores:")
score = int(input("Enter your score: "))
if score >= 80:
    print("Your grade is A")
elif score >= 70:
    print("Your grade is B")
elif score >=60:
    print("Your grade is C")         
elif score >=50:
    print("Ypur grades is D")
else:        
    print("Your grade is F")

#2- Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer
print("2- Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer")
month = input("Enter the month: ")
if month in ["September", "October", "November"]:
    print("The season is Autumn")
elif month in ["December", "January", "February"]:
    print("The season is Winter")
elif month in ["March", "April", "May"]:
    print("The season is Spring")
elif month in ["June", "July", "August"]:
    print("The season is Summer")
else:
    print("This is not a valid month")

#3- If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')
print("3- If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')")
fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = input("Enter the fruit: ")
if fruit in fruits:
    print("That fruit already exist in the list")
else:
    fruits.append(fruit)
    print(fruits) 

#Exercises: Level 3
#* Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
# * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
#* If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
 #* If the person is married and if he lives in México, print the information


person={
    'first_name': 'Brandon',
    'last_name': 'Tovar',
    'age': 18,
    'country': 'México',
    'is_married': True,
    'skills': ['JavaScript', 'React', "Node", "Python", "MongoDB"],
    'address': {
        'street': 'Simon Bolivar 149',
        'zipcode': '47270'
    }
    }
if 'skills' in person:
    skills = person['skills']
    middle = len(skills) // 2
    print(skills[middle])
    Python = 'Python' in skills
    comp = ["JavaScript", "React"]
    comp.sort()
    skills.sort()
    print(f"Is Pyhton in the skills? {Python}")
    if skills == comp:
        print("He is a front end developer")
    elif "Node" and "Python" and "MongoDB" in skills:
        print("He is backend developer")
    elif "React" and "Node" and "MongoDB" in skills:
        print("He is a fullstack developer")      
    else:
        print("Unknown title")

married = person["is_married"]
country = person["country"]
if married == True and country == "México":
    print(f"{person["first_name"]} {person['last_name']} lives in {person['country']}. He is married")
else:
    print("He doesn´t live in México or he is´nt married ")


print("No ejecuta")