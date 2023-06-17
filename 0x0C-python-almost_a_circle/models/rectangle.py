#!/usr/bin/python3
"""

"""
from models.base import Base



class Rectangle(Base):
    """
    This is the Rectangle class that inherits from the Base class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor for Rectangle class

        Args:
            width (int): Width of the rectangle
            height (int): Height of the rectangle
            x (int): x co-ordinate of the rectangle's position default: 0)
            y (int): y-coordinate of the rectangle's position (default: 0)
            id (int): ID value for the rectangle (default: None).
        """
        if type(width) == int:
            if width > 0:
                self.__width = width
            else:
                raise ValueError("{} must be > 0".format("width"))
        else:
            raise TypeError("{} must be an integer".format("width"))

        if type(height) == int:
            if height > 0:
                self.__height = height
            else:
                raise ValueError("{} must be > 0".format("height"))
        else:
            raise TypeError("{} must be an integer".format("height"))

        if type(x) == int:
            if x >= 0:
                self.__x = x
            else:
                raise ValueError("x must be >= 0")
        else:
            raise TypeError("{} must be an integer".format("x"))

        if type(y) == int:
            if y >= 0:
                self.__y = y
            else:
                raise ValueError("y must be >= 0")
        else:
            raise TypeError("{} must be an integer".format("y"))

        super().__init__(id)

    @property
    def width(self):
        """
        get current width
        """
        return self.__width

    @width.setter
    def width(self, new):
        """
        set new width
        """
        if type(new) == int:
            if new > 0:
                self.__width = new
            else:
                raise ValueError("width must be > 0")
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """
        get current height
        """
        return self.__height

    @height.setter
    def height(self, new):
        """
        set new height
        """
        if type(new) == int:
            if new > 0:
                self.__height = new
            else:
                raise ValueError("height must be > 0")
        else:
            raise TypeError("height must be an integer")

    @property
    def x(self):
        """
        get x co-ordinates
        """
        return self.__x
    @x.setter
    def x(self, new):
        """
        set new x co-ordinates
        """
        if type(new) == int:
            if new >= 0:
                self.__x = new
            else:
                raise ValueError("x must be >= 0")
        else:
            raise TypeError("x must be an integer")

    @property
    def y(self):
        """
        get y co-ordinates
        """
        return self.__y

    @y.setter
    def y(self, new):
        """
        set new y co-ordinates
        """
        if type(new) == int:
            if new >= 0:
                self.__y = new
            else:
                raise ValueError("y must be >= 0")
        else:
            raise TypeError("y must be an integer")
    
    def area(self):
        """
        get the rectangle area
        """
        w = self.__width
        h = self.__height
        return (w * h)

    def display(self):
        """
        Draws or prints the rectangle with "#" charactes
        """
        char = "#"
        w = self.__width
        h = self.__height
        x = self.__x
        y = self.__y
        for i in range(y):
            print()
        for i in range(h):
            print(" " * x, end="")
            print(char * w)

    def __str__(self):
        """
        str for printing rectangle details
        """
        _id = self.id
        x = self.x
        y = self.y
        w = self.width
        h = self.height
        _str = "[Rectangle] ({}) {}/{} - {}/{}".format(_id, x, y, w, h)
        return _str

    def update(self, *args, **kwargs):
        """
        This is for updating the rectangle attributes
        """
        args_map = {0: "id", 1: "width", 2: "height", 3: "x", 4: "y"}
        kwargs_map = {"id": "id", "width": "width", "height": "height", "x": "x", "y": "y"}
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
        Returns a dictionary containing all the data of a rectangle
        """
        dic = {}
        dic["id"] = self.id
        dic["width"] = self.width
        dic["height"] = self.height
        dic["x"] = self.x
        dic["y"] = self.y

        return dic
        
