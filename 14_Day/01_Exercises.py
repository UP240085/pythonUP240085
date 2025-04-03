countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#Explain the difference between map, filter, and reduce.
print("Explain the difference between map, filter, and reduce.")
print("\'Map\' transforma todos los elementos")
print("\'Filtrer\' selecciona elementos basados en una condición.")
print("\'Reduce\' combina todos los elementos en un solo valor.")

#Explain the difference between higher order function, closure and decorator
print("Explain the difference between higher order function, closure and decorator.")
print("\'Higher order function\' es una función que toma otra función como argumento o devuelve una función.")
print("\'Closure\' es una función que recuerda el entorno en el que fue creada.")
print("\'Decorator\' es una función que toma otra función y extiende su comportamiento sin modificarla.")

#Define a call function before map, filter or reduce, see examples.
print("Call function before map, filter or reduce:")
print("Map:")

def square(x):
    return x ** 2
numbers_squared = map(square, numbers)
print(list(numbers_squared))

numbers_squared = map(lambda x : x ** 2, numbers)
print(list(numbers_squared)) 

print("Filter:")
def is_even(num):
    if num % 2 == 0:
        return True
    return False

even_numbers = filter(is_even, numbers)
print(list(even_numbers))     

even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))


#Use for loop to print each country in the countries list.
print("Use For loop to print each country in the countries list.")
for country in countries:
    print(country)

#Use for to print each name in the names list.
print("Use For loop to print each name in the names list.")
for name in names:
    print(name)

#Use for to print each number in the numbers list.
print("Use For loop to print each number in the numbers list.")
for number in numbers:
    print(number)