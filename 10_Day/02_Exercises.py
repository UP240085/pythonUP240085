#Use for loop to iterate from 0 to 100 and print the sum of all numbers.
sum = 0
for i in range(101):
    sum = sum + i
print(f"The sum of all numbers is: {sum}")


#Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
even = 0
odd = 0
for i in range(101):
    if i % 2 == 0:
        even = even + i
    else:
        odd = odd + i

print(f"The sum of all evens is: {even} and the sum of all odds is: {odd}")

print("revisado")