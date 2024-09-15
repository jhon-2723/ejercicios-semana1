edades = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# EDAD MINIMA Y MAXIMA
edades.sort()
edad_minima = min(edades)
edad_maxima = max(edades)
print(f"Edades ordenadas: {edades}")
print(f"Edad mínima: {edad_minima}")
print(f"Edad máxima: {edad_maxima}")

#  AñadI1r de nuevo lista
edades.append(edad_minima)
edades.append(edad_maxima)
print(f"Lista después de añadir mínima y máxima: {edades}")

# la edad mediana
edades.sort()
longitud = len(edades)
if longitud % 2 == 0:
    mediana = (edades[longitud // 2 - 1] + edades[longitud // 2]) / 2
else:
    mediana = edades[longitud // 2]
print(f"Mediana: {mediana}")

# la edad promedio
promedio = sum(edades) / len(edades)
print(f"Promedio de edades: {promedio}")

# rango de las edades (máximo menos mínimo)
rango_edades = edad_maxima - edad_minima
print(f"Rango de edades: {rango_edades}")

# valor de (mínimo - promedio) y (máximo - promedio), usando abs()
diferencia_min = abs(edad_minima - promedio)
diferencia_max = abs(edad_maxima - promedio)
print(f"Diferencia mínima - promedio: {diferencia_min}")
print(f"Diferencia máxima - promedio: {diferencia_max}")



frase = "Soy profesor y me encanta inspirar y enseñar a la gente"
palabras = frase.split()
palabras_unicas = set(palabras)
print(f"Número de palabras únicas: {len(palabras_unicas)}")
print(f"Palabras únicas: {palabras_unicas}")



# Listas de números
lista1 = list(range(1, 11))   # [1, 2, 3, ..., 10]
lista2 = list(range(5, 16))   # [5, 6, 7, ..., 15]
lista3 = list(range(10, 21))  # [10, 11, 12, ..., 20]

# a. Convierte las listas en conjuntos
set1 = set(lista1)
set2 = set(lista2)
set3 = set(lista3)

print(f"Conjunto 1: {set1}")
print(f"Conjunto 2: {set2}")
print(f"Conjunto 3: {set3}")

# b. Encuentra el conjunto de todos los números que están presentes en las tres listas
conjunto_interseccion = set1 & set2 & set3
print(f"Números presentes en las tres listas: {conjunto_interseccion}")

# c. Encuentra el conjunto de todos los números que están presentes en al menos una de las listas
conjunto_union = set1 | set2 | set3
print(f"Números presentes en al menos una lista: {conjunto_union}")

# d. Encuentra el conjunto de todos los números que están presentes en la primera lista, pero no en la última
conjunto_diferencia = set1 - set3
print(f"Números en la primera lista pero no en la última: {conjunto_diferencia}")

# e. Convierte los conjuntos obtenidos en tuplas y suma el primer y último elemento de cada tupla
tupla_interseccion = tuple(conjunto_interseccion)
tupla_union = tuple(conjunto_union)
tupla_diferencia = tuple(conjunto_diferencia)

# Para evitar errores, verificamos si las tuplas tienen al menos dos elementos
if len(tupla_interseccion) >= 2:
    suma_interseccion = tupla_interseccion[0] + tupla_interseccion[-1]
    print(f"Suma primer y último elemento de la tupla intersección: {suma_interseccion}")

if len(tupla_union) >= 2:
    suma_union = tupla_union[0] + tupla_union[-1]
    print(f"Suma primer y último elemento de la tupla unión: {suma_union}")

if len(tupla_diferencia) >= 2:
    suma_diferencia = tupla_diferencia[0] + tupla_diferencia[-1]
    print(f"Suma primer y último elemento de la tupla diferencia: {suma_diferencia}")





#  las listas l1 y l2
l1 = [("one", 1), ("two", 2), ("three", 3), ("four", 4), ("five", 5)]
l2 = [("one", 1), ("two", 2), ("six", 6)]

# conjuntos a partir de estas listas, s1 y s2
conjunto1 = set(l1)
conjunto2 = set(l2)

print(f"Conjunto 1: {conjunto1}")
print(f"Conjunto 2: {conjunto2}")

# elementos que son comunes a s1 y s2 
s3 = conjunto1.intersection(conjunto2) 
print(f"Elementos comunes (s3): {s3}")

# elementos que son únicos para s1 y s2 
s4 = conjunto1.symmetric_difference(conjunto2)  
print(f"Elementos únicos (s4): {s4}")

# d.
l3 = list(s3.union(s4)) 
l3.sort(key=lambda x: x[1]) 

print(f"Lista l3 ordenada por número entero: {l3}")






