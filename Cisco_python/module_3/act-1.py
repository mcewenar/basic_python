#Usando uno de los operadores de comparación en Python, escribe un programa simple de dos líneas que tome el parámetro n como entrada, 
#que es un entero, e imprime False si n es menor que 100, y True si n es mayor o igual que 100.


n= int(input("Enter the number: "))
n = (False == n < 100) or (n>=100)
print(n)