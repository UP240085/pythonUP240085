#Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
print("Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list")
def shuffle_list(lst):
    import random
    shuffled = lst[:]
    random.shuffle(shuffled)
    return shuffled
print("Original List:", [1, 2, 3, 4, 5])
print("Shuffled List:", shuffle_list([1, 2, 3, 4, 5]))

#Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.
print("Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.")
def unique_random_numbers(n=7, start=0, end=9):
    import random
    if n > (end - start + 1):
        raise ValueError("n must be less than or equal to the range of numbers")
    return random.sample(range(start, end + 1), n)
print("Unique Random Numbers:", unique_random_numbers(7, 0, 9))