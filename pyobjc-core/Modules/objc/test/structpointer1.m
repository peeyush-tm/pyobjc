/*
 * This module is used in the unittests for object initialize.
 */
#include "Python.h"
#include "pyobjc-api.h"

#import <Foundation/Foundation.h>

struct TestStructPointerStruct {
    int i1;
};

struct UnwrappedStruct {
    int i1;
    int i2;
};

static struct TestStructPointerStruct myGlobal = { 1 };

@interface OC_TestStructPointer : NSObject
{
}
+(struct TestStructPointerStruct*)returnPointerToStruct;
+(struct UnwrappedStruct*)returnUnwrapped;
@end

@implementation OC_TestStructPointer
+(struct TestStructPointerStruct*)returnPointerToStruct
{
    return &myGlobal;
}

+(struct UnwrappedStruct*)returnUnwrapped
{
    return (struct UnwrappedStruct*)42;
}

@end


static PyMethodDef mod_methods[] = {
    { 0, 0, 0, 0 }
};

#if PY_VERSION_HEX >= 0x03000000

static struct PyModuleDef mod_module = {
    PyModuleDef_HEAD_INIT,
    "structpointer1",
    NULL,
    0,
    mod_methods,
    NULL,
    NULL,
    NULL,
    NULL
};

#define INITERROR() return NULL
#define INITDONE() return m

PyObject* PyInit_structpointer1(void);

PyObject* __attribute__((__visibility__("default")))
PyInit_structpointer1(void)

#else

#define INITERROR() return
#define INITDONE() return

void initstructpointer1(void);

void __attribute__((__visibility__("default")))
initstructpointer1(void)
#endif
{
    PyObject* m;

#if PY_VERSION_HEX >= 0x03000000
    m = PyModule_Create(&mod_module);
#else
    m = Py_InitModule4("structpointer1", mod_methods,
        NULL, NULL, PYTHON_API_VERSION);
#endif
    if (!m) {
        INITERROR();
    }

    if (PyObjC_ImportAPI(m) < 0) {
        INITERROR();
    }
    if (PyModule_AddObject(m, "OC_TestStructPointer",
        PyObjC_IdToPython([OC_TestStructPointer class])) < 0) {
        INITERROR();
    }

    INITDONE();
}
