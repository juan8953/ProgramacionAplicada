## 16-EJERCICO 03 RECURSIÓN
'''
Los ejercicios son de caracter obligatorio, sin embargo no se les asignará una calificación, el objetivo de estos
es que ustedes practiquen y mejoren sus habilidades.
estos los deben subir de manera individual en su cuenta de Git
'''
'''
se les darán multiples funciones, así como la documentación correspondiente
 deben completar las tareas marcadas como TODO
'''
## DEMOSTRACIONES MATEMATICAS
# ejercicios tomados de: https://elvex.ugr.es/decsai/java/pdf/7D-Ejercicios.pdf

#TODO: Demuestre por inducción que, para todo n mayor o igual que 4, n!>2^n
def f_induccion(int_num):
    if int_num>=4:
        fact=1
        while int_num>1:
            fact*=int_num
            int_num-=1
        if fact>2**int_num:
            print("La induccion se cumple con ese numero")
            return
    else:
        print("el numero asignado no cumple la induccion")
        return
print(f_induccion(7))

#TODO: Un granjero ha comprado una pareja de conejos para criarlos y luego venderlos.
#   Si la pareja de conejos produce una nueva pareja cada mes y la nueva pareja
#   tarda un mes más en ser también productiva, ¿cuántos pares de conejos podrá
#   poner a la venta el granjero al cabo de un año?
def f_contarconejos(parejas):
    if parejas<2:#condicion para saber si los conejos empiezan desde dos
        return parejas #se imprime el unico conejo
    parejas_tot= f_contarconejos(parejas-1)+f_contarconejos(parejas-2)#la serie para la operacion de fibonacci
    return parejas_tot #muestra las parejas totales
print(f_contarconejos(10)) 
## Ejercicio objetos.
# TODO: 1. Cree un archivo, Taller donde llevará acabo el codigo principal
#       crear una lista de vehiculos que se encuentran en el taller en ese momento que tienen asociados: fecha de entrega, costo, modelo, año y dueño
#       crear una caja donde se almacena el dinero y se lleva registro de los movimientos
#       crear una lista de empleados que tienen asociado un nombre, cargo, salario, vehiculo y documento
#       Crear una lista de clientes que tienen asociado un nombre, vehiculo y documento

# TODO: 2 Ejecute sobre so codigo principal:
#       ingresar un vehiculo nuevo al taller (validar cupo)
#       Sacar un vehiculo del taller (se debe generar un pago por parte del cliente)
#       PAgar a los empleados (se debe hacer una reducción en el dinero de la caja)
#       Contrarar a una persona nueva
#       Despedir a una persona
#       Encontrar un vehiculo a partir de su dueño y determinar si está en el taller
# TODO: 3 Todas las funciones que implemente deben estar en un script distinto al principal y donde se definen sus clases
#       NOTA - (la UNICA exepción son las funciones que definen dentro de sus clases.)
class Vehiculo():

    fechaEntrega = "" # definicion de los parametros y lo que se manejara del tipo  pecha de entrega se recibira como una cadena de caracteres
    costo = 0.0 #el costo se manejara como un punto flotante
    modelo = "" # el modelo se manejara como una cadena de caracteres
    anio = 0 # el año se manejara como un entero
    duenio = None # y el dueño va a depender de lo ingresado

    def _init_(self, fechaEntrega, costo, modelo, anio, duenio):#aqui se inicia la funcion en la que se van a definir los caracteres immplementados en la funcion
        self.fechaEntrega = fechaEntrega # el parametro de fecha de entrega sera igual al valor ingresado como fecha de entrega
        self.costo = costo # el parametro de fecha de entrega sera igual al valor ingresado como fecha de entrega
        self.modelo = modelo #el parametro de modelo sera igual al valor ingresado como modelo
        self.anio = anio # el parametro de anio sera igual al valor ingresado como anio
        self.duenio = duenio # el parametro del dueño sera igual al valor ingresado como duenio
        
    def informacion(self, fechaEntrega, costo, modelo, anio, duenio):#esta es la fucnión con la que se va a imprimir la informacion (el valor de los parametros) 
     '''
     a contincion se utiliza el print para imprimir lo que se muestra en la linea siguiente en este caso cada uno de los parametros
     en los que se usa el self para identificar que se establando de los parametros de la misma clase vehiculo 
     '''
        print
        self.fechaEntrega
        print
        self.costo
        print
        self.modelo
        print
        self.anio
        print
        self.duenio
