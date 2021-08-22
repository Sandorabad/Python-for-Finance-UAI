#Nombre: Sandor Abad
#Profesor: Francisco Ibanez
#Ayudante: Alejandro Romero

import numpy as np
import csv

# La Variable Auxiliar "indice_time" nos ayuda a extraer y formatear las fehas al formato np.datetime64
indice_time = []

# La funcion reordenar permite configurar las fechas en nuestros datos para que sean compatibles con las estructura de tiempo aceptada por numpy
def reordenar(fecha):
    # rellenamos los valores faltantes dependiendo del caso
    if len(fecha) == 9 and fecha[-8] == '-' :
        fecha = '0' + fecha #formateo deseado
        fecha = fecha[-4:] + fecha[-5] + fecha[-10:-8] + fecha[-8] + fecha[-7:-5] #orden deseado
        fecha = np.datetime64(fecha) #transformamos a np.datetime64
        indice_time.append(fecha)
        

    elif len(fecha) == 8 and fecha[-7] == '-' :
        fecha = '0' + fecha[0:2] + '0' + fecha[2:] #formateo deseado
        fecha = fecha[-4:] + fecha[-5] + fecha[-10:-8] + fecha[-8] + fecha[-7:-5] #orden deseado
        fecha = np.datetime64(fecha) #transformamos a np.datetime64
        indice_time.append(fecha)

    elif len(fecha) == 9 and fecha[-8] != '-' :
        fecha = fecha[0:3] + '0' + fecha[3:] #formateo deseado
        fecha = fecha[-4:] + fecha[-5] + fecha[-10:-8] + fecha[-8] + fecha[-7:-5] #orden deseado
        fecha = np.datetime64(fecha) #transformamos a np.datetime64
        indice_time.append(fecha)
    
    else:
        fecha = fecha[-4:] + fecha[-5] + fecha[-10:-8] + fecha[-8] + fecha[-7:-5] #orden deseado
        fecha = np.datetime64(fecha) #transformamos a np.datetime64
        indice_time.append(fecha)


# La funcion importar_serie permite leer archivos .csv que tengan la estructura por columnas: indice(en modo de fecha str), datos(etiquetas/titulos de datos)
# Es decir la columna que señala el indice(debe estar en la primera poscicion) contiene fechas en formato string
# La columna con etiquetas tiene datos numericos en formato str
# la funcion devuelve las fechas en formato np.datetime64 y los valores numericos en formato float 

def importar_serie(archivo):
    with open(archivo, 'r') as f: #Importamos el archivo
        datos = list(csv.reader(f)) #Lo cargamos
        datos = np.array(datos) #Le asignamos una variable

        data_str = datos[1:, 1:] #Extraemos los datos numericos
        dimensiones = data_str.shape #Extraemos las dimensiones
        data_float = data_str.astype(np.float) #Cambiamos el tipo de los datos
        data = data_float

        indice_str = datos[1:, 0:1] # Exraemos las fechas en modo str
        indice_str = np.array([indice_str[x][0].replace('/', '-') for x in range(dimensiones[0])]) #formateamos a un formato mas amigable

        for i in range(dimensiones[0]): #Aplicamos la funcion reordenar para transformar los valores fecha str en valores np.datetime64
            reordenar(indice_str[i])

        indice = np.array(indice_time, dtype = 'datetime64').reshape(dimensiones[0], 1) #Transformamos los valores en un array
        indice_time = [] #Restauramos nuestra variable auxiliar

        etiquetas = datos[0, 1:] #Extraemos las etiquetas


    print(f"\n data: \n{data}  shape: {data.shape} type: {data.dtype}") #mostramos los datos en la terminal
    print(f"\n indice: \n{indice}  shape: {indice.shape} type: {indice.dtype}") #mostramos los datos en la terminal
    print(f"\n etiquetas: \n{etiquetas}  shape: {etiquetas.shape} type: {etiquetas.dtype}") #mostramos los datos en la terminal


def regresa(dependiente, independiente, etiquetas, mudo = False):
    X_i_menos_promX = [independiente[i] - np.mean(independiente) for i in range(len(independiente))]
    Y_i_menos_promY = [dependiente[i] - np.mean(dependiente) for i in range(len(dependiente))]
    b_1_numerador = sum([X_i_menos_promX[i] * Y_i_menos_promY[i] for i in range(len(X_i_menos_promX))])
    b_1_denominador = sum([X_i_menos_promX[i] ** 2 for i in range(len(dependiente))])
    b_1 = b_1_numerador/b_1_denominador

    b_0 = np.mean(dependiente) - b_1 * np.mean(independiente)
    coeff = [b_1, b_0]

    Y_est = [b_0 + b_1 * independiente[i] for i in range(len(dependiente))]
    Y_est_menos_promY = [Y_est[i] - np.mean(dependiente) for i in range(len(dependiente))]

    ssr = sum([Y_est_menos_promY[i] ** 2 for i in range(len(dependiente))])
    sst = sum([Y_i_menos_promY[i] ** 2 for i in range(len(dependiente))])
    r2 = ssr / sst 

    final_array = np.array(etiquetas, [])
    print()

    return r2, coeff

    