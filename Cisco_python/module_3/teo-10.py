#El ciclo while ejecuta una sentencia o un conjunto de declaraciones siempre que una condición 
# booleana especificada sea verdadera


# Ejemplo 2
contador = 5
while contador > 2:
    print(contador)
    contador -= 1



#El ciclo for ejecuta un conjunto de sentencias muchas veces; se usa para iterar sobre una secuencia 
#(por ejemplo, una lista, un diccionario, una tupla o un conjunto; pronto aprenderás sobre ellos) u otros 
#objetos que son iterables (por ejemplo, cadenas). Puedes usar el ciclo for para iterar sobre una secuencia de 
#números usando 
#la función incorporada range

# Ejemplo 2
for i in range(1, 10):
    if i % 2 == 0:
        print(i)


#2. Puedes usar las sentencias break y continue para cambiar el flujo de un ciclo:
texto = "OpenEDG Python Institute"
for letter in texto:
    if letter == "P":
        break
    print(letter, end= "")

print("-----------------1----------------------")
text = "pyxpyxpyx"
for letter in text:
    if letter == "x":
        continue
    print(letter, end= "")


#3. Los ciclos while y for también pueden tener una cláusula else en Python. La cláusula else se 
#ejecuta después de que el ciclo finalice su ejecución siempre y cuando no haya terminado con break, 
#por ejemplo:
print("------------2-------------")
n = 0
while n != 3:
    print(n)
    n += 1
else:
    print(n, "else")

print()
print("------------3-----------")

for i in range(0, 3):
    print(i)
else:
    print(i,"else")




print("------------4-------------")

palabra = "Python"
for letter in palabra:
    print(letter, end = "*")


print("---------------5------------")


#4. La función range() genera una secuencia de números. Acepta enteros y devuelve objetos de rango. 
# a sintaxis de range() tiene el siguiente aspecto: range(start, stop, step), donde:

#start es un parámetro opcional que especifica el número de inicio de la secuencia (0 por defecto).
#stop es un parámetro opcional que especifica el final de la secuencia generada (no está incluido).
#y step es un parámetro opcional que especifica la diferencia entre los números en la secuencia es (1 por defecto).


for i in range(3):
    print(i, end=" ") # salidas: 0 1 2
print("------------6------------")
for i in range(6, 1, -2): #PASOS REGRESIVOS IMPORTANTE (CONTEO REGRESIVO)
    print(i, end=" ") # salidas: 6, 4, 2
print("----------7--------------")

for i in range(6, 1): #NO SIRVE PORQUE LE FALTA EL PASO 3
    print(i, end=" ")


