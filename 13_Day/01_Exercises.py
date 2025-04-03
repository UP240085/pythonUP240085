#Filter only negative and zero in the list using list comprehension
print("Filter only negative and zero in the list using list comprehension")
def filter_negative_zero(lst):
    return [x for x in lst if x <= 0]
print("Original List:", [1, -2, 3, -4, 5, 0])
print("Filtered List:", filter_negative_zero([1, -2, 3, -4, 5, 0]))

#Flatten the following list of lists of lists to a one dimensional list :
print("Flatten the following list of lists of lists to a one dimensional list")
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
def flatten_list(lst):
    return [item for sublist1 in lst for sublist2 in sublist1 for item in sublist2]
print("Flattened List:", flatten_list(list_of_lists))

#"Using list comprehension create the following list of
# [(0, 1, 0, 0, 0, 0, 0),
#(1, 1, 1, 1, 1, 1, 1),
#(2, 1, 2, 4, 8, 16, 32),
#(3, 1, 3, 9, 27, 81, 243),
#(4, 1, 4, 16, 64, 256, 1024),
#(5, 1, 5, 25, 125, 625, 3125),
#(6, 1, 6, 36, 216, 1296, 7776),
#(7, 1, 7, 49, 343, 2401, 16807),
#(8, 1, 8, 64, 512, 4096, 32768),
#(9, 1, 9, 81, 729, 6561, 59049),
#(10, 1, 10, 100, 1000, 10000, 100000)]

def generate_list():
    return [(i, *(i**j for j in range(7))) for i in range(11)]
print("Generated List:")
print(generate_list())

#Flatten the following list to a new list:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
#output:
#[['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flattened_countries = [[country.upper(), country[:3].upper(), capital.upper()] for sublist in countries for country, capital in sublist]
print(flattened_countries)

#Change the following list to a list of dictionaries:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
#output:
#[{'country': 'FINLAND', 'city': 'HELSINKI'},
#{'country': 'SWEDEN', 'city': 'STOCKHOLM'},
#{'country': 'NORWAY', 'city': 'OSLO'}]

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
countries_dict = [{'country': country.upper(), 'city': capital.upper()} for sublist in countries for country, capital in sublist]
print(countries_dict)

#Change the following list of lists to a list of concatenated strings:
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
#output
#['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates']
def concatenate_names(names):
    return [' '.join(name) for sublist in names for name in sublist]    
print(concatenate_names(names))

#Write a lambda function which can solve a slope or y-intercept of linear functions.
print("Write a lambda function which can solve a slope or y-intercept of linear functions.")
slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1) if x2 != x1 else None
print("Slope:", slope(1, 2, 3, 4))
y_intercept = lambda m, x, y: y - m * x if m is not None else None
print("Y-Intercept:", y_intercept(1, 2, 4))