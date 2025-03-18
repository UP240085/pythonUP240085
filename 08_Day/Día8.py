#Dictionaries

#1- Create an empty dictionary called dog
print("1- Create an empty dictionary called dog")
dog = {}
print(dog)

#2- Add name, color, breed, legs, age to the dog dictionary
print("2- Add name, color, breed, legs, age to the dog dictionary")
dog = {"name": "Firulais", "color": "brown", "breed": "Labrador", "legs": 4, "age": 5}
print(dog)

#3- Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
print("3- Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary")
student = {"first_name": "Brandon", "last name": "Tovar", "gender": "M", "age": 18, "marital status": "single", "skills":["Python", "extra"], "country": "Mexico", "city": "Chona", "address": "Simon Bolivar 149"}

#4.-Get the length of the student dictionary
print("4.-Get the length of the student dictionary")
print(len(student))

#5.-Get the value of skills and check the data type, it should be a list
print("5.-Get the value of skills and check the data type, it should be a list")
print(student["skills"])
print(type(student["skills"]))

#6.-Modify the skills values by adding one or two skills
print("6.-Modify the skills values by adding one or two skills")
student["skills"].append("otro")
print(student["skills"])

#7.-Get the dictionary keys as a list
print("7.-Get the dictionary keys as a list")
print(student.keys())

#8- Get the dictionary values as a list
print("8- Get the dictionary values as a list")
print(student.values())

#9- Change the dictionary to a list of tuples using items() method
print("9- Change the dictionary to a list of tuples using items() method")
print(student.items())

#10- Delete one of the items in the dictionary
print("10- Delete one of the items in the dictionary")
student.pop("address")
print(student)

#11- Delete one of the dictionaries
print("11- Delete one of the dictionaries")
del student