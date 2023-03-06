#!/usr/bin/python3
""" Este codigo define una clase llamada BaseModel con metodos para inicializar una instancia, convertir la instancia en un diccionario 
y actualizar la instancia. La clase utilizza el modulo uuid para generar identificadores unicos, el objeto datetime para manejar 
fechas y horas, y el modulo models para almacenar y recuperar instancias """
import uuid # importa el modulo uuid para generar identificadores unicos
from datetime import datetime # importa el objeto detatime
import models # se importa para poder acceder a la instancia de FileStorage que se utiliza


format = "%Y-%m-%dT%H:%M:%S.%f" # define el formato de fecha y hora utilizado en el objeto detatime


class BaseModel:
    """ class base para otros modelos """


    def __init__(self, *args, **kwargs):
        """ Inicializa el BaseModel con argumentos """
        if kwargs: # si se proporcionan argumentos clave-valor, inicializa los atributos de la instancia
            self.id = kwargs["id"]
            self.created_at = datetime.strptime(kwargs["created_at"], format)
            self.updated_at = datetime.strptime(kwargs["updated_at"], format)
        else: # si no se proporcionan argumentos, inicializa los atributos de la instancia con valores unicos         
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            from models import storage
            storage.new(self) # llama al metodo "new" del objeto "stronge" del modulo "models"

    def __str__(self):
        """ Retorna una representacion en cadena de la instancia """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """ Actualiza el atributo "updated_ar" con la fecha y hora actuales """
        self.updated_at = datetime.now()
        models.storage.save() # llama al metodo "save" del objeto "storage" del modulo "models"

    def to_dict(self):
        """ Retorna un diccionario con los atributos de la instancia """
        result_dict = self.__dict__.copy() # crea una copia del atributo __dict__ de la instancia
        result_dict["__class__"] = self.__class__.__name__ # agrega el nombre de la clase a la copia del diccionario
        result_dict["created_at"] = self.created_at.isoformat() # convierte la fecha y hora a una cadena ISO y la agrega al diccionario
        result_dict["updated_at"] = self.updated_at.isoformat() # convierte la fecha y hora a una cadena ISO ...
        return result_dict # retorna el diccionario
