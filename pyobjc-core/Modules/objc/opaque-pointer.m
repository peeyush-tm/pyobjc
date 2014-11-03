/*
 * Generic support for opaque pointer types, such as NSZone*
 */
#include "pyobjc.h"

typedef struct {
    PyObject_HEAD

    void* pointer_value;
} OpaquePointerObject;

static PyMemberDef opaque_members[] = {
    {
        .name   = "__pointer__",
        .type   = T_LONG,
        .offset = offsetof(OpaquePointerObject, pointer_value),
        .flags  = READONLY,
        .doc    = "raw value of the pointer"
    },
    {
        .name   = NULL  /* SENTINEL */
    }
};

static PyObject*
as_cobject(PyObject* self)
{
    if (((OpaquePointerObject*)self)->pointer_value == NULL) {
        Py_INCREF(Py_None);
        return Py_None;
    }

    return PyCapsule_New(((OpaquePointerObject*)self)->pointer_value, "objc.__opaque__", NULL);
}

static PyObject*
as_ctypes_voidp(PyObject* self)
{
    PyObject* c_void_p;

    if (((OpaquePointerObject*)self)->pointer_value == NULL) {
        Py_INCREF(Py_None);
        return Py_None;
    }

    c_void_p = PyObjC_get_c_void_p();
    if (c_void_p == NULL) {
        return NULL;
    }

    return PyObject_CallFunction(c_void_p, "k",
        (long)((OpaquePointerObject*)self)->pointer_value);
}

static PyObject*
opaque_sizeof(PyObject* self)
{
    return PyLong_FromSsize_t(Py_TYPE(self)->tp_basicsize);
}



static PyMethodDef opaque_methods[] = {
    {
        .ml_name    = "__cobject__",
        .ml_meth    = (PyCFunction)as_cobject,
        .ml_flags   = METH_NOARGS,
        .ml_doc     = "get a CObject representing this object"
    },
    {
        .ml_name    = "__c_void_p__",
        .ml_meth    = (PyCFunction)as_ctypes_voidp,
        .ml_flags   = METH_NOARGS,
        .ml_doc     = "get a ctypes.void_p representing this object"
    },
    {
        .ml_name    = "__sizeof__",
        .ml_meth    = (PyCFunction)opaque_sizeof,
        .ml_flags   = METH_NOARGS,
    },
    {
        .ml_name    = NULL /* SENTINEL */
    }
};


static PyObject*
opaque_new(PyTypeObject* type, PyObject* args, PyObject* kwds)
{
static  char* keywords[] = { "cobject", "c_void_p", NULL };
    PyObject* cobject = NULL;
    PyObject* c_void_p = NULL;

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "|OO", keywords, &cobject, &c_void_p)) {
        return NULL;
    }

    if (cobject != NULL && c_void_p != NULL) {
        PyErr_SetString(PyExc_ValueError,
            "pass 'cobject' or 'c_void_p', not both");
        return NULL;
    }

    if (cobject != NULL) {
        OpaquePointerObject* result;
        void* p;

        if (!PyCapsule_CheckExact(cobject)) {
            PyErr_SetString(PyExc_TypeError,
                 "'cobject' argument is not a PyCapsule");
            return NULL;
        }

        p = PyCapsule_GetPointer(cobject, "objc.__opaque__");
        if (PyErr_Occurred()) {
            return NULL;
        }

        result = PyObject_New(OpaquePointerObject, type);
        if (result == NULL) {
            return NULL;
        }

        result->pointer_value = p;
        return (PyObject*)result;

    } else if (c_void_p != NULL) {
        OpaquePointerObject* result;
        void* p;
        PyObject* attrval;

        if (PyLong_Check(c_void_p)
#if PY_MAJOR_VERSION == 2
                || PyInt_Check(c_void_p)
#endif
            ) {
                attrval = c_void_p;
                Py_INCREF(attrval);

        } else {
            attrval = PyObject_GetAttrString(c_void_p, "value");
            if (attrval == NULL) {
                return NULL;
            }
        }

        if (
#if PY_MAJOR_VERSION == 2
            PyInt_Check(attrval) ||
            /* NOTE: PyLong_AsVoidPtr works on Int objects as well */
#endif /* PY_MAJOR_VERSION == 2 */
            PyLong_Check(attrval)
        ) {
            p = PyLong_AsVoidPtr(attrval);
            if (p == NULL && PyErr_Occurred()) {
                Py_DECREF(attrval);
                return NULL;
            }

        } else {
            PyErr_SetString(PyExc_ValueError,
                "c_void_p.value is not an integer");
            return NULL;
        }

        Py_DECREF(attrval);
        result = PyObject_New(OpaquePointerObject, type);
        if (result == NULL) {
            return NULL;
        }

        result->pointer_value = p;
        return (PyObject*)result;

    } else {
        PyErr_Format(PyExc_TypeError, "Cannot create %s objects",
                type->tp_name);
        return NULL;
    }
}

