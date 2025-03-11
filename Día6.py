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
fruits = tuple("apple", "mango")
vegetables = tuple("carrot", "onion")
animal_products = tuple("egg", "milk")
food_stuff_tp = fruits + vegetables + animal_products
