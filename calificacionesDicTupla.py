#Las tuplas y los diccionarios pueden trabajar juntos:
#Se ha preparado un ejemplo sencillo, mostrando como las tuplas y los diccionarios pueden trabajar juntos.

#Imaginemos el siguiente problema:

#Necesitas un programa para calcular los promedios de tus alumnos.
#El programa pide el nombre del alumno seguido de su calificación.
#Los nombres son ingresados en cualquier orden.
#El ingresar la palabra exit da por terminado el ingreso de nombres.
#Una lista con todos los nombre y el promedio de cada alumno debe ser mostrada al final.

#Observa el código en el editor, se muestra la solución.
grupo = {}

while True:
    nombre = input("Ingresa el nombre del estudiante (o exit para detenerse): ")
    if nombre == 'exit':
        break
    
    calif = int(input("Ingresa la calificación del alumno (0-10): "))
    
    if nombre in grupo:
        grupo[nombre] += (calif,) #agrega más calificadores como una tupla y la clave es el nombre del alumno
    else:
        grupo[nombre] = (calif,)
        
for nombre in sorted(grupo.keys()): #Itera todos los estudiantes
    sum = 0
    contador = 0
    for calif in grupo[nombre]: #aquí recorre el valor de cada elemento de la tupla ( Se itera a través de la tupla, 
        #tomado todas las calificaciones subsecuentes y actualizando la suma junto con el contador.)
        sum += calif
        contador += 1
    print(nombre, ":", sum/contador)



#Ahora se analizará línea por línea:

#Línea 1: crea un diccionario vacío para ingresar los datos: el nombre del alumno es empleado como clave, mientras que todas las 
#calificaciones asociadas son almacenadas en una tupla (la tupla puede ser el valor de un diccionario, esto no es un problema).
#Línea 3: se ingresa a un bucle "infinito" (no te preocupes, saldrémos de el en el momento indicado).
#Línea 4: se lee el nombre del alumno.
#Línea 5-6: si el nombre es exit, nos salimos del bucle.
#Línea 8: se pide la calificación del alumno (un valor entero en el rango del 1-10).
#Línea 10-11: si el nombre del estudiante ya se encuentra en el diccionario, se alarga la tupla asociada con la nueva calificación 
#(observa el operador +=).
#Línea 12-13: si el estudiante es nuevo (desconocido para el diccionario), se crea una entrada nueva, su valor es una tupla de un solo 
#elemento la cual contiene la calificación ingresada.
#Línea 15: se itera a través de los nombres ordenados de los estudiantes.
#Línea 16-17: inicializa los datos necesarios para calcular el promedio (sumador y contador).
#Línea 18-20: Se itera a través de la tupla, tomado todas las calificaciones subsecuentes y actualizando la suma junto con el contador.
#Línea 21: se calcula e imprime el promedio del alumno junto con su nombre.
#Este es un ejemplo del programa:

#Ingresa el nombre del estudiante (o exit para detenerse): Bob
#Ingresa la calificación del alumno (0-10): 7
#Ingresa el nombre del estudiante (o exit para detenerse): Andy
#Ingresa la calificación del alumno (0-10): 3
#Ingresa el nombre del estudiante (o exit para detenerse): Bob
#Ingresa la calificación del alumno (0-10): 2
#Ingresa el nombre del estudiante (o exit para detenerse): Andy
#Ingresa la calificación del alumno (0-10): 10
#Ingresa el nombre del estudiante (o exit para detenerse): Andy
#Ingresa la calificación del alumno (0-10): 3
#Ingresa el nombre del estudiante (o exit para detenerse): Bob
#Ingresa la calificación del alumno (0-10): 9
#Ingresa el nombre del estudiante (o exit para detenerse): exit
#Andy : 5.333333333333333
#Bob : 6.0