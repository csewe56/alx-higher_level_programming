#include <Python.h>

void print_list_info(PyObject* pList)
{
    if (PyList_Check(pList)) {
        printf("Python list length: %ld\n", PyList_Size(pList));
    } else {
        printf("Object is not a Python list.\n");
    }
}

void print_bytes_info(PyObject* pBytes)
{
    if (PyBytes_Check(pBytes)) {
        printf("Python bytes length: %ld\n", PyBytes_Size(pBytes));
    } else {
        printf("Object is not a Python bytes.\n");
    }
}
