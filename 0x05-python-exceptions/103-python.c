#include <Python.h>
#include <stdio.h>

/**
 * print_python_list - gives data of the PyListObject
 * @p: the PyObject
 */
void print_python_list(PyObject *p) {
    // Check if the given object is a list
    if (!PyList_Check(p)) {
        fprintf(stderr, "Invalid PyListObject\n");
        return;
    }

    // Print basic information about the list
    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", ((PyVarObject *)p)->ob_size);
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    // Print information about each element in the list
    for (Py_ssize_t i = 0; i < ((PyVarObject *)p)->ob_size; ++i) {
        PyObject *element = ((PyListObject *)p)->ob_item[i];
        printf("Element %ld: %s\n", i, element->ob_type->tp_name);
    }
}

/**
 * print_python_bytes - gives data of the PyBytesObject
 * @p: the PyObject
 */
void print_python_bytes(PyObject *p) {
    // Check if the given object is bytes
    if (!PyBytes_Check(p)) {
        fprintf(stderr, "Invalid PyBytesObject\n");
        return;
    }

    // Print basic information about the bytes object
    printf("[.] bytes object info\n");
    printf("size: %ld\n", ((PyVarObject *)p)->ob_size);
    printf("trying string: %s\n", ((PyBytesObject *)p)->ob_sval);
    printf("first 10 bytes: ");

    // Print the first 10 bytes in hexadecimal format
    for (Py_ssize_t i = 0; i < (((PyVarObject *)p)->ob_size) && i < 10; ++i) {
        printf("%02x", (unsigned char)((PyBytesObject *)p)->ob_sval[i]);
        if (i < 9 && i + 1 < ((PyVarObject *)p)->ob_size)
            printf(" ");
    }
    printf("\n");
}

/**
 * print_python_float - gives data of the PyFloatObject
 * @p: the PyObject
 */
void print_python_float(PyObject *p) {
    // Check if the given object is a float
    if (!PyFloat_Check(p)) {
        fprintf(stderr, "Invalid PyFloatObject\n");
        return;
    }

    // Print basic information about the float object
    printf("[.] float object info\n");
    printf("value: %lf\n", ((PyFloatObject *)p)->ob_fval);
}
