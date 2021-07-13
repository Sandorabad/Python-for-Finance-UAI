
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


### TESTS
#---------------------------------------------------------------------------------------------------------------------------------------------
importar_serie(archivo = 'C:\\Users\sando\Desktop\Programming\Python for Finance Francisco\Proyecto 1\goog.csv')
 
importar_serie(archivo = 'C:\\Users\\sando\\Desktop\\Programming\\Python for Finance Francisco\\Proyecto 1\\fama_french_ordenado.csv')





























with open('goog.csv', 'r') as f:
    datos = list(csv.reader(f))
    datos = np.array(data)


data_str = datos[1:, 1:]
dimensiones = data_str.shape
data_float = np.array([float(i) for i in data_str]).reshape(dimensiones)

indice_str = datos[1:, 0:1]
dimensiones = data_str.shape
indice_str = np.array([indice_str[x][0].replace('/', '-') for x in range(dimensiones[0])]).reshape(dimensiones)


for i in range(dimensiones[0]):
    reordenar(indice_str[i][0])

indice_time = np.array(indice_time).reshape(dimensiones)



def reordenar(fecha):
    # rellenamos los valores faltantes dependiendo del caso
    if len(fecha) == 9 and fecha[-8] == '-' :
        fecha = '0' + fecha
        fecha = fecha[-4:] + fecha[-5] + fecha[-10:-8] + fecha[-8] + fecha[-7:-5]
        fecha = np.datetime64(fecha)
        indice_time.append(fecha)
        

    elif len(fecha) == 8 and fecha[-7] == '-' :
        fecha = '0' + fecha[0:2] + '0' + fecha[2:]
        fecha = fecha[-4:] + fecha[-5] + fecha[-10:-8] + fecha[-8] + fecha[-7:-5]
        fecha = np.datetime64(fecha)
        indice_time.append(fecha)

    elif len(fecha) == 9 and fecha[-8] != '-' :
        fecha = fecha[0:3] + '0' + fecha[3:]
        fecha = fecha[-4:] + fecha[-5] + fecha[-10:-8] + fecha[-8] + fecha[-7:-5]
        fecha = np.datetime64(fecha)
        indice_time.append(fecha)
    
    else:
        fecha = fecha[-4:] + fecha[-5] + fecha[-10:-8] + fecha[-8] + fecha[-7:-5]
        fecha = np.datetime64(fecha)
        indice_time.append(fecha)

reordenar(a)


a = '8-23-2019' 
b = '8-9-2019'
c = '12-9-2019'
d = '12-24-2019'
a[-8]
obj = '2019-08-23'

reordenar(a)
reordenar(b)
reordenar(c)
reordenar(d)





indice_str = np.array(["0" + indice_str[x][0] if indice_str[x][0][0:2] not in numeros else indice_str[x][0] for x in range(dimensiones[0])]).reshape(dimensiones)
indice_str = [indice_str[x][0][:1] + '0' + indice_str[x][0][1:] if indice_str[x][0][-7:-5] not in numeros else  indice_str[x][0] for x in range(dimensiones[0])]

indice_time = np.array([indice_str[i][0][6:] + indice_str[i][0][5] + indice_str[i][0][0:3] + indice_str[i][0][3:5] for i in range(dimensiones[0])]).reshape(dimensiones)


indice_time = np.array([np.datetime64(indice_time[i][0]) for i in range(dimensiones[0])]).reshape(dimensiones)


indice_str[0][0]

a = ['08-15-2004', '08-20-2004', '08-20-2004', '08-20-2004', '08-20-2004']
a[0][-7:-]
as3 = a[0][0:3]
as4 = a[0][3:5]

print(as1 + as2 + as3 + as4)

def año_mes_dia(mes_dia_año):

b = np.datetime64(a)

estesipo = [a[i][6:] + a[i][5] + a[i][0:3] + a[i][3:5] for i in range(len(a))]

indice_str = np.array(["0" + indice_str[x][0] if len(indice_str[x][0]) == 9 indice_str[x][0] = indice_str[x][0][:1] + '0' + indice_str[x][0][1:] if len(indice_str[x][0]) == 8 else indice_str[x][0] for x in range(dimensiones[0])]).reshape(dimensiones)







def importar_serie_google(archivo):
    with open(archivo, 'r') as f:
        datos = list(csv.reader(f))
        datos = np.array(datos)

        data_str = datos[1:, 1:]
        dimensiones = data_str.shape
        data_float = np.array([float(i) for i in data_str]).reshape(dimensiones)
        data = data_float

        indice_str = datos[1:, 0:1]
        indice_str = np.array([indice_str[x][0].replace('/', '-') for x in range(dimensiones[0])]).reshape(dimensiones)
        
        for i in range(dimensiones[0]):
            reordenar(indice_str[i][0])

        indice = np.array(indice_time, dtype = 'datetime64' )

        etiquetas = datos[0, 1:]

        print(f"\n data: \n{data}  shape: {data.shape} type: {data.dtype}")
        print(f"\n indice: \n{indice}  shape: {indice.shape} type: {indice.dtype}")
        print(f"\n etiquetas: \n{etiquetas}  shape: {etiquetas.shape} type: {etiquetas.dtype}")



