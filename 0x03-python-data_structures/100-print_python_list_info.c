#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <Python.h>
/**
 * prints some basic info about Python lists.
 * @p: PyObject representing a Python list
 *
 * Return: void
 */

void print_python_list_info(PyObject *p)
{
	Py_ssize_t size = PyList_size(p);
	Py_ssize_t n;
	PyObject *item;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (n = 0; i < size; i++)
	{
		i = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", 1, Py_TYPE(i)->tp_name);
	}
}
