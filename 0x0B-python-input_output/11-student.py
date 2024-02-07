#!/usr/bin/python3
"""
module contains one class Student
"""


class Student:
    """
    class has one method
    """
    def __init__(self, first_name, last_name, age):
        """
        insantiate class
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, atrs=None):
        """
        returns a dictionary representation of a student instance
        """
        if atrs is None:
            return self.__dict__
        d = {}
        for att in atrs:
            if hasattr(self, att):
                d[att] = getattr(self, att)
        return d

    def reload_from_json(self, json):
        """
        replaces all attributes of the Student instance
        """
        for keys in json:
            setattr(self, keys, json[keys])
