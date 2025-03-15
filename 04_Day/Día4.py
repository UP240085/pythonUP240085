#1- Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
print("1- Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.")
string1 = 'Thirty'
string2 = 'Days'
string3 = 'Of'
string4 = 'Python'
title = string1 + ' ' + string2 + ' ' + string3 + ' ' + string4
print(title)

#2- Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
print("2- Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.")
string1 = 'Coding'
string2 = 'For'
string3 = 'All'
sentence = string1 + ' ' + string2 + ' ' + string3
print(sentence)

#3- Declare a variable named company and assign it to an initial value "Coding For All".
print("3.- Declare a variable named company and assign it to an initial value 'Coding For All'.")
company = "Coding For All"

#4- Print the variable company using print().
print("4- Print the variable company using print().")
print(company)

#5- Print the length of the company string using len() method and print().
print("5- Print the length of the company string using len() method and print().")
print(len(company))

#6- Change all the characters to uppercase letters using upper() method.
print("6- Change all the characters to uppercase letters using upper() method.")
print(company.upper())

#7- Change all the characters to lowercase letters using lower() method.
print("7- Change all the characters to lowercase letters using lower() method.")
print(company.lower())

#8- Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print("8- Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.")
print(company.capitalize())
print(company.title())
print(company.swapcase())

#9- Cut(slice) out the first word of Coding For All string.
print("9- Cut(slice) out the first word of Coding For All string.")
print(company[0:6])

#10- Check if Coding For All string contains a word Coding using the method index, find or other methods.
print("10- Check if Coding For All string contains a word Coding using the method index, find or other methods.")
print(company.index('Coding'))
print(company.find('Coding'))
print('Coding' in company)
print(company.startswith('Coding'))

#11- Replace the word coding in the string 'Coding For All' to Python.
print("11- Replace the word coding in the string 'Coding For All' to Python.")
print(company.replace('Coding', 'Python'))

#12- Change Python for Everyone to Python for All using the replace method or other methods.
print("12- Change Python for Everyone to Python for All using the replace method or other methods.")
sentence = "Python for Everyone"
print(sentence.replace('Everyone', 'All'))

#13- Split the string 'Coding For All' using space as the separator (split())
print("13- Split the string 'Coding For All' using space as the separator (split())")
print(company.split())

#14- "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
print("14- 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon' split the string at the comma.")
companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(companies.split(","))

#15- What is the character at index 0 in the string Coding For All.
print("15- What is the character at index 0 in the string Coding For All.")
print(company[0])

#16- What is the last index of the string Coding For All.
print("16- What is the last index of the string Coding For All.")
print(company[-1])

#17- What character is at index 10 in "Coding For All" string.
print("17- What character is at index 10 in 'Coding For All' string.")
print(company[10])

#18- Create an acronym or an abbreviation for the name 'Python For Everyone'.
print("18- Create an acronym or an abbreviation for the name 'Python For Everyone'.")
sentence = "Python For Everyone"
acronym = sentence[0] + sentence[7] + sentence[11]
print(acronym)

#19- Create an acronym or an abbreviation for the name 'Coding For All'.
print("19- Create an acronym or an abbreviation for the name 'Coding For All'.")
company = "Coding For All"
acronym = company[0] + company[7] + company[11]
print(acronym)

#20- Use index to determine the position of the first occurrence of C in Coding For All.
print("20- Use index to determine the position of the first occurrence of C in Coding For All.")
print(company.index('C'))

#21- Use index to determine the position of the first occurrence of F in Coding For All.
print("21- Use index to determine the position of the first occurrence of F in Coding For All.")
print(company.index('F'))

#22- Use rfind to determine the position of the last occurrence of l in Coding For All People.
print("22- Use rfind to determine the position of the last occurrence of l in Coding For All People.")
sentence = "Coding For All People"
print(sentence.rfind('l'))

#23- Use index or find to find the position of the first occurrence of the word 'because' in the following sentence:\n'You cannot end a sentence with because because because is a conjunction'
print("23- Use index or find to find the position of the first occurrence of the word 'because' in the following sentence:\n'You cannot end a sentence with because because because is a conjunction'")
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.index('because'))

#24- Use rindex to find the position of the last occurrence of the word because in the following sentence:\n'You cannot end a sentence with because because because is a conjunction'
print("24- Use rindex to find the position of the last occurrence of the word because in the following sentence:\n'You cannot end a sentence with because because because is a conjunction'")
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.rindex('because'))

