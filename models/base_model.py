#!/usr/bin/python3

from models import storage
import uuid
from datetime import datetime


format = "%Y-%m-%dT%H:%M:%S.%f"

class BaseModel:


    def __init__(self, *args, **kwargs):
        if kwargs:
            self.id = kwargs["id"]
            self.created_at = datetime.strptime(kwargs["created_at"], format)
            self.updated_at = datetime.strptime(kwargs["updated_at"], format)
        else:            
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        result_dict = self.__dict__.copy()
        result_dict["__class__"] = self.__class__.__name__
        result_dict["created_at"] = self.created_at.isoformat()
        result_dict["updated_at"] = self.updated_at.isoformat()
        return result_dict
