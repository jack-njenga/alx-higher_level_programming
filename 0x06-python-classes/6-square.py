#!/usr/bin/python3

"""
Square V6
upgrade based on V5
"""


class Square:
    """
    Square
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Intialization
        Args:
            size (int): size of the square
        """
        if (type(size) != int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

        if not isinstance(position, tuple) or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    @property
    def size(self):
        """
        retriving the size of the square
        """
        return (self.__size)

    @property
    def position(self):
        """
        retrives the position of the square.
        """
        return (self.__posstion)

    @size.setter
    def size(self, value):
        """
        size setter
        Args:
            value (int): the new size value of the square.
        """
        if (type(value) != int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @position.setter
    def position(self, value):
        """
        position setter
        Args:
            value (tuple): tuple for the co-ordinates of the square.
        """
        if not isinstance(position, tuple) or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        returns the area of the square.
        """
        ans = self.__size**2
        return (ans)

    def my_print(self):
        """
        prints the square in the stdout with '#' character.
        """
        if (self.__position[1] > 0):
            pos = 0
        else:
            pos = self.__position[0]
        if (self.__size == 0):
            print("")
        else:
            for i in range(self.__size):
                print("_" * pos, end="")
                print("#" * self.__size)
