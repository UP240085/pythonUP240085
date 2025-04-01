#Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word land.
print("Loop through the countries and extract all the countries containing the word land")
import countries as c
countries = c.countries
land = []
for country in countries:
    if "land" in country:
        land.append(country)
print(land)

#This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
print("This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.")
fruits = ['banana', 'orange', 'mango', 'lemon']
reverse = []
for fruit in fruits:
    reverse.insert(0, fruit)
print(reverse)

#Go to the data folder and use the countries_data.py file
#What are the total number of languages in the data
import data as cd
data = cd.data
print("What are the total number of languages in the data")
languages = set()
for country in data:
    for language in country["languages"]:
        languages.add(language)
print(f"The total number of languages in the data is: {len(languages)}")

#Find the ten most spoken languages from the data
print("Find the ten most spoken languages from the data") 
from collections import Counter #https://docs-python-org.translate.goog/3/library/collections.html?_x_tr_sl=en&_x_tr_tl=es&_x_tr_hl=es&_x_tr_pto=tc
language_counter = Counter()
for country in data:
    for language in country["languages"]:
        language_counter[language] += 1
most_common_languages = language_counter.most_common(10)
print(f"The ten most spoken languages are: {most_common_languages}")
print("The ten most spoken languages are:")
for language, count in most_common_languages:
    print(f"{language}: {count}")

#Find the 10 most populated countries in the world