static void
opaque_dealloc(PyObject* self)
{
    PyObject_Del(self);
}

static void
opaque_from_c(
    ffi_cif* cif __attribute__((__unused__)),
    void* retval,
    void** args,
    void* userdata)
{
    void* pointer_value = *(void**)args[0];
    PyTypeObject* opaque_type = (PyTypeObject*)userdata;
    OpaquePointerObject* result;

    result = PyObject_New(OpaquePointerObject, opaque_type);
    if (result == NULL) {
        *(PyObject**)retval = NULL;
        return;
    }

    result->pointer_value = pointer_value;
    *(PyObject**)retval = (PyObject*)result;
}

static void
opaque_to_c(
    ffi_cif* cif __attribute__((__unused__)),
    void* retval,
    void** args,
    void* userdata)
{
    PyObject* obj = *(PyObject**)args[0];
    void* pObj = *(void**)args[1];
    PyTypeObject* opaque_type = (PyTypeObject*)userdata;

    if (!PyObject_TypeCheck((obj), opaque_type)) {
        *(void**)pObj = (void*)0xDEADBEEF; /* force errors */
        PyErr_Format(PyExc_TypeError,
            "Need instance of %s, got instance of %s",
            opaque_type->tp_name, Py_TYPE(obj)->tp_name);
        *(int*)retval = -1;
        return;
    }

    *(void**)pObj = ((OpaquePointerObject*)obj)->pointer_value;
    *(int*)retval = 0;
}


/*
 * Usage:
 *     PyDict_SetItemString(moduleDict, "NSZonePointer",
 *         PyObjCCreateOpaquePointerType(
 *             "Foundation.NSZonePointer",
 *             @encode(NSZone*),
 *             NSZonePointer_doc));
 */
