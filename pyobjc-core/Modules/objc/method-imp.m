#include "pyobjc.h"

typedef struct {
    PyObject_HEAD
    IMP imp;
    PyObjC_CallFunc callfunc;
    PyObjCMethodSignature* signature;
    SEL selector;
    int flags;
} PyObjCIMPObject;

PyObject*
PyObjCIMP_New(IMP imp, SEL selector, PyObjC_CallFunc callfunc,
        PyObjCMethodSignature* signature, int flags)
{
    PyObjCIMPObject* result;

    result = PyObject_New(PyObjCIMPObject, &PyObjCIMP_Type);
    if (result == NULL) return NULL;

    result->imp = imp;
    result->selector = selector;
    result->callfunc = callfunc;
    result->signature = signature;

    if (signature) {
        Py_INCREF(signature);
    }

    result->flags = flags;
    return (PyObject*)result;
}

SEL
PyObjCIMP_GetSelector(PyObject* self)
{
    if (!PyObjCIMP_Check(self)) {
        PyErr_BadInternalCall();
        return NULL;
    }

    return ((PyObjCIMPObject*)self)->selector;
}

IMP
PyObjCIMP_GetIMP(PyObject* self)
{
    if (!PyObjCIMP_Check(self)) {
        PyErr_BadInternalCall();
        return NULL;
    }

    return ((PyObjCIMPObject*)self)->imp;
}

int
PyObjCIMP_GetFlags(PyObject* self)
{
    if (!PyObjCIMP_Check(self)) {
        PyErr_BadInternalCall();
        return -1;
    }

    return ((PyObjCIMPObject*)self)->flags;
}

PyObjC_CallFunc
PyObjCIMP_GetCallFunc(PyObject* self)
{
    if (!PyObjCIMP_Check(self)) {
        PyErr_BadInternalCall();
        return NULL;
    }

    return ((PyObjCIMPObject*)self)->callfunc;
}

PyObjCMethodSignature*
PyObjCIMP_GetSignature(PyObject* self)
{
    if (!PyObjCIMP_Check(self)) {
        PyErr_BadInternalCall();
        return NULL;
    }

    return ((PyObjCIMPObject*)self)->signature;
}

/* ========================================================================= */


static PyObject*
imp_call(PyObject* _self, PyObject* args, PyObject* kwds)
{
    PyObjCIMPObject* self = (PyObjCIMPObject*)_self;
    PyObject* pyself;
    PyObjC_CallFunc execute = NULL;
    PyObject* res;
    PyObject* pyres;
    Py_ssize_t argslen;
    PyObject* arglist;
    Py_ssize_t i;

    if (kwds != NULL && PyObject_Size(kwds) != 0) {
        PyErr_SetString(PyExc_TypeError,
            "Objective-C selectors don't support keyword arguments");
        return NULL;
    }

    argslen = PyTuple_Size(args);
    if (argslen < 1) {
        PyErr_SetString(PyExc_TypeError, "Missing argument: self");
        return NULL;
    }

    pyself = PyTuple_GET_ITEM(args, 0);
    if (pyself == NULL) {
        return NULL;
    }

    execute = self->callfunc;

    arglist = PyTuple_New(argslen - 1);
    for (i = 1; i < argslen; i++) {
        PyObject* v = PyTuple_GET_ITEM(args, i);

        if (v == NULL) {
            Py_DECREF(arglist);
            return NULL;
        }

        PyTuple_SET_ITEM(arglist, i-1, v);
        Py_INCREF(v);
    }

    pyres = res = execute((PyObject*)self, pyself, arglist);
    Py_DECREF(arglist);

    if (pyres != NULL
        && PyTuple_Check(pyres)
        && PyTuple_GET_SIZE(pyres) > 1
        && PyTuple_GET_ITEM(pyres, 0) == pyself) {
        pyres = pyself;
    }

    if (PyObjCObject_Check(pyself) && (((PyObjCObject*)pyself)->flags & PyObjCObject_kUNINITIALIZED)) {
        if (pyself != pyres && !PyErr_Occurred()) {
            PyObjCObject_ClearObject(pyself);
        }
    }

    if (pyres && PyObjCObject_Check(res)) {
        if (self->flags & PyObjCSelector_kRETURNS_UNINITIALIZED) {
            ((PyObjCObject*)pyres)->flags |= PyObjCObject_kUNINITIALIZED;

        } else if (((PyObjCObject*)pyres)->flags & PyObjCObject_kUNINITIALIZED) {
            ((PyObjCObject*)pyres)->flags &=
                ~PyObjCObject_kUNINITIALIZED;
            if (pyself && pyself != pyres && PyObjCObject_Check(pyself) && !PyErr_Occurred()) {
                PyObjCObject_ClearObject(pyself);
            }
        }
    }

    return res;
}

static PyObject*
imp_repr(PyObject* _self)
{
    PyObjCIMPObject* self = (PyObjCIMPObject*)_self;
    return PyText_FromFormat("<IMP %s at %p for %p>",
        sel_getName(self->selector),
        self, self->imp);
}

