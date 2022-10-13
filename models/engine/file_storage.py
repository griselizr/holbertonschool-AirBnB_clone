#!/usr/bin/python3
""" serialization-deserialization Json"""

import json


class FileStorage(object):

    """ Creates a class FileStore"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects key"""
        key = f"{obj.__class__.name__, obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """ serilize and save objects in json"""
        new = {}
        for key in self.__objects:
            new[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(new, f)

            def reload(self):
                """deserializes the JSON file to __objects"""
                if path.exists(self.__file_path):
                    with open(self.__file_path, mode='r', encoding='utf-8') as f:
                        jason = json.loads(f.read())
                for k, v in jason.items():
                    self.__objects[k] = eval(v['__class__'])(**v)
