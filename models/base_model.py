#!/user/bin/python3
""" Create BaseModel from dictionary"""

from datetime import datetime
from uuid import uuid4
from models import storage


class BaseModel:
    """ a class Basemodel
    instance attributes:
    id: string - assign with an uuid when an instance to convert to a string
        the goal is to have unique id for each BaseModel
    created_at: datetime - assign with the current datetime
        when an instance is created
    updated_at: datetime - assign with the current datetime
    when an instance is created
    and it will be updated every time you change your object
    """

    def __init__(self, *args, **kwargs):
        """ intialize the instances """
        convert = None
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ["created_at", "updated_at"]:
                        convert = datetime.strptime(
                            value, '%Y-%m-%dT%H:%M:%S.%f')
                        setattr(self, key, convert)
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.today()
            self.updated_at = datetime.today()
            models.storage.new(self)

    def __str__(self):
        """ returns a string """
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """updates the public instance attribute updated_at
        with the current datetime"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values
        of __dict__ of the instance"""

        new_dict = self.__dict__.copy()
        new_dict['__class__'] = str(self.__class__.__name__)
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict
