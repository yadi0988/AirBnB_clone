#!/usr/bin/env python3
"""class that defines all common attributes/methods for other classes"""

import uuid
from datetime import datetime


class BaseModel():
    """BaseModel class"""

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        return "\
[{}] ({}) {}\
".format(__class__.__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        obj_dict = {}
        for key, value in self.__dict__.items():
            if type(value) is datetime:
                obj_dict[key] = value.isoformat()
            else:
                obj_dict[key] = value
        obj_dict['__class__'] = __class__.__name__
        return obj_dict
