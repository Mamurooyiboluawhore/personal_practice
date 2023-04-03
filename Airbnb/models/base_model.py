#!/usr/bin/python3
from datetime import datetime
import uuid

#a base class that defines all common attributes
class BaseModel():
#initializing
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
   
    def __str__(self):
#prints attribute; classname, id, dict
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"


