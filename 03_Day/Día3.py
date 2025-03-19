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

#12- Largo de "python" y "dragon" y falsa comparación
print("12- Largo de 'python' y 'dragon' y falsa comparación") 
len_python = len('python')
len_dragon = len('dragon')
falsy_comparison = len_python == len_dragon
print(f"Length of 'python': {len_python}")
print(f"Length of 'dragon': {len_dragon}")
print(f"Falsy comparison (length of 'python' == length of 'dragon'): {falsy_comparison}")

# 13- Checar si "on" está en "python" y "dragon"
print("13- Checar si 'on' está en 'python' y 'dragon'")
on_in_both = 'on' in 'python' and 'on' in 'dragon'
print(f"'on' in both 'python' and 'dragon': {on_in_both}")

# 14- Checar si "jargon" está en la frase
print("14- Checar si 'jargon' está en la frase")
frase = "I hope this course is not full of jargon"
jargon_in_frase = 'jargon' in frase
print(f"'jargon' in the frase: {jargon_in_frase}")

# 15- No hay "on" en "python" y "dragon"
print("15- No hay 'on' en 'python' y 'dragon'")
no_on_in_both = 'on' not in 'python' and 'on' not in 'dragon'
print(f"'on' not in both 'python' and 'dragon': {no_on_in_both}")

#16- Convertir la longitud de "python" a float y luego a string
print("16- Convertir la longitud de 'python' a float y luego a string")
len_python = len('python')
len_python = float(len_python)
print(type(len_python))
len_python = str(len_python)
print(type(len_python))
print(f"Length of 'python' as string: {len_python}")
print(type(len_python))

#17- Checar si un número es par
print("17- Checar si un número es par")
numero = int(input("Ingresa un número: "))
es_par = numero % 2 == 0
print(f"El número {numero} es par: {es_par}")

#18- Check if floor division of 7 by 3 is equal to int converted value of 2.7 
print("18- Check if floor division of 7 by 3 is equal to int converted value of 2.7")
floor_division = 7 // 3
int_conversion = int(2.7)
equal = floor_division == int_conversion
print(f"Floor division of 7 by 3: {floor_division}")
print(f"Int converted value of 2.7: {int_conversion}")
print(f"Equal: {equal}")

#19- Checar si el tipi de "10" es igual al tipo de 10
print("19- Checar si el tipo de '10' es igual al tipo de 10")
type_comparison = type('10') == type(10)
print(f"Type of '10' is equal to type of 10: {type_comparison}")

#20-Checar si int("9.8") es igual a 10
print("20-Checar si int('9.8') es igual a 10")
try:
    int_value = int('9.8')
except ValueError:
    int_value = None
comparison = int_value == 10
print(f"int('9.8') is equal to 10: {comparison}")

#21- Calcular pago basado en horas y tarifa por hora
print("21- Calcular pago basado en horas y tarifa por hora")
horas = float(input("Ingresa el número de horas trabajadas: "))
tarifa = float(input("Ingresa la tarifa por hora: "))
pago = horas * tarifa
print(f"El pago es: {pago}")
 
#22- Escribe un script que le pida al usuario que ingrese el número de años.
#  Calcula el número de segundos que una persona puede vivir. 
print("22- Calcular el número de segundos que una persona puede vivir")
años = int(input("Ingresa el número de años: "))
segundos_por_año = 365 * 24 * 60 * 60
segundos_vividos = años * segundos_por_año
print(f"Una persona puede vivir {segundos_vividos} segundos")

#23- Script para mostrar tabla 
print("23- Script para mostrar tabla")

print("1 1 1 1 1")
print("2 1 2 4 8")
print("4 1 4 16 64")
print("5 1 5 25 125")

