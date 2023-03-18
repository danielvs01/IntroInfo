# Ejercicio 1
# Escribir un programa que muestre por pantalla la cadena ¡Hola Mundo!.

print("¡Hola Mundo!")

print("///////////////////////")

# Ejercicio 2
# Escribir un programa que almacene la cadena ¡Hola Mundo! en una variable y luego muestre por pantalla el contenido de la variable.

text = "¡Hola Mundo!"
print(text)

print("///////////////////////")

# Ejercicio 3
# Escribir un programa que almacene el nombre del usuario en la consola y después de que muestre por pantalla la cadena ¡Hola <nombre>!, donde <nombre> es el nombre que el usuario.

name = "Daniel"
print("¡Hola " + (name) + "!")

print("///////////////////////")

# Ejercicio 4
# Escribir un programa que muestre por pantalla el resultado de la siguiente operación aritmética

a = 3
b = 2
c = 5
resultado = ((a + b) / (b * c)) ** b
print("El resultado de la operación ((3+2)/(2⋅5))^2 es:", resultado)

print("///////////////////////")

# Ejercicio 5

# Escribir un programa que pregunte almacene el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.

horas = 48
coste_hora = 20
pago = horas * coste_hora
print("El pago por las horas trabajadas son: " , "$" , (pago)) 

print("///////////////////////")

# Ejercicio 6
# Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.

peso = 80
estatura = 1.80
imc = peso / estatura
imc_2 = round(imc, 2)
print("Tu índice de masa corporal es: " , (imc_2))

print("///////////////////////")

# Ejercicio 7
# Escribir un programa donde almacenas dos números enteros y muestre por pantalla la <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m> son los números almacenados, y <c> y <r> son el cociente y el resto de la división entera respectivamente.

n = 8
m = 10
c = n / m
r = n % m
print(n, "entre", m, "da el cociente", c, "y el resto", r)