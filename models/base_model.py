#!/usr/bin/python3
""" BaseModel """
import uuid
from datetime import datetime
import models


format = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """ class BaseModel """


    def __init__(self, *args, **kwargs):
        """ Initializes the BaseModel """
        if kwargs:
            self.id = kwargs["id"]
            self.created_at = datetime.strptime(kwargs["created_at"], format)
            self.updated_at = datetime.strptime(kwargs["updated_at"], format)
        else:           
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            from models import storage
            storage.new(self)

    def __str__(self):
        """ print str BaseModel """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """ updates the instance attribute updated_at with the current datetime """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ returns a dictionary containing all keys/values of __dict__ of the instance """
        result_dict = self.__dict__.copy()
        result_dict["__class__"] = self.__class__.__name__
        result_dict["created_at"] = self.created_at.isoformat()
        result_dict["updated_at"] = self.updated_at.isoformat()
        return result_dict
