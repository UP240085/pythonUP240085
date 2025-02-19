#Día 3 
#1- Declarar edad como int
print("1- Declarar edad como int")
edad = int(input("Ingresa tú edad: "))
print(type(edad))

#2- Declarar estaura como float
print("2- Declarar estaura como float")
estatura = float(input("Ingresa tú estatura: "))
print(type(estatura))

#3- Declarar variable con numero complejo
print("3- Declarar variable con numero complejo")
complejo = 2+3j
print(complejo)
print(type(complejo))

#4- Área triángulo
print("4- Área triángulo")
base = float(input("Ingresa el valor de la base: "))
altura = float(input("Ingresa la altura: ")) 
área = 0.5 * base * altura
print("El área del triángulo es:",área)

#5- Perímetro de un triángulo
print("5- Perímetro de un triángulo")
lado = float(input("Ingresa el primer valor: "))
lado2 = float(input("Ingresa el segundo lado: "))
lado3 = float(input("Ingresa el tercer valor: "))
per = lado + lado2 + lado3 
print("El perímetro del triángulo es:",per)

#6- Cálculos de un rectángulo
print("6- Cálculos de un rectángulo")
largo = float(input("Ingresa el largo del rectángulo: "))
ancho = float(input("Ingresa el ancho del rectángulo: "))
área = largo * ancho
per = 2*(largo + ancho)
print("El perímetro de tu rectángulo es:",per)
print("El área del triángulo es:",área)

#7- Cálculos de un círculo
print("7- Cálculos de un círculo")
radio = float(input("Ingresa el radio del círculo: "))
área = 3.1416 * radio**2
circunferencia = 2 * 3.1416 * radio
print("El área del círculo es:",área)
print("La circunferencia del círculo es:",circunferencia)

#8- Cálculos de pendiente
print("8- Cálculos de pendiente y = 2x - 2")
# Ecuación de la línea: y = 2x - 2
m = 2  # Pendiente
y_intercept = -2  # Intersección con el eje y
x_intercept = -y_intercept / m  # Intersección con el eje x

print("La pendiente (m) es:", m)
print("La intersección con el eje y es:", y_intercept)
print("La intersección con el eje x es:", x_intercept)

#9- Cálculo de la pendiente y distancia euclidiana entre dos puntos
print("9- Cálculo de la pendiente y distancia euclidiana entre (2, 2) y (6, 10)")
x1 = 2
y1 = 2
x2 = 6
y2 = 10

# Pendiente
pendiente = (y2 - y1) / (x2 - x1)
print("La pendiente entre los puntos es:", pendiente)

# Distancia euclidiana
distancia = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
print("La distancia euclidiana entre los puntos es:", distancia)

#10- Comparación de pendientes
print("10- Comparación de pendientes")

comparación = m>=pendiente
print("La pendiente de la ecuación y = 2x - 2 es mayor o igual a la pendiente entre los puntos (2, 2) y (6, 10):", comparación)
comparación = m<=pendiente
print("La pendiente de la ecuación y = 2x - 2 es menor o igual a la pendiente entre los puntos (2, 2) y (6, 10):", comparación) 
comparación = m==pendiente
print("La pendiente de la ecuación y = 2x - 2 es igual a la pendiente entre los puntos (2, 2) y (6, 10):", comparación)
comparación = m!=pendiente
print("La pendiente de la ecuación y = 2x - 2 es diferente a la pendiente entre los puntos (2, 2) y (6, 10):", comparación) 
comparación = m>pendiente   
print("La pendiente de la ecuación y = 2x - 2 es mayor a la pendiente entre los puntos (2, 2) y (6, 10):", comparación)
comparación = m<pendiente
print("La pendiente de la ecuación y = 2x - 2 es menor a la pendiente entre los puntos (2, 2) y (6, 10):", comparación)

#11- Cálculo de y = x^2 + 6x + 9 para diferentes valores de x
print("Cálculo de y = x^2 + 6x + 9 para diferentes valores de x")
def calcular_y(x):
    return x**2 + 6*x + 9

# Probar diferentes valores de x
valores_x = [-5, -4, -3, -2, -1, 0, 1, 2, 3]
for x in valores_x:
    y = calcular_y(x)
    print(f"Para x = {x}, y = {y}")

# Solicitar un valor de x al usuario
x = float(input("Ingresa el valor de x: "))
y = calcular_y(x)
print("El valor de y es:", y)