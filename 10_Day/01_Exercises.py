#Exercises: Level 1

#1- Iterate 0 to 10 using for loop, do the same using while loop.
print("1- Iterate 0 to 10 using for loop, do the same using while loop.")
numbers = [0,1,2,3,4,5,6,7,8,9,10]
for number in numbers:
    print(number)
print("-----------------------")

for i in range(11):
    print(i)
print("------------------------------")  

count = 0
while count < 10:
    print(count)
    count = count + 1
else:
    print(count)
print("--------------------------------")

i = 0
while i < 11:
    print(i)
    i += 1
print("")

#2- Iterate 10 to 0 using for loop, do the same using while loop.
print("2- Iterate 10 to 0 using for loop, do the same using while loop.")

numbers = (10,9,8,7,6,5,4,3,2,1,0)
for number in numbers:
    print(number)
print("------------------------")

i=10
while i > -1:
    print(i)
    i -= 1

#3- Write a loop that makes seven calls to print(), so we get on the output the following triangle
  #
  ##
  ###
  ####
  #####
  ######
  #######
print("3- Write a loop that makes seven calls to print(), so we get on the output the following triangle with #")
for i in range(8):
    print("#"*i)

#4- Use nested loops to create the following:
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #

print("4- Use nested loops to create the following:")
n = 8 #Filas
m = 8 #Columnas

for i in range(n): 
    print("# "*m)

#5- Print the following pattern:
#0 x 0 = 0
#1 x 1 = 1
#2 x 2 = 4
#3 x 3 = 9
#4 x 4 = 16
#5 x 5 = 25
#6 x 6 = 36
#7 x 7 = 49
#8 x 8 = 64
#9 x 9 = 81
#10 x 10 = 100

print("5- Print the following pattern:")
for i in range(11):
    print(f"{i} x {i} = {i*i}")

#6- Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
print("Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.")
items = ['Python', 'Numpy','Pandas','Django', 'Flask']
for item in items:
    print(item)

#7- Use for loop to iterate from 0 to 100 and print only even numbers
print("7- Use for loop to iterate from 0 to 100 and print only even numbers")
for i in range(101):
    if i % 2 == 0:
        print(i)

#8- Use for loop to iterate from 0 to 100 and print only odd numbers
print("8- Use for loop to iterate from 0 to 100 and print only odd numbers")
for i in range(101):
    if i % 2 == 1:
        print(i)


print("revisado")