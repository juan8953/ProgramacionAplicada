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
#Trabajamos con Samuel Tamara, Alber Muñoz, Alejandra Leyton, Juan Lozano
class persona():
    pass  # class establece a las personas como un objeto
    def init(self, Hermanos, Padres):  # definimos el objeto ya creado y establecemos sus parametros
        self.nombre=[]  # Nombre de la persona
        self.Hermanos = []  # hermanos de la persona (n datos)
        self.Padres = []  # padres de la persona (2 datos o menos)

    def add_siblings(self, Hermanos):  # TODO: verificar y asegurar que los hermanos tengan los mismos padres (0.5)
        self.Hermanos.append(Hermanos)

    def add_parents(self, Padres):
        if len(self.Padres) < 2:
            self.Padres.append(Padres)
        else:
            print('No se puede agregar')

    def search(self, nombre):
        i = 0
        while i < len(self.Hermanos):
            if nombre == self.Hermanos[i]:
                print(f"{nombre} es hermano")
                break
            else:
                i += 1
        j = 0
        while j < len(self.Padres):
            if nombre == self.Padres[i]:
                print(f"{nombre} es un padre")
                break
            else:
                j += 1

    def tree2dict(self):
        '''
        convierte el arbol actual en un diccionario usando los nombres como llaves y los padres y hermanos como llaves
        :return: retorna un diccionario
        '''
        # TODO: Implementar una función que permita convertir el arbol actual en un diccionario (1.0)

        arbol = persona()

        def diccionario(self, nombre):
            self.nombre = nombre

        def str(self):
            txt = "persona {0}"
            return txt.format(self.nombre)

    def encript(self, nombre):  # definimos la base de la encriptacion
        abcdario = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                    "u", "v", "w", "x", "y",
                    "z"]  # integramos una lista de letras que contaran estos mismos para la enriptacion
        str_msg = ""
        s_key = 3  # Establecemos la llave dentro de la encrpitacion que en este caso es "3"
        for letra in nombre:  # creamos un bucle para las letras y nombres dentro de la definicion
            if letra in abcdario:
                indice_actual = abcdario.index(letra)
                indice = indice_actual + s_key
            if indice > 26:
                indice -= 26
                str_msg += abcdario[indice]  # la variable guardada se suma con las letras dentro del abecedario
        else:
            str_msg += letra
            return str_msg, s_key  # retornamos el bucle para la llave y la variable guardada
            # TODO: Implementar una función que permita converti el arbol en un archivo encriptado (1.0)

    def decrip(self, nombre):
        abcdario = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                    "u", "v", "w", "x", "y",
                    "z"]  # integramos una lista como terminos que se contaran para la descriptacion
        nombre = ''
        for letra in abcdario:
            if letra.isdigit():
                nombre += abcdario[int(letra)]
        else:
            nombre += letra
        return (nombre)

gustav = persona("Hermanos","padres")  # en este punto integraremos los objetos que iran en el arbol como los hujos y los padres
gustav.add_siblings("Manuel")  # Hijo dentro del arbol
gustav.add_siblings("Sofia")  # Hija dentro del arbol
gustav.add_siblings("Luciana")  # Hija dentro del arbol
gustav.add_siblings("Valentino")  # Hijo dentro del arbol
gustav.add_parents("Lamar")  # padre dentro del arbol
gustav.add_parents("Demi")  # madre dentro del arbol
juan = persona("Hermanos", "Padres")
gustav.search("Luciana")
print(gustav.Hermanos, gustav.Padres)
print(encript(Sofia))  # Imprimiremos la encriptacion del arbol teniendo en cuenta la lista puesta antes
print(decript(nombre))  # Imprimiremos la desencriptacion del arbol teniendo en cuenta la lista puesta antes
