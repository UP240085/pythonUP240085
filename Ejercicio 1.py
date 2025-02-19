#Día 3 
#Área triángulo
base = float(input("Ingresa el valor de la base: "))
altura = float(input("Ingresa la altura: ")) 
área = 0.5 * base * altura
print("El área del triángulo es:",área)

#Perímetro de un triángulo
lado = float(input("Ingresa el primer valor: "))
lado2 = float(input("Ingresa el segundo lado: "))
lado3 = float(input("Ingresa el tercer valor: "))
per = lado + lado2 + lado3 
print("El perímetro del triángulo es:",per)

#Cálculos de un rectángulo
largo = float(input("Ingresa el largo del rectángulo: "))
ancho = float(input("Ingresa el ancho del rectángulo: "))
área = largo * ancho
per = 2*(largo + ancho)
print("El perímetro de tu rectángulo es:",per)
print("El área del triángulo es:",área)