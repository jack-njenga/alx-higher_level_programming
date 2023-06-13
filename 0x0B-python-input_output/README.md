## Python - Input/Output

### Learning Objectives
- Why Python programming is awesome
- How to open a file
- How to write text in a file
- How to read the full content of a file
- How to read a file line by line
- How to move the cursor in a file
- How to make sure a file is closed after using it
- What is and how to use the with statement
- What is JSON
- What is serialization
- What is deserialization
- How to convert a Python data structure to a JSON string
- How to convert a JSON string to a Python data structure

### Resources
Read or watch:
- [7.2. Reading and Writing Files](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
- [8.7. Predefined Clean-up Actions](https://docs.python.org/3/tutorial/errors.html#predefined-clean-up-actions)
- [Dive Into Python 3: Chapter 11. Files (until “11.4 Binary Files” (included))](https://histo.ucsf.edu/BMS270/diveintopython3-r802.pdf)
- [JSON encoder and decoder](https://docs.python.org/3/library/json.html)
- [Learn to Program 8 : Reading / Writing Files](https://www.youtube.com/watch?v=EukxMIsNeqU)
- [Automate the Boring Stuff with Python (ch. 8 p 180-183 and ch. 14 p 326-333)](https://automatetheboringstuff.com/)
- [All about py-file I/O](https://www.google.com/search?q=All+about+py-file+I%2FO&sourceid=chrome&ie=UTF-8)


#### Tasks
- [x] 0-read_file.py - Write a function that reads a text file (UTF8) and prints it to stdout:

	- Prototype: def read_file(filename=""):
	- You must use the with statement
	- You don’t need to manage file permission or file doesn't exist exceptions.
	- You are not allowed to import any module

- [x] 1-write_file.py - Write a function that writes a string to a text file (UTF8) and returns the number of characters written:

	- Prototype: def write_file(filename="", text=""):
	- You must use the with statement
	- You don’t need to manage file permission exceptions.
	- Your function should create the file if doesn’t exist.
	- Your function should overwrite the content of the file if it already exists.
	- You are not allowed to import any module

- [x] 2-append_write.py - Write a function that appends a string at the end of a text file (UTF8) and returns the number of characters added:

	- Prototype: def append_write(filename="", text=""):
	- If the file doesn’t exist, it should be created
	- You must use the with statement
	- You don’t need to manage file permission or file doesn't exist exceptions.
	- You are not allowed to import any module

- [x] 3-to_json_string.py - Write a function that returns the JSON representation of an object (string):

	- Prototype: def to_json_string(my_obj):
	- You don’t need to manage exceptions if the object can’t be serialized.

- [x] 4-from_json_string.py - Write a function that returns an object (Python data structure) represented by a JSON string:

	- Prototype: def from_json_string(my_str):
	- You don’t need to manage exceptions if the JSON string doesn’t represent an object.

- [x] 5-save_to_json_file.py - Write a function that writes an Object to a text file, using a JSON representation:

	- Prototype: def save_to_json_file(my_obj, filename):
	- You must use the with statement
	- You don’t need to manage exceptions if the object can’t be serialized.
	- You don’t need to manage file permission exceptions.

- [x] 6-load_from_json_file.py - Write a function that creates an Object from a “JSON file”:

	- Prototype: def load_from_json_file(filename):
	- You must use the with statement
	- You don’t need to manage exceptions if the JSON string doesn’t represent an object.
	- You don’t need to manage file permissions / exceptions.

- [x] 7-add_item.py - Write a script that adds all arguments to a Python list, and then save them to a file:

	- You must use your function save_to_json_file from 5-save_to_json_file.py
	- You must use your function load_from_json_file from 6-load_from_json_file.py
	- The list must be saved as a JSON representation in a file named add_item.json
	- If the file doesn’t exist, it should be created
You don’t need to manage file permissions / exceptions.

- [x] 8-class_to_json.py - Write a function that returns the dictionary description with simple data structure (list, dictionary, string, integer and boolean) for JSON serialization of an object:

	- Prototype: def class_to_json(obj):
	- obj is an instance of a Class
	- All attributes of the obj Class are serializable: list, dictionary, string, integer and boolean
	- You are not allowed to import any module

- [x] 9-student.py - Write a class Student that defines a student by:

	- Public instance attributes:
		> first_name
		> last_name
		> age
	- Instantiation with first_name, last_name and age: def __init__(self, first_name, last_name, age):
	- Public method def to_json(self): that retrieves a dictionary representation of a Student instance (same as 8-class_to_json.py)
	- You are not allowed to import any module

- [x] 10-student.py - Write a class Student that defines a student by: (based on 9-student.py)

	- Public instance attributes:
		> first_name
		> last_name
		> age
	- Instantiation with first_name, last_name and age: def __init__(self, first_name, last_name, age):
	- Public method def to_json(self, attrs=None): that retrieves a dictionary representation of a Student instance (same as 8-class_to_json.py):
		> If attrs is a list of strings, only attribute names contained in this list must be retrieved.
		> Otherwise, all attributes must be retrieved
	- You are not allowed to import any module

- [x] 11-student.py - Write a class Student that defines a student by: (based on 10-student.py)

	- Public instance attributes:
		> first_name
		> last_name
		> age
	- Instantiation with first_name, last_name and age: def __init__(self, first_name, last_name, age):
	- Public method def to_json(self, attrs=None): that retrieves a dictionary representation of a Student instance (same as 8-class_to_json.py):
		> If attrs is a list of strings, only attributes name contain in this list must be retrieved.
		> Otherwise, all attributes must be retrieved
	- Public method def reload_from_json(self, json): that replaces all attributes of the Student instance:
		> You can assume json will always be a dictionary
		> A dictionary key will be the public attribute name
		> A dictionary value will be the value of the public attribute
	- You are not allowed to import any module
- Now, you have a simple implementation of a serialization and deserialization mechanism (concept of representation of an object to another format, without losing any information and allow us to rebuild an object based on this representation)

- [x] 12-pascal_triangle.py - Technical interview preparation:
	- **Technical interview preparation:**

	- You are not allowed to google anything
	- Whiteboard first
- Create a function def pascal_triangle(n): that returns a list of lists of integers representing the Pascal’s triangle of n:

	- Returns an empty list if n <= 0
	- You can assume n will be always an integer
	- You are not allowed to import any module 

#### Advance tasks
- [ ]
- [ ]
