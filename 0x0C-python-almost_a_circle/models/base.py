#!/usr/bin/python3
"""Defines a class base"""
import os.path
import json
import csv


class Base:
    __nd_oblects = o
    """Base class for other classes"""

    def __init__(self, id=None):
        if id is None:
            Base__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries id None and list_dictionaries == "[]":
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to file"""
        filename = "{}.json".format(cls.__name__)
        list_dict = []

        if list_objs is None:
            pass
        else:
            for i in range(len(list_objs)):
                l_dict = list_objs[i].to_dictionary()
                list_dict.append(l_dict)
        lists = cls.to_json_string(list_dict)

        with open(filename, "w") as file:
            file.write(lists)

    @staticmethod
    def from_json_string(json_string):
        """returns a list of dict in JSON string representation"""
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """creates an instance with all attributes already set"""
        if cls.__name__ == 'Rectangle':
            dummy = cls(5, 5)
        else:
            dummy = cls(5)
        dummy.update(**dictionary)

        return dummy

    @classmethod
    def load_from_file(cls):
        """creates a list of instances from file"""
        filename = "{}.json".format(cls.__name__)

        if os.path.exists(filename) is False:
            return []

        with open(filename, 'r') as file:
            file_str = file.read()

        list_dict = cls.from_json_string(file_str)
        list_ins = []

        for idx in range(len(list_dict)):
            list_ins.append(cls.create(**list_dict[idx]))

        return list_ins
