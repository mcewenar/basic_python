#Algunas funciones simples: Serie Fibonacci
#¿Estás familiarizado con la serie Fibonacci?

#Son una secuencia de números enteros los cuales siguen una regla sencilla:

#El primer elemento de la secuencia es igual a uno (Fib1 = 1).
#El segundo elemento también es igual a uno (Fib2 = 1).
#Cada numero después de ellos son la suman de los dos números anteriores (Fibi = Fibi-1 + Fibi-2).
#Aquí están algunos de los primeros números en la serie Fibonacci:

#fib1 = 1
#fib2 = 1
#fib3 = 1 + 1 = 2
#fib4 = 1 + 2 = 3
#fib5 = 2 + 3 = 5
#fib6 = 3 + 5 = 8
#fib7 = 5 + 8 = 13

#¿Que opinas acerca de implementarlo como una función?

#Creemos nuestra propia función fib y probémosla, aquí esta:

def fib(n):
    if n < 1:
         return None
    if n < 3:
        return 1

    elem1 = elem2 = 1
    sum = 0
    for i in range(3, n + 1):
        sum = elem1 + elem2
        elem1, elem2 = elem2, sum
    return sum

for n in range(1, 10): # probando
    print(n, "->", fib(n))


#Analiza el codigo del bucle for cuidadosamente, descifra como se mueven las variables elem1 y elem2 a través de 
#los números subsecuentes de la serie Fibonacci.

#Al probar el código, se generan los siguientes resultados:

#1 -> 1
#2 -> 1
#3 -> 2
#4 -> 3
#5 -> 5
#6 -> 8
#7 -> 13
#8 -> 21
#9 -> 34