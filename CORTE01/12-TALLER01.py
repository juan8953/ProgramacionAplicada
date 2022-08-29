## 12-TALLER 01
'''
El presente taller tiene como objetivo evaluar las habilidades adquiridas hasta el momento a lo largo del curso,
así como repasar los conceptos e introducir nuevas herramientas.
'''
# Recordatorio, el archivo lo deben subir a su repositorio en la fecha indicada.
#Trabajado con Maria Alejandra Leyton, Alber Jose Muñoz y Juan David Panadero
## 1. Persistencia (1.0)
#TODO: escriba un programa que le permina escribir de manera automatica los nombres de estos paises en un archivo txt
#NOTA: todos los nombres deben tener una mayuscula al comienzo
#el archivo se ecuentra en formato csv
l_paises = ['Colombia','Mexico','Turquia','Polonia','serbia','dinamarca','holanda','Alemania'] #colocamos la lista que nos indico el docente
l_paises1=""  #Inicio una variable donde se van a almacenar los datos
for i in range(0,8,1): #inicio un bucle para poder poner la letra mayuscula en la primera letra de cada pais
    l_paises1+=l_paises[i].capitalize() #Funcion capitalize para colocar la primera letra mayuscula y se agrega la palabra ya lista segun los parametros
    l_paises1+=", " #se le agrega una , y un espacio para que quede en formato csv
archi1=open("datos.txt","w") #generamos el archivo txt para almacenar los paises
with open('datos.txt', 'w') as temp_file: # se abre el archivo para poder agregar
    for item in l_paises1:#bucle para que se escriban todas las palabras en el formato
        temp_file.write("%s" % item)#se agregan los datos
file = open('datos.txt', 'r')#se abren los datos para verificar que se genere el archivo
## 2. Lectura de archivos (1.0)
str_archivo = open("datos.txt") #se busca el archivo con la funcion open
print(str_archivo.read()) #se una la funcion read para que se imprima
#TODO: escriba un programa que le permita leer e imprimir el archivo generado anteriormente

## 3. números binario (1.5)
def f_calBin (s_num):#funcion f_calBin para iniciar todo el ciclo
    s_residuo=0#se inicia una variable para poder hacer la convercion  segun el residuo
    list=[]#se inicia una lista para almacenar los datos segun su parte entera o decimal
    str_num=str(s_num)#se convierte el numero en un tipo string
    print(str_num.split(sep="."))#se hace la evaluacion para separar el numero a ver si tiene decimales o no y se imprime
    s1_num=int(str_num[0]) #se convierte cada parte en un entero para poder evaluar todos los paso
    s2_num=int(s1_num)

    while s1_num!=0:#se inicia un  bucle para iniciar con la conversion
        s_residuo =s1_num % 2#se evalua el residuo de la division
        s1_num=s1_num//2 #se usa la division entera para evaluar bien el cambio
        list.append(s_residuo) #se le agrega a la lista el residuo, esto quiere decir q se empieza a escribir el binario
    t= len(list) - 1#se cuenta la cantidad de terminos de la lista con la funcion len y se almacena en la varaiable k
    s_bin=[]#se inicia una lista para agregar la otra parte de la funcion
    while (t>= 0): #se inicia un bucle para porder identificar la parte entera
        s_bin.append(list[t])#se agrega la posicion en la lista t
        t = t - 1#se le reta 1 a la cantidad de terminos
    s2_num=s2_num*10^(len(str_num[1]))#se hace la operacion para el segundo termino para organizar el binario
    for i in range(5):#se inicia un bucle en un rango para el proceso
        s2_num=s2_num*2#se multiplica por 2 el segundo numero
        t=str(s2_num)#se convierte a string
        s_bin.append(int(t[0]))#se agrega como entero a la posicion 0 de la lista
        s2_num=int(t[0])#se cambia la posicion
    return s_bin#retorna el numero en binario
print(f_calBin(0))#se imprime la funcion con el parametro del numero a convertir

#Test

assert f_calBin (1) == 1
assert f_calBin (4) == 100
assert f_calBin (10) == 1010
assert f_calBin (1.25) == 1.01

## 4. Valores estadisticos (1.5)
import numpy as np  #se importa la libreria numpy
l_valores = [9,2, 9, 4, 5, 1, 8, 7, 8, 8, 9, 10,3] #la lista para obtener los datos solicitados
def f_stat(l_valores):#se inicia una funcion con el paso de la lista
    s_mean, s_median,str_ordn,int_contadora,int_divisor,str_ordn = 0, 0, 0, 0,len(l_valores),np.sort(l_valores)#se declaran las variables necesarias para poder hacer todo el proceso
    s_mean=sum(l_valores)/int_divisor#se saca el promedio segun su formula, donde se suman todos los terminos y se divide en la cantidad de estos
    half=int_divisor//2#se hace una variable como indice
    if not int_divisor%2:#se inicia un bucle para evaluar si el numero es par o impar
        s_median=(l_valores[half-1]+l_valores[half])/2#segun el indice se le resta a la lista ya que es impar para poder sacar la media
    else:
        s_median=l_valores[half]#se le saca la mitad a la lista
    def mode(l_valores):#se inicia otra funcion para la moda
      frequency = {}#se hace un diccionario para ver la frecuencia de los datos
      for value in l_valores:#se evalua en la lista los valores que hay
          frequency[value] = frequency.get(value, 0) + 1#se hace un inicio para el conteo
      most_frequent = max(frequency.values())#se hace el conteo de cuantas veces se repite los datos
      s_moda = [key for key, value in frequency.items()#
                        if value == most_frequent]#se le pide el valor con mas frecuencia
      return s_moda#se retorna la moda
    return (f"la media es:{s_mean}, y la mediana es: {s_median}, y la moda es: {mode(l_valores)}")#se retornas los valores solicitados
print(f_stat(l_valores))#se imprime toda la funcion

## 5. BONO (0.5)
#TODO: realizar la verificación del punto aterior haciendo uso de la función assert (pytest)

