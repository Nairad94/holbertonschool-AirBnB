#!/usr/bin/python3
""" FileStorage """
import json # Importa la libreria json para manejar archivos JSON
import os # Importa el modulo os para manejar archivos y directorios en el sistema operativo
from models.user import User # Importa la clase User del modulo models


class FileStorage:
    """ Define la class FileStorage """

    __file_path = "file.json" # Define el atributo __file_path y le asigna el valor "file.json"
    __objects = {} # Define el atributo __objects como un diccionario vacio


    def all(self): # Define el método "all" que retorna el diccionario __objects
        """ Returns the dictionary __objects """
        return FileStorage.__objects

    def new(self, obj):
        """ Define el método "new" que agrega un objeto al diccionario __objects usando el nombre de la clase y su atributo id como clave """
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """ Define el método "save" que serializa el diccionario __objects en un archivo JSON con el path definido en __file_path """
        obj_dict = {} # se crea un diccionario vacio 
        for key, value in self.__objects.items(): # itera a través de los elementos del diccionario self.__objects y asigna cada clave al nombre de variable key y cada valor al nombre de variable value
            obj_dict[key] = value.to_dict() # crea un nuevo par clave-valor en el diccionario obj_dict donde la clave es la misma clave del diccionario __objects y el valor es el resultado de llamar al método to_dict() del objeto correspondiente.
        with open(self.__file_path, "w", encoding="utf-8") as file: # El parámetro "w" indica que el archivo debe abrirse en modo de escritura, y "utf-8" indica que se debe usar la codificación UTF-8 para el archivo.
            json.dump(obj_dict, file) # La función json.dump() es utilizada para serializar el diccionario obj_dict a una cadena JSON y escribirlo en el archivo abierto.

    def reload(self):
        """ Define el método "reload" que deserializa el archivo JSON en __objects """
        # Importa todas las clases necesarias del módulo models
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        # Crea un diccionario de clases que corresponde a los valores de "__class__" en el archivo JSON
        dic_classes = {
            "BaseModel": BaseModel,
            "User": User,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
        }           
        if os.path.isfile(self.__file_path): # La función os.path.isfile() se utiliza para verificar si el archivo especificado en self.__file_path existe
            with open(self.__file_path, "r", encoding="utf-8") as file: # Abre el archivo JSON y carga su contenido en un diccionario
                obj_dict = json.load(file)
                for key, value in obj_dict.items(): # itera sobre cada par de clave-valor en el diccionario obj_dict utilizando el método items().
                    # En cada iteración, se asigna la clave a la variable key y el valor a la variable value
                    FileStorage.__objects[key] = dic_classes[value["__class__"]](**value)
                    """crea una nueva instancia de una clase y la almacena en el diccionario FileStorage.__objects, utilizando la clave key que se recupera del archivo JSON 
                    y la clase correspondiente que se determina a partir de la clave __class__ en el diccionario value.
                    Para hacer esto, se utiliza el diccionario dic_classes que se crea anteriormente en el método reload, el cual tiene los nombres de las clases como claves
                    y las clases en sí como valores. La sintaxis dic_classes[value["__class__"]] busca la clase correspondiente en el diccionario a partir de la cadena de texto value["__class__"].
                    Finalmente, se crea una instancia de la clase encontrada usando los argumentos proporcionados por el diccionario value utilizando la sintaxis dic_classes[value["__class__"]](**value)
                    y se almacena en el diccionario FileStorage.__objects con la clave key."""