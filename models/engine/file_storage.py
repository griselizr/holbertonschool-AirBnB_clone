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
        with open(self.__file_path, mode='w', encoding='utf-8') as file:

    def reload(self):
        """deserializes the JSON file to __objects"""

        with open(self.__filepath, 'r') as file:
