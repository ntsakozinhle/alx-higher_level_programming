#define PY_SIZE_T_CLEAN
#define _GNU_SOURCE
#include <stdio.h>
#include <Python.h>
#include <object.h>
#include <listobject.h>

void print_python_list_info(PyObject *p)
{
	long int size = PyList_Size(p);
	long int allocated = ((PyListObject *)p)->allocated;
	int i;

	printf("[*] size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", allocated);
	for (i = 0; i < size; i++)
		printf("Element %i: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
}
