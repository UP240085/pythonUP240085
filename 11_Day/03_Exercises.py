#Write a function called is_prime, which checks if a number is prime.
# A prime number is a number that is only divisible by 1 and itself.
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
print(is_prime(7))  

#Write a functions which checks if all items are unique in the list.
def are_items_unique(lst):
    return len(lst) == len(set(lst))
print(are_items_unique([1, 2, 3, 4, 5]))

#Write a function which checks if all the items of the list are of the same data type.
def are_items_same_type(lst):
    return all(isinstance(item, type(lst[0])) for item in lst)
print(are_items_same_type([1, 2, 3, 4, 5]))

#Write a function which check if provided variable is a valid python variable
def is_valid_variable(variable):
    return variable.isidentifier()
print(is_valid_variable("my_variable"))

#Go to the data folder and access the countries-data.py file.
#Create a function called the most_spoken_languages in the world. It should return 10 or 20 most spoken languages in the world in descending order
# based on the countries data.
import data as cd
from collections import Counter
data = cd.data
def most_spoken_languages(data, n=20):
    language_counter = Counter()
    for country in data:
        for language in country["languages"]:
            language_counter[language] += 1
    most_common_languages = language_counter.most_common(n)
    return most_common_languages
print("The most spoken languages are:")
for language, count in most_spoken_languages(data, 20):
    print(f"{language}: {count}")

#Create a function called the most_populated_countries. It should return 10 or 20 most populated countries in descending order.
# based on the countries data.
def most_populated_countries(data, n=20):
    countries_population = {country["name"]: country["population"] for country in data}
    most_populated = sorted(countries_population.items(), key=lambda item: item[1], reverse=True)
    return most_populated[:n]
print("The most populated countries are:")
for country, population in most_populated_countries(data, 20):
    print(f"{country}: {population}")