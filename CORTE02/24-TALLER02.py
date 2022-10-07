class persona (object):
    def __init__(self):
        self.nombre() # Nombre de la persona
        self.Hermanos() # hermanos de la persona (n datos)
        self.Padres() # padres de la persona (2 datos o menos)

    def add_siblings (self,sib):
        # TODO: verificar y asegurar que los hermanos tengan los mismos padres (0.5)
        self.Hermanos.append(sib)

    def add_parents (self,parent):
        if self.Padres < 2:
            self.Padres.append(parent)
        else:
            print('No se puede agregar')

    def search (self,nombre):
        '''
        se busca a cualquier persona en el arbol, se asume que el usuario puede colocar cualquier combinación de
        mayusculas y minusculas
        :param nombre: nombre de la persona a buscar
        :return: retorna el objeto encontrado así como la altura a la que se encuentra el elemento
        '''
        #TODO: Implementar un método de busqueda para encontrar a cualquier persona en el arbol (0.5)

    def tree2dict (self):
        '''
        convierte el arbol actual en un diccionario usando los nombres como llaves y los padres y hermanos como llaves
        :return: retorna un diccionario
        '''
        # TODO: Implementar una función que permita convertir el arbol actual en un diccionario (1.0)

    def encript(self,nombre):
        '''
        crea un archivo encriptado, con la información correspondiente al arbol
        :param nombre: nombre del archivo que se desea crear
        :return: null
        '''
        # TODO: Implementar una función que permita converti el arbol en un archivo encriptado (1.0)

    def decrip(self,nombre):
        '''
        lee un archivo de texto, lo decifra y convierte el resultado en el arbol correspondiente
        :param nombre: Nombre del archivo que se desea leer
        :return: arbol creado
        '''
        #TODO: Im plementar una función que permita convertir un archivo encriptado en un arbol (1.0)

##
'''
la siguiente sección se debe realizar en un archivo distinto llamado TALLER02-2_nombre_apellido.py
'''
#TODO: iniciar y crear el arbol con una profundidad de almenos 4 con su familia (0.2)
#TODO: validar la función de busqueda (0.2)
#TODO: validad la encriptación de los archivos (0.2)
#TODO: validar la decriptación de archivos (0.2)
#TODO: validar la converción a diccionario (0.2)

#Trabajamos con Alejandra Leyton, Samuel Tamara, Juan Lozano, Kenneth Gomez 

def busqueda_secuencial(n, lista):
    for i in range(0, len(lista)):
        if lista[i] == (n):
            return i
class persona():
    def __init__(self):
        self.Hermanos = []  # hermanos de la persona (n datos)
        self.Padres = []  # padres de la persona (2 datos o menos)
        self.edad = []
    def add_parents(self, padres):
        if len(self.Padres) < 2:
            self.Padres.append(padres)
        else:
            print('No se puede agregar')
    def add_siblings(self, hermano):
        self.Hermanos.append(hermano)
        hermano.add_parents(self.Padres[0])
        hermano.add_parents(self.Padres[1])
    def search(self, nombre):
        if self == nombre:
            return self
        else:
            A = busqueda_secuencial(nombre, self.Hermanos)
            if A != None:
                return A
            else:
                return self.Padres[0].search(nombre)
    def tree2lista(self):
        lista1 = []
        t = self
        t.Hermanos = []
        t.Padres = []
        lista1.append(t)
        lista1.append(self.Hermanos)
        lista1p0 = self.t.tree2lista(self.Padres[0])
        lista1p1 = self.t.tree2lista(self.Padres[1])
        lista1.append(lista1p0)
        lista1.append(lista1p1)
        return lista1

    def tree2dict(self):

        '''
        convierte el arbol actual en un diccionario usando los nombres como llaves y los padres y hermanos como llaves
        :return: retorna un diccionario
        '''
        # TODO: Implementar una función que permita convertir el arbol actual en un dicci(1.0)onario

    def encript(self,nombre):
        self.nombrearch=nombre
        zn=self.nombrearch+'.txt'
        print(zn)
        with open(zn,'a') as file:
            file.write('\n'+self.nombre)
            file.write('\n'+self.PPadres)
            file.write('\n'+self.HHermanos)
            #SE HIZO LA COMPROBACION EN 2 PLATAFORMAS Y ESTA SECCION SI FUNCIONA
        # TODO: Implementar una función que permita converti el arbol en un archivo encriptado (1.0)
    def decrip(self,nombre):
        self.nombrearch=nombre
        zn=self.nombrearch+'.txt'
        archivo=open(zn,'rt',encoding='utf-8')
        print(archivo.read())
        return('Arbol creado')
