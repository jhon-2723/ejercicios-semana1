#LONGITUD
texto = "python"
longitud = len(texto)
longitud_float = float(longitud)
longitud_str = str(longitud_float)
print(longitud_str) 

#PAR O IMPAR
numero = int(input("Introduce un número: "))
if numero % 2 == 0:
    print(f"{numero} es un número par.")
else:
    print(f"{numero} es un número impar.")

# DIVISION DE ENTERO
division_entera = 7 // 3
entero= int(2.7)
resultado = division_entera == entero
print(resultado)  

#CMPARACION
comparacion = type('9.8') == type(10)
print(comparacion)  

#SALARIO
horas = float(input("Introduce las horas trabajadas: "))
tarifa = float(input("Introduce la tarifa por hora: "))
salario_semanal = horas * tarifa
print(f"Tu salario semanal es {salario_semanal}")

#AÑOS VIVODOS
años_de_vivencia = int(input("Introduce el número de años que has vivido: "))
segundos_por_año = 365 * 24 * 60 * 60
segundos_vividos = años_de_vivencia * segundos_por_año
print(f"Has vivido durante {segundos_vividos} segundos.")


for i in (1, 6):
    print(f"{i} {1} {i} {i**2} {i**3}")


cadena = input("Introduce una cadena: ")
cadena_invertida = cadena[::-1]
print("Cadena invertida:", cadena_invertida)


cadena = input("Introduce una cadena: ")
vocales = "aeiouAEIOU"
contador_vocales = sum(1 for char in cadena if char in vocales)
print("Número de vocales en la cadena:", contador_vocales)


cadena = input("Introduce una cadena: ").replace(" ", "").lower()
es_palindromo = cadena == cadena[::-1]
if es_palindromo:
    print("La cadena es un palíndromo.")
else:
    print("La cadena no es un palíndromo.")


cadena = input("Introduce una cadena: ")
cadena_reemplazada = cadena.replace(" ", "_")
print("Cadena con espacios reemplazados:", cadena_reemplazada)

cadena = input("Introduce una cadena: ")
palabras = cadena.split()
num_palabras = len(palabras)
print("Número de palabras en la cadena:", num_palabras)


cadena = input("Introduce una cadena: ")
mayusculas = cadena.upper()
minusculas = cadena.lower()
print("En mayúsculas:", mayusculas)
print("En minúsculas:", minusculas)


cadena = input("Introduce una cadena: ")
cadena_sin_espacios = cadena.strip()
print("Cadena sin espacios al principio y al final:", cadena_sin_espacios)


cadena = input("Introduce una cadena: ")
inicio = int(input("Introduce el índice de inicio: "))
fin = int(input("Introduce el índice de fin: "))
subcadena = cadena[inicio:fin]
print("Subcadena extraída:", subcadena)



cadena = input("Introduce una cadena: ")
prefijo = input("Introduce el prefijo a verificar: ")
sufijo = input("Introduce el sufijo a verificar: ")

empieza_con_prefijo = cadena.startswith(prefijo)
termina_con_sufijo = cadena.endswith(sufijo)

print(f"¿La cadena empieza con '{prefijo}'?:", empieza_con_prefijo)
print(f"¿La cadena termina con '{sufijo}'?:", termina_con_sufijo)


