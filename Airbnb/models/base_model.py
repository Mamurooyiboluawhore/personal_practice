#!/usr/bin/python3
from datetime import datetime
import uuid

# a base class that defines all common attributes
class BaseModel():
# initializing
    def __init__(self, *args, **kwargs):
# checkin if kwargs is empty
        if (kwargs):
# deleting the key named class with the for loop
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.fromisoformat(value)
                else:
                    self.__dict__[key] = value
        else:    
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

   
    def __str__(self):
# prints attribute; classname, id, dict
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
    
    def save(self):
        self.updated_at = datetime.now()

# makes a copy of a dictionary

    def to_dict(self):
        copy_dict = self.__dict__.copy()
        copy_dict["__class__"] = self.__class__.__name__
        copy_dict["created_at"] = self.created_at.isoformat()
        copy_dict["updated_at"] = self.updated_at.isoformat()
        return copy_dict

