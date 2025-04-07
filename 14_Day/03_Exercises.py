#Use the countries_data.py (https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries-data.py) file and follow the tasks below:

#Sort out the ten most populated countries.

from data import data
# Sort countries by name, by capital, by population
def sort_countries(data, key):
    return sorted(data, key=lambda x: x[key])

# Obtener solo los nombres de los países ordenados
sorted_by_name = [country['name'] for country in sort_countries(data, 'name')]
sorted_by_capital = [country['name'] for country in sort_countries(data, 'capital')]
sorted_by_population = [country['name'] for country in sort_countries(data, 'population')]

# Imprimir los primeros 10 resultados
print("Sorted by name:", sorted_by_name[:10])
print("Sorted by capital:", sorted_by_capital[:10])
print("Sorted by population:", sorted_by_population[:10])

#Sort out the ten most spoken languages by location.
def sort_languages(data):
    languages = {}
    for country in data:
        for language in country['languages']:
            if language not in languages:
                languages[language] = 0
            languages[language] += 1
    return sorted(languages.items(), key=lambda x: x[1], reverse=True)
print("Most spoken languages:", sort_languages(data)[:10])

#Sort out the ten most populated countries.
def sort_population(data):
    return sorted(data, key=lambda x: x['population'], reverse=True)
print("Most populated countries:", [country['name'] for country in sort_population(data)[:10]])


print("revisado")