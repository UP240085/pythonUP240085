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

#Use filter to filter out countries containing 'land'.
print("Use filter to filter out countries containing 'land'.")
def filter_land(country):
    if "land" in country:
        return True
    return False
land_countries = filter(filter_land, countries)
print(list(land_countries))

#Use filter to filter out countries having exactly six characters.
print("Use filter to filter out countries having exactly six characters.")
def filter_six(country):
    if len(country) == 6:
        return True
    return False
countries_six = filter(filter_six, countries)
print(list(countries_six))

#Use filter to filter out countries containing six letters and more in the country list.
print("Use filter to filter out countries containing six letters and more in the country list.")
def filter_six(country):
    if len(country) >= 6:
        return True
    return False
countries_six = filter(filter_six, countries)
print(list(countries_six))

#Use filter to filter out countries starting with an 'E'
print("Use filter to filter out countries starting with an 'E'")
def e_countries(country):
    if country.startswith("E"):
        return True
    return False
starts_with_e = filter(e_countries, countries)
print(list(starts_with_e))

#Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))
print("Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))")
 #Sin el from functools no se puede usar reduce en el código
from functools import reduce
chained = reduce(lambda x, y: x + y,  map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers)))
print(chained)

#Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.
print("Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.")
objects = [1, 2, 3, "a", "b", "c", True, False, None]
def get_string_lists(lst):
    if type(lst) == str:
        return True
    return False
string_items = filter(get_string_lists, objects)
print(list(string_items))

#Use reduce to sum all the numbers in the numbers list.
print("Use reduce to sum all the numbers in the numbers list.")
def sum(x, y):
    return x + y
sum_numbers = reduce(sum, numbers)
print(sum_numbers)

#Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
print("Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries")
def concatenate(x, y):
    return x + ", " + y
concatenated_countries = reduce(concatenate, countries)
print(concatenated_countries + " are north European countries")

#Declare a function called categorize_countries that returns a list of countries with some common pattern (you can find the countries list in this repository as countries.js(eg 'land', 'ia', 'island', 'stan')).
print("Declare a function called categorize_countries that returns a list of countries with some common pattern (you can find the countries list in this repository as countries.js(eg 'land', 'ia', 'island', 'stan')).")
import countries as c
countries = c.countries
def categorize_countries(countries, pattern):
    return list(filter(lambda country: pattern in country, countries))
print(categorize_countries(countries, "land"))
print(categorize_countries(countries, "ia"))
print(categorize_countries(countries, "island"))    
print(categorize_countries(countries, "stan"))

#Create a function returning a dictionary, where keys stand for starting letters of countries and values are the number of country names starting with that letter.
print("Create a function returning a dictionary, where keys stand for starting letters of countries and values are the number of country names starting with that letter.")
def country_dict(countries):
    country_dict = {}
    for country in countries:
        first_letter = country[0].upper()
        if first_letter in country_dict:
            country_dict[first_letter] += 1
        else:
            country_dict[first_letter] = 1
    return country_dict
print(country_dict(countries))

#Declare a get_first_ten_countries function - it returns a list of first ten countries from the countries.js list in the data folder.
print("Declare a get_first_ten_countries function - it returns a list of first ten countries from the countries.js list in the data folder.")
def get_first_ten_countries(countries):
    return countries[:10]
print(get_first_ten_countries(countries))

#Declare a get_last_ten_countries function that returns the last ten countries in the countries list.
print("Declare a get_last_ten_countries function that returns the last ten countries in the countries list.")
def get_last_ten_countries(countries):
    return countries[-10:]
print(get_last_ten_countries(countries)) 

print("revisado")