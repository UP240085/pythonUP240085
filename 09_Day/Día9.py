#Conditionals
#Exercises: Level 1

#1- Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. 
print("1- Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years.")
age = int(input("Enter your age: "))
if age >= 18:
    print("You are old enough to drive")
else:
    print(f"Wait for {18 - age} years")

#2- Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. 
print("2- Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age.")
my_age = 18
your_age = int(input("Enter your age: "))
if my_age > your_age:
    print(f"I am {my_age - your_age} years older than you")
elif my_age < your_age:
    print(f"You are {your_age - my_age} years older than me")
else:
    print("We are the same age")
