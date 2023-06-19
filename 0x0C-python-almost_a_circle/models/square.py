#!/usr/bin/python3
"""
filename: square.py
Description: Contains the Square class of the models
Author: --i--
Date Created: 20 Jun 2023
"""
from models.rectangle import Rectangle as rec


class Square(rec):
    """
    Square Class
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialization
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """
        size getter
        """
        return self.height

    @size.setter
    def size(self, new):
        """
        size setter
        """
        self.width = new
        self.height = new

    def __str__(self):
        """
        str for printing the details of the square
        """
        _id = str(self.id)
        x = str(self.x)
        y = str(self.y)
        sz = str(self.size)
        _str = "[Square] ({}) {}/{} - {}".format(_id, x, y, sz)

        return _str

    def update(self, *args, **kwargs):
        """
        Updates the square attributes
        """
        args_map = {0: "id", 1: "size", 2: "x", 3: "y"}
        kwargs_map = {"id": "id", "size": "size", "x": "x", "y": "y"}
        if len(args):
            for n, arg in enumerate(args):
                if n in args_map:
                    setattr(self, args_map[n], arg)
        else:
            for attr_name, kwarg_key in kwargs_map.items():
                if kwarg_key in kwargs:
                    setattr(self, attr_name, kwargs[kwarg_key])

    def to_dictionary(self):
        """
        Returns a dictionary containing all the data of a square
        """
        dic = {}
        dic["id"] = self.id
        dic["size"] = self.size
        dic["x"] = self.x
        dic["y"] = self.y

        return dic
