#Exercises level 1
#1 Create an empty tuple
print("1- Create an empty tuple")
empty_tuple = tuple() #o empty_tuple = ()

#2 Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
print("2- Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)")
brothers = ("Bryan", "Alejandro")
print(brothers)
sisters = ("Susana", "Valentina")
print(sisters)

#3 Join brothers and sisters tuples and assign it to siblings
print("3- Join brothers and sisters tuples and assign it to siblings")
siblings = brothers + sisters
print(siblings)

#4 How many siblings do you have?
print("How many siblings do you have?")
len_siblings = len(siblings)
print(len_siblings)

#5 Modify the siblings tuple and add the name of your father and mother and assign it to family_members
print("Modify the siblings tuple and add the name of your father and mother and assign it to family_members")
listm = list(siblings)
listm.append("Gilberto")
listm.append("Elizabeth")
family_members = tuple(listm)
print(family_members)

#Exercises level 2
#1 Unpack siblings and parents from family_members
print("1- Unpack siblings and parents from family_members")
family_members = list(family_members)
print(family_members)
siblings = family_members[0:4]
print(f"Mis hermanos son {siblings}")
parents = family_members[4:]
print(f"Mis padres son {parents}")

#2 Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
print("2- Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.")
fruits = ("apple", "mango", "pear")
vegetables = ("carrot", "onion")
animal_products = ("egg", "milk")
food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)

#3 Change the about food_stuff_tp tuple to a food_stuff_lt list
print("3- Change the about food_stuff_tp tuple to a food_stuff_lt list")
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

#4 Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
print("4- Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.")
print(len(food_stuff_lt))
middle_item = food_stuff_lt[(len(food_stuff_lt)//2)]
print (middle_item)

#5 Slice out the first three items and the last three items from food_staff_lt list
print("5- Slice out the first three items and the last three items from food_staff_lt list")
first_three = food_stuff_lt[:3]
print(first_three)
last_three = food_stuff_lt[-3:]
print(last_three)

#6 Delete the food_staff_tp tuple completely
print("6- Delete the food_staff_tp tuple completely")
del food_stuff_tp

#7 Check if an item exists in tuple:
print("7- Check if an item exists in tuple:")
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print(f"Existe Estonia en nordic_countries: {"Estonia" in nordic_countries}")
print(f"Existe Iceland en nordic_countries: {"Iceland" in nordic_countries}")


