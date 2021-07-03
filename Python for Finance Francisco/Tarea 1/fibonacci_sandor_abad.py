#Alumno: Sandor Abad
#Profesor: Francisco Ibañez
#Ayudante: Alejandro Romero

#------------------------------------------------------------------------------------------------------------

# EJERCICIO I

prompt = "Ingresa el numero para calcular la serie fibonacci hasta ese numero: "
n = int(input(prompt)) #Ingresamos el valor y lo transformamos en un int para poder trabajar con el

Fibo_list = [0, 1] #Valores minimos iniciales para crear la secuencia

while Fibo_list[-1] < n: #Creamos la secuencia hasta alcanzar/superar el valor n
    post = Fibo_list[-1] + Fibo_list[-2]
    Fibo_list.append(post)

print(Fibo_list[:-1]) #Proyectamos en la consola los valores menores a n


#------------------------------------------------------------------------------------------------------------