
#LONGITUD DE TU NOMBRE 
nombre = "Jhony"  
longitud_nombre = len(nombre)
print("La longitud de tu nombre es:", longitud_nombre)

#COMPRARAR NOMBRE Y APELLIDO
apellido = "Flores"  
longitud_apellido = len(apellido)
Diferencia = longitud_nombre - longitud_apellido
print("Diferencia de longitud entre nombre y apellido:", Diferencia)



num1 = 5
num2 = 4

# SUMA
total = num1 + num2
print("La suma es:", total)

# RESTA
dif = num1 - num2
print("La diferencia es:", dif)

# MULTIPLICACION
producto = num1 * num2
print("El producto es:", producto)

# DIVISION
division = num1 / num2
print("La división es:", division)

# MODULO
resto = num1 % num2
print("El resto es:", resto)

# POTENCIA
exp = num1 % num2
print("El resultado de la potencia es:", exp)

# DIVISION ENTERA
Division_entera = num1 // num2
print("La división entera es:", Division_entera)



# RADIO DEL CIRCULO
import math

radio = 10

area_del_circulo = math.pi * (radio ** 2)
print("El área del círculo es:", area_del_circulo )

circunferencia = 2 * math.pi * radio
print("La circunferencia del círculo es:", circunferencia)

radio_usuario = float(input("Introduce el radio del círculo: "))
area_usuario = math.pi * (radio_usuario ** 2)
print("El área del círculo con tu radio es:", area_usuario)



nombre_usuario = input("Introduce tu nombre: ")
apellido_usuario = input("Introduce tu apellido: ")
pais_usuario = input("Introduce tu país: ")
edad_usuario = int(input("Introduce tu edad: "))

print("Tu nombre es:", nombre_usuario)
print("Tu apellido es:", apellido_usuario)
print("Tu país es:", pais_usuario)
print("Tu edad es:", edad_usuario)
