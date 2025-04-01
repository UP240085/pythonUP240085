# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#Exercises: Level 1
print("Exercises: Level 1")

#1- Find the length of the set it_companies
print("1- Find the length of the set it_companies")
print(f"La longitud de \"it_companies\" es: {len(it_companies)} ")

#2- Add 'Twitter' to it_companies
print("2- Add 'Twitter' to it_companies")
it_companies.add("Twitter")
print(it_companies)

#3- Insert multiple IT companies at once to the set it_companies
print("3- Insert multiple IT companies at once to the set it_companies")
it_companies.update(["Tesla", "Nissan"])
print(it_companies)

#Otra forma 
two_companies = ["Aston Martin", "Danonino"]
it_companies.update(two_companies)
print(it_companies)

#4- Remove one of the companies from the set it_companies
print("4- Remove one of the companies from the set it_companies")
it_companies.remove("Danonino")
print(it_companies)
it_companies.discard("Danonino")

#5- What is the difference between remove and discard
print("5- What is the difference between remove and discard")
print("Si el discard no ecnuentra el elemento a eliminar, el programa seguirá, el remove dará un error si no encuentra  el argumento")

#Exercises: Level 2

#1- Join A and B
print("1- Join A and B")
A.union(B)
print(A)

#2- Find A intersection B
print("2- Find A intersection B")
A.intersection(B)
print(A)

#3- Is A subset of B
print("3- Is A subset of B")
A.issubset(B)
print(A)

#4- Are A and B disjoint sets
print("4- Are A and B disjoint sets")
A.isdisjoint(B)
print(A)

#5- Join A with B and B with A
print("5- Join A with B and B with A")
A.union(B)
print(A)
B.union(A)
print(B)

#6- What is the symmetric difference between A and B
print("6- What is the symmetric difference between A and B")
A.symmetric_difference(B)
print(A)

#7- Delete the sets completely
print("7- Delete the sets completely")
del A
del B

print("Revisado")