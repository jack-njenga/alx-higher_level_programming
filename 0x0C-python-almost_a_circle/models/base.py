#!/usr/bin/python3
"""
Base Class
"""


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
        """
        import json

        if list_dictionaries == None:
            return "[]"
        else:
            js_list = ""
            for dic in list_dictionaries:
                js_list = js_list + json.dumps(dic)

            return "[" + js_list + "]"

    @classmethod
    def save_to_file(cls, list_objs):
        """
        """
        filename = cls.__name__ + ".json"
        obj = []
        if list_objs is not None:
            for i in list_objs:
                obj.append(cls.to_dictionary(i))
            with open(filename, "w", encoding="utf-8") as f:
                f.write(cls.to_json_string(obj))
