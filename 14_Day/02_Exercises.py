countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#Use map to create a new list by changing each country to uppercase in the countries list
print("Use map to create a new list by changing each country to uppercase in the countries list.")
def to_uppercase(country):
    return country.upper()
map_uppercase = map(to_uppercase, countries)
print(list(map_uppercase))

map_uppercase = map(lambda country: country.upper(), countries)
print(list(map_uppercase))

#Use map to create a new list by changing each number to its square in the numbers list
print("Use map to create a new list by changing each number to its square in the numbers list.")
def square(num):
    return num ** 2
msquare = map(square, numbers)
print(list(msquare))

#Use map to change each name to uppercase in the names list
print("Use map to change each name to uppercase in the names list.")
def n_uppercase(name):
    return name.upper()
print(list(map(n_uppercase, names)))