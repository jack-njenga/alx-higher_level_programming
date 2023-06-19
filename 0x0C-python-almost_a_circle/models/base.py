#!/usr/bin/python3
"""
File: base.py
Description: Contains the Base class of the models implementation
Author: --i--
Date Created: 20 Jun 2023
"""
import json


class Base:
    """
    Base Class
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Keeps count on id

        Args:
            id (int): id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """
        returns the JSON string representation of list_dictionaries.
        Args:
            list_dic... (list): the list of dic... to convert to json
        """

        if list_dictionaries is None:
            return "[]"
        else:
            js_list = ""
            for dic in list_dictionaries:
                js_list = js_list + json.dumps(dic)

        return "[" + js_list + "]"

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation of list_objs to a file
        Args:
            cls (obj): a class instance
            list_objs (list): list of objects
        """

        filename = cls.__name__ + ".json"
        obj = []
        if list_objs is not None:
            for i in list_objs:
                obj.append(cls.to_dictionary(i))
            with open(filename, "w", encoding="utf-8") as f:
                f.write(cls.to_json_string(obj))

    def from_json_string(json_string):
        """
        returns the list of the JSON string representation json_string.
        """
        jstr_l = []
        if json_string is None or len(json_string) == 0:
            return []
        j_obj = json.dumps(json_string)
        return [j_obj]

    @classmethod
    def create(cls, **dictionary):
        """
        returns an instance with all attributes already set.
        """

        if cls.__name__ == "Rectangle":
            hold = cls(2, 2)
        elif cls.__name__ == "Square":
            hold = cls(2)
        else:
            hold.update(**dictionary)

            return hold

    @classmethod
    def load_from_file(cls):
        """
        returns a list of instances.
        """
        obj_l = []
        fname = cls.__name__ + ".json"
        try:
            with open(fname, "r", encoding="utf-8") as fl:
                content = fl.read()
                obj_l = cls.from_json_string(content)

                for i, obj in enumerate(obj_l):
                    obj_l[i] = cls.create(**obj_l[i])
        except FileNotFoundError:
            return []
        except Exception:
            pass

        return obj_l

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        saves the rectangle data in CSV:
        """
        import csv
        fname = cls.__name__ + ".csv"
