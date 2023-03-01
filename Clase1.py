# String 
name = "Daniel"
last_name = "Vidal"

# Integer
id = 208170796

# Float 
cash = 10.5

# Bool
active = True

# Comparaciones de las variables
# Como verificar si el PIN ingresado por un usuario coincide con su PIN guardado

entered_pin = 5448
expected_pin = 5448

result = entered_pin == expected_pin

print(result)

# Comparaciones con desigualdad. 
# Tenemos que usar el operador !=

result_1 = 1 != 2
print(result_1)

one= 1
two= 2 
print(one == two)
print(one != two)


# Vamos a hacer un interruptor de luz inteligente que apague las luces si es de dia y las encienda si es de noche

print("----------------")
is_day = False
lights_on = not is_day

print("Daytime?")
print(is_day)

print("Lights on?")
print(lights_on)

# Con las comparaciones vamos a hacer un codigo que rastree status de ventas de una tienda de pantalones
print("----------------")

stock = 600
jeans_sold = 500
target = 500

target_hit = jeans_sold == target
print("Hit jeans sale target: ")
print(target_hit)

current_stock = stock - jeans_sold
in_stock = current_stock != 0
print("Jeans in stock: ")
print(in_stock)
print(current_stock)


# Podemos usar comparaciones para verificar si un numero es mayor o menorque otro numero
print("----------------")

print(2 < 100)
print(2 > 100)

print(201 <= 100)
print(2 >= 100)

# Comparaciones de cadenas de texto 

print("----------------")

my_answer = "lowr"
solution = "low"

print(my_answer == solution)
print(my_answer != solution)

# Ejercicio de medidor de frecuencia cardiaca, usando comparaciones para verificar si la frecuencia cardiaca es demasiado baja o alta y le diremos al paciente si debe preocuparse

print("---------------------")

presion = 70
presion_alta = 100
presion_baja= 20


print("Presion baja")
print(presion_baja)
print("Acudir al medico")

print("Presion alta")
print(presion_alta)
print("Acudir al medico")

print("Presion estable")
print(presion)

hearth_rate = 77
too_low = hearth_rate < 60
too_high = hearth_rate >100

print("Hearth rate low")
print(too_low)
print("Hearth rate high")
print(too_high)
