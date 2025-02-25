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
print(companies.split(','))

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
