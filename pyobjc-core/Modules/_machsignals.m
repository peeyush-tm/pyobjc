/*
 * Nicer signal handling, integrated into the runloop.
 */

#include <Python.h>
#include <mach/mach.h>
#include <mach/mach_error.h>
#include <CoreFoundation/CoreFoundation.h>
#include "pyobjc-api.h"

PyDoc_STRVAR(machsignals_doc,
    "_machsignals - signal handling integrated into the runloop\n"
    "\n"
    "This module exports a dictionary that contains the functions that \n"
    "should be called when a signal is caught.\n"
    "\n"
    "The function 'handleSignal' installs a C signal handler that will \n"
    "make sure our signal handler is called."
);

static mach_port_t exit_m_port       = MACH_PORT_NULL;
static PyObject *signalmapping;


static void
SIGCallback(CFMachPortRef port __attribute__((__unused__)), void *msg, CFIndex size __attribute__((__unused__)), void *info __attribute__((__unused__)))
{
    PyObject *tmp;
    PyObject *callable;
    int signum;
    /* this is abuse of msgh_id */
    signum = ((mach_msg_header_t*)msg)->msgh_id;
    if (!signalmapping) {
        return;
    }
    PyObjC_BEGIN_WITH_GIL
        do {
            tmp = PyInt_FromLong((long)signum);
            if (!tmp) break;

            callable = PyDict_GetItem(signalmapping, tmp);
            Py_DECREF(tmp);
            if (!callable) {
                tmp = NULL;
                break;
            }

            tmp = PyObject_CallFunction(callable, "i", signum);
            Py_XDECREF(tmp);
        } while (0);
        if (!tmp)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
}

static void
HandleSIG(int signum)
{
    /*
     * Send a mach_msg to ourselves (since that is signal safe) telling us
     * to handle a signal.
     */
    mach_msg_return_t msg_result;
    mach_msg_header_t header;

    header.msgh_bits = MACH_MSGH_BITS(MACH_MSG_TYPE_MAKE_SEND, 0);
    header.msgh_remote_port = exit_m_port;
    header.msgh_local_port = MACH_PORT_NULL;
    header.msgh_size = sizeof(header);
    /* this is abuse of msgh_id */
    header.msgh_id = signum;

    msg_result = mach_msg_send(&header);
}

PyDoc_STRVAR(machsignals_handleSignal_doc,
    "handle_signal(signum) -> None\n"
    "\n"
    "Handle a signal using the registered mach callback\n"
    "Raises an ObjC exception if the callback fails"
);
static PyObject*
machsignals_handleSignal(PyObject *self __attribute__((__unused__)), PyObject *args, PyObject *kwds)
{
    static char* keywords[] = { "signum", 0 };
    int signum;

    if (!PyArg_ParseTupleAndKeywords(args, kwds,
        "i:handleSignal", keywords,
        &signum)) {
        return NULL;
    }

    signal(signum, HandleSIG);

    Py_INCREF(Py_None);
    return Py_None;
}

static PyMethodDef mod_methods[] = {
    {
            "handle_signal",
            (PyCFunction)machsignals_handleSignal,
            METH_VARARGS|METH_KEYWORDS,
            machsignals_handleSignal_doc
    },
    { 0, 0, 0, 0}
};

PyObjC_MODULE_INIT(_machsignals)
{
    PyObject* m;
    m = PyObjC_MODULE_CREATE(_machsignals)
    if (m == NULL) {
        PyObjC_INITERROR();
    }

    CFMachPortRef e_port;
    CFRunLoopSourceRef e_rls;

    if (PyObjC_ImportAPI(m) < 0) {
        PyErr_Print();
	PyObjC_INITERROR();
    }

    signalmapping = PyDict_New();
    if (!signalmapping) {
        PyObjC_INITERROR();
    }

    PyObject_SetAttrString(m, "_signalmapping", signalmapping);

    e_port = CFMachPortCreate(NULL, SIGCallback, NULL, NULL);
    exit_m_port = CFMachPortGetPort(e_port);
    e_rls = CFMachPortCreateRunLoopSource(NULL, e_port, 0);
    CFRunLoopAddSource(CFRunLoopGetCurrent(), e_rls, kCFRunLoopDefaultMode);
    CFRelease(e_rls);

    PyObjC_INITDONE();
}