PyObject*
PyObjCCreateOpaquePointerType(
        const char* name,
        const char* typestr,
        const char* docstr)
{
static const char convert_cif_signature[] = { _C_INT, _C_PTR, _C_VOID, _C_PTR, _C_VOID, 0 };
static const char new_cif_signature[]     = { _C_PTR, _C_VOID, _C_PTR, _C_VOID, 0 };
static  ffi_cif* convert_cif = NULL;
static  ffi_cif* new_cif = NULL;

    PyHeapTypeObject* newType = NULL;
    PyObjCPointerWrapper_ToPythonFunc from_c = NULL;
    PyObjCPointerWrapper_FromPythonFunc to_c = NULL;
    ffi_closure* cl = NULL;
    ffi_status rv;
    int r;
    PyObject* v = NULL;
    PyObject* w = NULL;
    const char* name_dot;

    if (new_cif == NULL) {
        PyObjCMethodSignature* signature;
        signature = PyObjCMethodSignature_FromSignature(new_cif_signature, NO);
        new_cif = PyObjCFFI_CIFForSignature(signature);
        Py_DECREF(signature);
        if (new_cif == NULL) {
            return NULL;
        }
    }

    if (convert_cif == NULL) {
        PyObjCMethodSignature* signature;
        signature = PyObjCMethodSignature_FromSignature(convert_cif_signature, YES);
        convert_cif = PyObjCFFI_CIFForSignature(signature);
        Py_DECREF(signature);
        if (convert_cif == NULL) {
            return NULL;
        }
    }

    newType = (PyHeapTypeObject*)PyType_Type.tp_alloc(&PyType_Type, 0);
    if (newType == NULL) {
        return NULL;
    }

    newType->ht_type.tp_basicsize = sizeof(OpaquePointerObject);
    newType->ht_type.tp_dealloc = opaque_dealloc;
    newType->ht_type.tp_getattro = PyObject_GenericGetAttr;
    newType->ht_type.tp_flags = Py_TPFLAGS_DEFAULT|Py_TPFLAGS_HEAPTYPE;
    newType->ht_type.tp_methods = opaque_methods;
    newType->ht_type.tp_members = opaque_members;
    newType->ht_type.tp_new = opaque_new;

    newType->ht_type.tp_as_number = &newType->as_number;
    newType->ht_type.tp_as_mapping = &newType->as_mapping;
    newType->ht_type.tp_as_sequence = &newType->as_sequence;
    newType->ht_type.tp_as_buffer = &newType->as_buffer;

    /* Force type to be a heap type. Not only is that technically correct,
     * it also makes the type mutable (annoyingly enough all heap types
     * and only heap types are mutable).
     */
    newType->ht_type.tp_flags |= Py_TPFLAGS_HEAPTYPE;
    newType->ht_type.tp_flags &= ~Py_TPFLAGS_HAVE_GC;

    name_dot = strchr(name, '.');
    if (name_dot != NULL && name_dot[1] != '\0') {
        newType->ht_name = PyText_FromString(name_dot + 1);
    } else {
        newType->ht_name = PyText_FromString(name);
    }
    if (newType->ht_name == NULL) {
        PyMem_Free(newType);
        PyErr_NoMemory();
        return NULL;
    }

    newType->ht_type.tp_name = PyText_AsString(newType->ht_name);

#if PY_VERSION_HEX >= 0x03030000
    newType->ht_qualname = newType->ht_name;
    Py_INCREF(newType->ht_qualname);
#endif

    v = PyDict_New();
    if (v == NULL) {
        goto error_cleanup;
    }

    w = PyBytes_FromString(typestr);
    if (w ==  NULL) {
        goto error_cleanup;
    }

    if (PyDict_SetItemString(v, "__typestr__", w) != 0) {
        Py_CLEAR(w);
        goto error_cleanup;
    }

    Py_CLEAR(w);

    if (name_dot == NULL || name_dot[1] == '\0') {
        w = PyText_FromString("objc");
        if (w == NULL) {
            goto error_cleanup;
        }
        if (PyDict_SetItemString(v, "__module__", w) != 0) {
            Py_CLEAR(w);
            goto error_cleanup;
        }
        Py_CLEAR(w);
    } else {
        w = PyText_FromStringAndSize(name, name_dot - name);
        if (w == NULL) {
            goto error_cleanup;
        }
        if (PyDict_SetItemString(v, "__module__", w) != 0) {
            Py_CLEAR(w);
            goto error_cleanup;
        }
        Py_CLEAR(w);
    }

    newType->ht_type.tp_dict = v; v = NULL;

    if (docstr != NULL) {
        newType->ht_type.tp_doc = PyObjCUtil_Strdup(docstr);
        if (newType->ht_type.tp_doc == NULL) {
            PyErr_NoMemory();
            goto error_cleanup;
        }
    }

    cl = PyObjC_malloc_closure();
    if (cl == NULL) {
        goto error_cleanup;
    }

    newType->ht_type.tp_alloc = PyType_GenericAlloc;
    Py_INCREF(Py_TYPE(&(newType->ht_type)));
    PyType_Ready((PyTypeObject*)newType);

    rv = ffi_prep_closure(cl, convert_cif, opaque_to_c, newType);
    if (rv != FFI_OK) {
        PyErr_Format(PyExc_RuntimeError,
            "Cannot create FFI closure: %d", rv);
        goto error_cleanup;
    }
    Py_INCREF(newType); /* Store reference, hence INCREF */

    to_c = (PyObjCPointerWrapper_FromPythonFunc)cl;
    cl = NULL;

    cl = PyObjC_malloc_closure();
    if (cl == NULL) {
        goto error_cleanup;
    }

    rv = ffi_prep_closure(cl, new_cif, opaque_from_c, newType);
    if (rv != FFI_OK) {
        PyErr_Format(PyExc_RuntimeError,
            "Cannot create FFI closure: %d", rv);
        goto error_cleanup;
    }
    Py_INCREF(newType); /* Store reference, hence INCREF */

    from_c = (PyObjCPointerWrapper_ToPythonFunc)cl;
    cl = NULL;

    r = PyObjCPointerWrapper_Register(name, typestr, from_c, to_c);
    if (r == -1) {
        goto error_cleanup;
    }

    return (PyObject*)newType;

error_cleanup:
    if (newType) {
        if (newType->ht_type.tp_name) PyMem_Free((char*)newType->ht_type.tp_name);
        if (newType->ht_type.tp_doc) PyMem_Free((char*)newType->ht_type.tp_doc);
        Py_XDECREF(newType->ht_type.tp_dict);
        PyMem_Free(newType);
    }

    if (cl) {
        PyObjC_free_closure(cl);
    }

    if (to_c) {
        PyObjC_free_closure((ffi_closure*)to_c);
    }

    if (from_c) {
        PyObjC_free_closure((ffi_closure*)from_c);
    }

    Py_XDECREF(v);
    Py_XDECREF(w);
    return NULL;
}