static void
imp_dealloc(PyObject* _self)
{
    PyObjCIMPObject* self = (PyObjCIMPObject*)_self;
    Py_XDECREF(self->signature);
    PyObject_Free(self);
}

PyDoc_STRVAR(imp_signature_doc, "Objective-C signature for the IMP");

static PyObject*
imp_signature(PyObject* _self, void* closure __attribute__((__unused__)))
{
    PyObjCIMPObject* self = (PyObjCIMPObject*)_self;
    if (self->signature) {
        return PyBytes_FromString(self->signature->signature);
    } else {
        Py_INCREF(Py_None);
        return Py_None;
    }
}

PyDoc_STRVAR(imp_selector_doc, "Objective-C name for the IMP");

static PyObject*
imp_selector(PyObject* _self, void* closure __attribute__((__unused__)))
{
    PyObjCIMPObject* self = (PyObjCIMPObject*)_self;
    return PyBytes_FromString(sel_getName(self->selector));
}

PyDoc_STRVAR(imp_class_method_doc,
    "True if this is a class method, False otherwise");

static PyObject*
imp_class_method(PyObject* _self, void* closure __attribute__((__unused__)))
{
    PyObjCIMPObject* self = (PyObjCIMPObject*)_self;
    return PyBool_FromLong(0 != (self->flags & PyObjCSelector_kCLASS_METHOD));
}

PyDoc_STRVAR(imp_is_alloc_doc,
"True if this is method returns a a freshly allocated object (uninitialized)\n"
"\n"
"NOTE: This field is used by the implementation."
);
static PyObject*
imp_is_alloc(PyObject* _self, void* closure __attribute__((__unused__)))
{
    PyObjCIMPObject* self = (PyObjCIMPObject*)_self;
    return PyBool_FromLong(0 != (self->flags & PyObjCSelector_kRETURNS_UNINITIALIZED));
}


static PyGetSetDef imp_getset[] = {
    {
        .name   = "isAlloc",
        .get    = imp_is_alloc,
        .doc    = imp_is_alloc_doc,
    },
    {
        .name   = "isClassMethod",
        .get    = imp_class_method,
        .doc    = imp_class_method_doc,
    },
    {
        .name   = "signature",
        .get    = imp_signature,
        .doc    = imp_signature_doc,
    },
    {
        .name   = "selector",
        .get    = imp_selector,
        .doc    = imp_selector_doc,
    },
    {
        .name   = "__name__",
        .get    = imp_selector,
        .doc    = imp_selector_doc,
    },

#if PY_VERSION_HEX >= 0x03030000
    {
        .name   = "__signature__",
        .get    = PyObjC_callable_signature_get,
        .doc    = "inspect.Signature for an IMP",
    },
#endif

    {
        .name   = NULL  /* SENTINEL */
    }
};

static PyObject*
imp_metadata(PyObject* self)
{
    PyObject* result = PyObjCMethodSignature_AsDict(
            ((PyObjCIMPObject*)self)->signature);
    int r;

    if (((PyObjCIMPObject*)self)->flags & PyObjCSelector_kCLASS_METHOD) {
        r = PyDict_SetItemString(result, "classmethod", Py_True);

    } else {
        r = PyDict_SetItemString(result, "classmethod", Py_False);
    }

    if (r == -1) {
        Py_DECREF(result);
        return NULL;
    }

    if (((PyObjCIMPObject*)self)->flags & PyObjCSelector_kRETURNS_UNINITIALIZED) {
        r = PyDict_SetItemString(result, "return_unitialized_object", Py_True);
        if (r == -1) {
            Py_DECREF(result);
            return NULL;
        }
    }

    return result;
}

static PyMethodDef imp_methods[] = {
    {
        .ml_name    = "__metadata__",
        .ml_meth    = (PyCFunction)imp_metadata,
        .ml_flags   = METH_NOARGS,
        .ml_doc     = "Return metadata for the method",
    },
    {
        .ml_name    = NULL /* SENTINEL */
    }
};


PyTypeObject PyObjCIMP_Type = {
    PyVarObject_HEAD_INIT(NULL, 0)
    .tp_name        = "objc.IMP",
    .tp_basicsize   = sizeof(PyObjCIMPObject),
    .tp_itemsize    = 0,
    .tp_dealloc     = imp_dealloc,
    .tp_repr        = imp_repr,
    .tp_call        = imp_call,
    .tp_getattro    = PyObject_GenericGetAttr,
    .tp_flags       = Py_TPFLAGS_DEFAULT,
    .tp_methods     = imp_methods,
    .tp_getset      = imp_getset,
};


/* ========================================================================= */

