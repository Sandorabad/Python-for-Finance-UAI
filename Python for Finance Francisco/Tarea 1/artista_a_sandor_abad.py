#Alumno: Sandor Abad
#Profesor: Francisco Ibañez
#Ayudante: Alejandro Romero

#------------------------------------------------------------------------------------------------------------

# EJERCICIO II (A)

prompt = "Ingresa la cantidad de filas: " # Elegimos la cantidad de Filas
n = int(input(prompt))

dibujo = []

if n == 0:
    print("Elige un numero más grande porfavor") #Es necesario que le numero de filas sea mayor que 0

for i in range(n):
    if n == 0:
        continue
    else:
        dibujo.append(i+1)
        print(*dibujo) # el operador * permite permutar el interior de la lista sin tener que escribir un for loop  



#------------------------------------------------------------------------------------------------------------