mustang = vehiculo()
mustang.fechaEntrega = '13/09/2022'
mustang.costo= '200000000'
mustang.modelo = 'match 1'
mustang.anio = '1969'
mustang.duenio = 'Samuel'
mustang.print_information(mustang.d_delivery,mustang.cost,mustang.model,mustang.year,mustang.owner) 

class Caja(): #e inicia la clase de la caja 
    dineroTotal = 0.0 # la cual contara con el parametro de el dinero total el cual se manejara como un punto flotante 
    movimientos = [] # y los movimientos los cuales se manejran como una lista 
    def _init_(self, dineroTotal): #la funcion para definicion de los marametros 
        self.dineroTotal = dineroTotal 

    def pagarEmpleados(self, empleados): # funcion para la accion de pagar a los empleados 
        totalAPagar = 0.0# los parametros utilizados el total a pagar el cual se manejara en punto flotante
        i = 0# i que sera una variable contadora inicializada en 0
        while i < len(empleados):# inicia un bucle para recorrer a los empleados 
            totalAPagar += empleados[i].salario # a cada empleado se le tiene q pagar el valor de salario por lo que este valor se le sumara al total a pagar 
            i+=1 # hecho este procedimiento se le añade i a la variable contadora para que siga recorriendo a los empleados 
        if(self.dineroTotal >= totalAPagar): # se abre el condciona ya que si el valor del paramatro de la clase ejecutada dinerototal en mayor al valor al total a pagar 
            self.dineroTotal -= totalAPagar # se descontara el valor a pagar de dinerototal
            return True
        return False

    def ingresarDinero(self, dineroIngresado):# se fefine la funcion de ingresar el dinero 
        self.dineroTotal += dineroIngresado # se agrega el dinero que esta ingresando al dinero total 
  class GestionVehiculos():# se inicia la clase de gestion de vehiculos 
    vehiculos = [] #el parametro utilizado en esta funcion sera implemetado como una lista en la cual se almacenaran los vehiculos  

    def _init_(self, vehiculos):#la funcio en la que se definene los parammetros
        self.vehiculos = vehiculos

    def ingresarVehiculo(self, vehiculo, cantidadEmpleados):# funcion para ingresar vehiculos 
        if(len(self.vehiculos)<cantidadEmpleados):# si la cantidad de vehiculos es menor a la cantidad de empleados 
            self.vehiculos.append(vehiculo)#los vehiculos 
            return True
        return False

    def sacarVehiculo(self, vehiculo):
        if(len(self.vehiculos)>0):
            if(vehiculo in self.vehiculos):
                self.vehiculos.remove(vehiculo)
                return True
        return False
 class GestionEmpleado():
    empleados = []

    def _init_(self, empleados):
        self.empleados = empleados

    def buscarEmpleado(self, documento):
        print("falta")

    def contratarEmpleado(self, empleado):
        self.empleados.append(empleado)
        return True


    def despedirEmpleado(self, empleado):
        if(len(self.empleados) > 0):
            self.empleados.remove(empleado)
            return True
        return False
       
from Vehiculo import Vehiculo


class Empleado():
    nombre = ""
    cargo = ""
    salario = 0.0
    vehiculo = None
    documento = 0

    def _init_(self, nombre, cargo, salario, vehiculo, documento):
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario
        self.vehiculo = vehiculo
        self.documento = documento
        
from Vehiculo import Vehiculo

class Cliente():
    nombre = ""
    documento = 0

    def _init_(self, nombre, documento):
        self.nombre = nombre
        self.documento = documento
