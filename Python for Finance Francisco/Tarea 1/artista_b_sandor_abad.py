#Alumno: Sandor Abad
#Profesor: Francisco Ibañez
#Ayudante: Alejandro Romero

#------------------------------------------------------------------------------------------------------------

# EJERCICIO II (B)

prompt = "Ingresa la cantidad de filas: " # Elegimos la cantidad de Filas
n = int(input(prompt))

star = "*"
space = " "

if n == 0:
    print("Elige un numero más grande porfavor") #Es necesario que le numero de filas sea mayor que 0

for i in range(n+1):
    if i == 0:
        continue
    else:
        print(f"{(n-i)*space}{star*(2*i-1)}{(n-i)*space}") #una ecuacion que nos permite ver como se desplaza el espacio

#------------------------------------------------------------------------------------------------------------