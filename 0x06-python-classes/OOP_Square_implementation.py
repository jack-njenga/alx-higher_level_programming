{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "72d36d1b",
   "metadata": {},
   "outputs": [],
   "source": [
    "import math, sys, os"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 127,
   "id": "24ba240a",
   "metadata": {},
   "outputs": [],
   "source": [
    "#!/usr/bin/python3\n",
    "\n",
    "\"\"\"\n",
    "Square V0\n",
    "Square implementation of Version 0\n",
    "\"\"\"\n",
    "\n",
    "\n",
    "class Square:\n",
    "    \"\"\"\n",
    "    Square Implementation\n",
    "    \"\"\"\n",
    "    def __init__(self, size=0):\n",
    "        \"\"\"\n",
    "        Args:\n",
    "            size (int): size of the square\n",
    "        \"\"\"\n",
    "        if (type(size) != int):\n",
    "            raise TypeError(\"size must be an int\")\n",
    "        elif (size < 0):\n",
    "            raise ValueError(\"size must be >= 0\")\n",
    "        else:\n",
    "            self.__size = size\n",
    "    def __mai__(self):\n",
    "        print(\"Square\")\n",
    "            \n",
    "    @property\n",
    "    def size(self):\n",
    "        \"\"\"\n",
    "        retrives the current size of the square\n",
    "        \"\"\"\n",
    "        return (self.__size)\n",
    "    \n",
    "    @size.setter\n",
    "    def size(self, new):\n",
    "        \"\"\"\n",
    "        new size setter of the square\n",
    "        Args:\n",
    "            new (int): the new value of the size of the square\n",
    "        \"\"\"\n",
    "        if (type(new) != int):\n",
    "            raise TypeError(\"size must be an int\")\n",
    "        elif (new < 0):\n",
    "            raise ValueError(\"size must be >= 0\")\n",
    "        else:\n",
    "            self.__size = new\n",
    "            \n",
    "    def area(self):\n",
    "        \"\"\"\n",
    "        returns the area of the square\n",
    "        \"\"\"\n",
    "        ans = self.__size**2\n",
    "        return ans\n",
    "    \n",
    "    def draw(self):\n",
    "        \"\"\"\n",
    "        draws the square using the current size\n",
    "        \"\"\"\n",
    "        size = self.__size\n",
    "        for i in range(size):\n",
    "            if i == 0 or i == size - 1:\n",
    "                print(\".\" * size)\n",
    "            else:\n",
    "                print(\":\" + \" \" * (size - 2) + \":\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 128,
   "id": "b50b2d08",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "5"
      ]
     },
     "execution_count": 128,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sq = Square(5)\n",
    "sz = sq.size\n",
    "sz"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 129,
   "id": "0f92a10e",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "10"
      ]
     },
     "execution_count": 129,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sz = sq.size = 10\n",
    "sz"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 130,
   "id": "84f0fa99",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "..........\n",
      ":        :\n",
      ":        :\n",
      ":        :\n",
      ":        :\n",
      ":        :\n",
      ":        :\n",
      ":        :\n",
      ":        :\n",
      "..........\n"
     ]
    }
   ],
   "source": [
    "sq.draw()\n",
    "\n",
    "# note that its not actually a square because of the ratio of\n",
    "# the horizontal space and the Vertical space ( \"<->\" and \"|^\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 131,
   "id": "218159eb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "..............................\n",
      ":                            :\n",
      ":                            :\n",
      ":                            :\n",
      ":                            :\n",
      ":                            :\n",
      ":                            :\n",
      ":                            :\n",
      ":                            :\n",
      ":                            :\n",
      ":                            :\n",
      ":                            :\n",
      ":                            :\n",
      ":                            :\n",
      ":                            :\n",
      ":                            :\n",
      ":                            :\n",
      ":                            :\n",
      ":                            :\n",
      ":                            :\n",
      ":                            :\n",
      ":                            :\n",
      ":                            :\n",
      ":                            :\n",
      ":                            :\n",
      ":                            :\n",
      ":                            :\n",
      ":                            :\n",
      ":                            :\n",
      "..............................\n"
     ]
    }
   ],
   "source": [
    "sq.size = 30\n",
    "sq.draw()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
