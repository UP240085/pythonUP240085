#Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
print("Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.")

def evens_and_odds(n):
    even_count = 0
    odd_count = 0
    for i in range(n + 1):
        if i % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return even_count, odd_count
print(evens_and_odds(100))
print(f"Number of evens: {evens_and_odds(100)[0]}, Number of odds: {evens_and_odds(100)[1]}")

#Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
print("Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number")
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))

#Call your function is_empty, it takes a parameter and it checks if it is empty or not
print("Call your function is_empty, it takes a parameter and it checks if it is empty or not")
def is_empty(lst):
    if len(lst) == 0:
        return True
    else:
        return False
print(is_empty([]))

#Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).
print("Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).")
def calculate_mean(lst):
    return sum(lst) / len(lst)
def calculate_median(lst):
    lst.sort()
    n = len(lst)
    if n % 2 == 0:
        return (lst[n // 2 - 1] + lst[n // 2]) / 2
    else:
        return lst[n // 2]
def calculate_mode(lst):
    mode = max(lst, key=lst.count)
    return mode
def calculate_range(lst):
    return max(lst) - min(lst)
def calculate_variance(lst):
    mean = calculate_mean(lst)
    variance = sum((x - mean) ** 2 for x in lst) / len(lst)
    return variance
def calculate_std(lst):
    variance = calculate_variance(lst)
    return variance ** 0.5
print(calculate_mean([1, 2, 3, 4, 5]))
print(calculate_median([1, 2, 3, 4, 5]))
print(calculate_mode([1, 2, 3, 4, 5, 5]))
print(calculate_range([1, 2, 3, 4, 5]))
print(calculate_variance([1, 2, 3, 4, 5]))
print(calculate_std([1, 2, 3, 4, 5]))

print("revisado")