static PyObject*
call_instanceMethodForSelector_(PyObject* method, PyObject* self, PyObject* args)
{
    PyObject* sel;
    SEL selector;
    IMP retval;
    PyObject* attr;
    PyObject* res;

    if (!PyArg_ParseTuple(args, "O", &sel)) {
        return NULL;
    }

    if (depythonify_c_value(@encode(SEL), sel, &selector) == -1) {
        return NULL;
    }

    if (!PyObjCClass_Check(self)) {
        PyErr_Format(PyExc_TypeError,
            "Expecting instance of 'objc.objc_class' as 'self', "
            "got '%s'", Py_TYPE(self)->tp_name);
        return NULL;
    }

    PyObjC_DURING
        retval = (IMP)objc_msgSend(PyObjCClass_GetClass(self),
            PyObjCSelector_GetSelector(method),
            selector);

    PyObjC_HANDLER
        PyObjCErr_FromObjC(localException);
        retval = NULL;

    PyObjC_ENDHANDLER

    if (retval == NULL) {
        if (PyErr_Occurred()) {
            return NULL;
        }
        Py_INCREF(Py_None);
        return Py_None;
    }

    attr = PyObjCClass_FindSelector(self, selector, NO);
    if (attr == NULL) {
        return NULL;
    }

    /*
     * XXX: what if the method is implemented in Python. We should be able to deal with that!!!
     */

    if (!PyObjCNativeSelector_Check(attr)) {
        PyErr_Format(PyExc_TypeError, "Cannot locate Python representation of %s",
                sel_getName(selector));
        return NULL;
    }

    if (((PyObjCNativeSelector*)attr)->sel_call_func == NULL) {
        ((PyObjCNativeSelector*)attr)->sel_call_func = PyObjC_FindCallFunc(((PyObjCNativeSelector*)attr)->base.sel_class, ((PyObjCNativeSelector*)attr)->base.sel_selector);
        if (((PyObjCNativeSelector*)attr)->sel_call_func == NULL) {
            return NULL;
        }
    }

    res = PyObjCIMP_New(
            retval,
            selector,
            ((PyObjCNativeSelector*)attr)->sel_call_func,
            PyObjCSelector_GetMetadata(attr),
            PyObjCSelector_GetFlags(attr)
        );
    Py_DECREF(attr);
    return res;
}

static PyObject*
call_methodForSelector_(PyObject* method, PyObject* self, PyObject* args)
{
    PyObject* sel;
    SEL selector;
    struct objc_super super;
    IMP retval;
    PyObject* attr;
    PyObject* res;

    if (!PyArg_ParseTuple(args, "O", &sel)) {
        return NULL;
    }

    if (depythonify_c_value(@encode(SEL), sel, &selector) == -1) {
        return NULL;
    }

    if (PyObjCClass_Check(self)) {
        objc_superSetReceiver(super, PyObjCClass_GetClass(self));

    } else {
        objc_superSetReceiver(super, PyObjCObject_GetObject(self));
    }

    objc_superSetClass(super, object_getClass(objc_superGetReceiver(super)));

    PyObjC_DURING
        retval = (IMP)objc_msgSendSuper(&super,
            PyObjCSelector_GetSelector(method),
            selector);

    PyObjC_HANDLER
        PyObjCErr_FromObjC(localException);
        retval = NULL;
    PyObjC_ENDHANDLER

    if (retval == NULL) {
        if (PyErr_Occurred()) {
            return NULL;
        }
        Py_INCREF(Py_None);
        return Py_None;
    }

    if (PyObjCClass_Check(self)) {
        attr = PyObjCClass_FindSelector(self, selector, YES);

    } else {
        attr = PyObjCObject_FindSelector(self, selector);
    }

    if (attr == NULL) {
        return NULL;
    }

    /* FIXME:  We should be able to deal with Python methods as well */

    if (!PyObjCNativeSelector_Check(attr)) {
        PyErr_Format(PyExc_TypeError, "Cannot locate Python representation of %s",
                sel_getName(selector));
        return NULL;
    }


    /* FIXME: there should be a function for retrieving the call function */
    if (((PyObjCNativeSelector*)attr)->sel_call_func == NULL) {
        ((PyObjCNativeSelector*)attr)->sel_call_func = PyObjC_FindCallFunc(((PyObjCNativeSelector*)attr)->base.sel_class, ((PyObjCNativeSelector*)attr)->base.sel_selector);
        if (((PyObjCNativeSelector*)attr)->sel_call_func == NULL) {
            return NULL;
        }
    }

    res = PyObjCIMP_New(
            retval,
            selector,
            ((PyObjCNativeSelector*)attr)->sel_call_func,
            PyObjCSelector_GetMetadata(attr),
            PyObjCSelector_GetFlags(attr)
        );
    Py_DECREF(attr);
    return res;
}

int PyObjCIMP_SetUpMethodWrappers(void)
{
    int r;

    r = PyObjC_RegisterMethodMapping(
            nil,
            @selector(instanceMethodForSelector:),
            call_instanceMethodForSelector_,
            PyObjCUnsupportedMethod_IMP);
    if (r == -1) return -1;

    r = PyObjC_RegisterMethodMapping(
            nil,
            @selector(methodForSelector:),
            call_methodForSelector_,
            PyObjCUnsupportedMethod_IMP);
    if (r == -1) return -1;

    return 0;
}
