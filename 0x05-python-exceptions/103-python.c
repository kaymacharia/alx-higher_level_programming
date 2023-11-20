#include <Python.h>
#include <stdio.h>
#include <floatobject.h>
/**
 * print_python_list - prints basic information about Python lists
 * @p: the PyObject representing a list
 */
void print_python_list(PyObject *p) {
    if (!PyList_Check(p)) {
        fprintf(stderr, "Invalid PyListObject\n");
        return;
    }

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", ((PyVarObject *)p)->ob_size);
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    printf("[*] Element 0: %s\n", Py_TYPE(PyList_GetItem(p, 0))->tp_name);
    printf("[*] Element 1: %s\n", Py_TYPE(PyList_GetItem(p, 1))->tp_name);
    printf("[*] Element 2: %s\n", Py_TYPE(PyList_GetItem(p, 2))->tp_name);
}
/**
 * print_python_bytes - prints basic information about Python bytes
 * @p: the PyObject representing bytes
 */

void print_python_bytes(PyObject *p) {
    if (!PyBytes_Check(p)) {
        fprintf(stderr, "Invalid PyBytesObject\n");
        return;
    }

    printf("[.] bytes object info\n");
    printf("size: %ld\n", ((PyVarObject *)p)->ob_size);
    printf("trying string: %s\n", ((PyBytesObject *)p)->ob_sval);
    printf("first 10 bytes: ");

    for (Py_ssize_t i = 0; i < (((PyVarObject *)p)->ob_size) && i < 10; ++i) {
        printf("%02x", (unsigned char)((PyBytesObject *)p)->ob_sval[i]);
        if (i < 9 && i + 1 < ((PyVarObject *)p)->ob_size)
            printf(" ");
    }
    printf("\n");
}
/**
 * print_python_float - prints basic information about Python float
 * @p: the PyObject representing a float
 */

void print_python_float(PyObject *p) {
    if (!PyFloat_Check(p)) {
        fprintf(stderr, "Invalid PyFloatObject\n");
        return;
    }

    printf("[.] float object info\n");
    printf("value: %lf\n", ((PyFloatObject *)p)->ob_fval);
}