#25- Slice out the phrase 'because because because' in the following sentence:\n'You cannot end a sentence with because because because is a conjunction'
print("25- Slice out the phrase 'because because because' in the following sentence:\n'You cannot end a sentence with because because because is a conjunction'")
sentence = 'You cannot end a sentence with because because because is a conjunction'
word = 'because'
firstWordPos = sentence.index(word)
lastWordPos = sentence.rindex(word) + len(word)+1
print(sentence)
print(sentence[firstWordPos:lastWordPos])

#26- Find the position of the first occurrence of the word 'because' in the following sentence:\n'You cannot end a sentence with because because because is a conjunction'
print("26- Find the position of the first occurrence of the word 'because' in the following sentence:\n'You cannot end a sentence with because because because is a conjunction'")
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.find('because'))

#27- Slice out the phrase 'because because because' in the following sentence:\n'You cannot end a sentence with because because because is a conjunction'
print("27- Slice out the phrase 'because because because' in the following sentence:\n'You cannot end a sentence with because because because is a conjunction'")
sentence = 'You cannot end a sentence with because because because is a conjunction'
word = 'because'
firstWordPos = sentence.find(word)
lastWordPos = sentence.rfind(word) + len(word)+1
print(sentence)
print(sentence[firstWordPos:lastWordPos])

#28- Does ''Coding For All' start with a substring Coding?
print("28- Does 'Coding For All' start with a substring Coding?")
print(company.startswith('Coding'))

#29- Does 'Coding For All' end with a substring coding?
print("29- Does 'Coding For All' end with a substring coding?")
print(company.endswith('coding'))

#30- '   Coding For All      '  , remove the left and right trailing spaces in the given string.
print("30- '   Coding For All      '  , remove the left and right trailing spaces in the given string.")
sentence = '   Coding For All      '
print(sentence.strip())

#31- Which one of the following variables return True when we use the method isidentifier():\n30DaysOfPython, thirty_days_of_python
print("31- Which one of the following variables return True when we use the method isidentifier():\n30DaysOfPython, thirty_days_of_python")
print('30DaysOfPython'.isidentifier())
print('thirty_days_of_python'.isidentifier())
print('thirty days of python' + " is a valid variable name")

#32- The following list contains the names of some of python libraries:\n['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']\nJoin the list with a hash with space string.
print("32- The following list contains the names of some of python libraries:\n['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']\nJoin the list with a hash with space string.")
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print('# '.join(libraries))

#33- Use the new line escape sequence to separate the following sentence into two lines. I am enjoying this challenge.I just wonder what is next.
print("33- Use the new line escape sequence to separate the following sentence into two lines. I am enjoying this challenge.I just wonder what is next.")
sentence = "I am enjoying this challenge.\nI just wonder what is next."
print(sentence)

#34- Use a tab escape sequence to write the following lines.
#Name      Age     Country  City
#Asabeneh  250     Finland Helsinki
print("34- Use a tab escape sequence to write the following lines.")
print("Name, Age, Country, City")
print("Asabeneh, 250, Finland, Helsinki")
print("Tab escape sequence: ")
print("\tName\t\tAge\tCountry\t\tCity")
print("\tAsabeneh\t250\tFinland\t\tHelsinki")

#35- Use the string formatting method to display the following:\nradius = 10 \narea = 3.14 * radius ** 2 \nThe area of a circle with radius 10 is 314 meters square.
print("35- Use the string formatting method to display the following:radius = 10 area = 3.14 * radius ** 2 The area of a circle with radius 10 is 314 meters square.")
print("\nradius = 10 \narea = 3.14 * radius ** 2 \nThe area of a circle with radius 10 is 314 meters square.")

#36- Operation formatting method
print("36- Operation formatting method")
num1 = 8
num2 = 6
print(f'{num1} + {num2} = {num1 + num2}')
print(f'{num1} - {num2} = {num1 - num2}')
print(f'{num1} * {num2} = {num1 * num2}')
print(f'{num1} / {num2} = {num1 / num2}')
print(f'{num1} % {num2} = {num1 % num2}')
print(f'{num1} // {num2} = {num1 // num2}')
print(f'{num1} ** {num2} = {num1 ** num2}')

