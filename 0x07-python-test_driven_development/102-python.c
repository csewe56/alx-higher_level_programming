#include <Python.h>
#include <stdio.h>

void print_python_string(PyObject *p) 
{
	printf("[.] string object info\n");

	if (PyUnicode_Check(p))
	{
		PyUnicodeObject *str_obj = (PyUnicodeObject *)p;
        
		printf("  type: %s\n", (str_obj->state.compact ? "compact" : "compact unicode object"));
		printf("  length: %ld\n", PyUnicode_GET_LENGTH(p));
		printf("  value: %s\n", PyUnicode_AsUTF8(p));
	} 
	else 
	{
		printf("  [ERROR] Invalid String Object\n");
	}
}
int main(void) {
    PyObject *s1, *s2, *s3, *s4, *s5, *s6, *s7;

    s1 = PyUnicode_DecodeUTF8("The spoon does not exist", 24, "strict");
    s2 = PyUnicode_DecodeUTF8("ложка не существует", 19, "strict");
    s3 = PyUnicode_DecodeUTF8("La cuillère n'existe pas", 24, "strict");
    s4 = PyUnicode_DecodeUTF8("勺子不存在", 5, "strict");
    s5 = PyUnicode_DecodeUTF8("숟가락은 존재하지 않는다.", 14, "strict");
    s6 = PyUnicode_DecodeUTF8("スプーンは存在しない", 10, "strict");
    s7 = PyBytes_FromString("The spoon does not exist");

    print_python_string(s1);
    print_python_string(s2);
    print_python_string(s3);
    print_python_string(s4);
    print_python_string(s5);
    print_python_string(s6);
    print_python_string(s7);

    Py_DECREF(s1);
    Py_DECREF(s2);
    Py_DECREF(s3);
    Py_DECREF(s4);
    Py_DECREF(s5);
    Py_DECREF(s6);
    Py_DECREF(s7);

    return 0;
} 
