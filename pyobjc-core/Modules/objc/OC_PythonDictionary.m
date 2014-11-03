/*
 * NOTE: the implementation uses PyDict_* APIs whenever possible and falls
 * back to the generic PyObject_* APIs otherwise. We don't use the PyMapping_*
 * APIs because those are incomplete(!).
 */
#include "pyobjc.h"
#import "OC_PythonDictionary.h"

/*
 * OC_PythonDictionaryEnumerator - Enumerator for Python dictionaries
 *
 * This class implements an NSEnumerator for proxied Python dictionaries.
 */
@interface OC_PythonDictionaryEnumerator : NSEnumerator
{
    OC_PythonDictionary* value;
    Py_ssize_t pos;
    BOOL valid;
}
+(instancetype)enumeratorWithWrappedDictionary:(OC_PythonDictionary*)value;
-(id)initWithWrappedDictionary:(OC_PythonDictionary*)value;
-(void)dealloc;
-(id)nextObject;

@end /* interface OC_PythonDictionaryEnumerator */


@implementation OC_PythonDictionaryEnumerator

+(instancetype)enumeratorWithWrappedDictionary:(OC_PythonDictionary*)v
{
    return [[[self alloc] initWithWrappedDictionary:v] autorelease];
}

-(id)initWithWrappedDictionary:(OC_PythonDictionary*)v
{
    self = [super init];
    if (unlikely(self == nil)) return nil;

    value = [v retain];
    valid = YES;
    pos = 0;
    return self;
}

-(void)dealloc
{
    [value release];
    [super dealloc];
}

-(id)nextObject
{
    id key = nil;
    PyObject* pykey = NULL;

    PyObjC_BEGIN_WITH_GIL
        PyObject* dct = [value __pyobjc_PythonObject__];
        if (unlikely(!PyDict_Next(dct, &pos, &pykey, NULL))) {
            key = nil;

        } else if (pykey == Py_None) {
            key = [NSNull null];

        } else {
            if (depythonify_c_value(@encode(id), pykey, &key) == -1) {
                Py_DECREF(dct);
                PyObjC_GIL_FORWARD_EXC();
            }
        }
        Py_DECREF(dct);

    PyObjC_END_WITH_GIL

    valid = (key != nil) ? YES : NO;

    return key;
}

@end // implementation OC_PythonDictionaryEnumerator


@implementation OC_PythonDictionary

+(OC_PythonDictionary*)dictionaryWithPythonObject:(PyObject*)v
{
    OC_PythonDictionary* res = [[OC_PythonDictionary alloc] initWithPythonObject:v];
    [res autorelease];
    return res;
}

-(OC_PythonDictionary*)initWithPythonObject:(PyObject*)v
{
    self = [super init];
    if (unlikely(self == nil)) return nil;

    SET_FIELD_INCREF(value, v);
    return self;
}

-(BOOL)supportsWeakPointers {
    return YES;
}

-(oneway void)release
{
    /* See comment in OC_PythonUnicode */
    PyObjC_BEGIN_WITH_GIL
        [super release];

    PyObjC_END_WITH_GIL
}

-(void)dealloc
{
    PyObjC_BEGIN_WITH_GIL
        PyObjC_UnregisterObjCProxy(value, self);
        Py_CLEAR(value);

    PyObjC_END_WITH_GIL

    [super dealloc];
}

-(PyObject*)__pyobjc_PythonObject__
{
    Py_XINCREF(value);
    return value;
}

-(PyObject*)__pyobjc_PythonTransient__:(int*)cookie
{
    *cookie = 0;
    Py_XINCREF(value);
    return value;
}

-(NSUInteger)count
{
    Py_ssize_t result;
    if (value == NULL) {
        return 0;
    }

    PyObjC_BEGIN_WITH_GIL
        if (likely(PyDict_CheckExact(value))) {
            result = PyDict_Size(value);

        } else {
            result = PyObject_Length(value);
        }

    PyObjC_END_WITH_GIL

    if (sizeof(Py_ssize_t) > sizeof(NSUInteger)) {
        if (result > (Py_ssize_t)NSUIntegerMax) {
            return NSUIntegerMax;
        }
    }

    return result;
}

-(id)objectForKey:key
{
    PyObject* v;
    PyObject* k;
    id result;

    if (value == NULL) {
        return nil;
    }

    PyObjC_BEGIN_WITH_GIL

        if (unlikely(key == [NSNull null])) {
            Py_INCREF(Py_None);
            k = Py_None;

        } else {
            k = PyObjC_IdToPython(key);
            if (k == NULL) {
                    PyObjC_GIL_FORWARD_EXC();
            }
        }

        if (likely(PyDict_CheckExact(value))) {
            v = PyDict_GetItem(value, k);
            Py_XINCREF(v);

        } else {
            v = PyObject_GetItem(value, k);
        }

        Py_DECREF(k);

        if (unlikely(v == NULL)) {
            PyErr_Clear();
            PyObjC_GIL_RETURN(nil);
        }

        if (v == Py_None) {
            result = [NSNull null];

        } else if (unlikely(depythonify_c_value(@encode(id), v, &result) == -1)) {
            Py_DECREF(v);
            PyObjC_GIL_FORWARD_EXC();
        }
        Py_DECREF(v);

    PyObjC_END_WITH_GIL

    return result;
}


-(void)setObject:val forKey:key
{
    PyObject* v = NULL;
    PyObject* k = NULL;
    id null = [NSNull null];

    PyObjC_BEGIN_WITH_GIL
        if (unlikely(val == null)) {
            Py_INCREF(Py_None);
            v = Py_None;

        } else {
            v = PyObjC_IdToPython(val);
            if (unlikely(v == NULL)) {
                PyObjC_GIL_FORWARD_EXC();
            }
        }

        if (unlikely(key == nil)) {
            Py_INCREF(Py_None);
            k = Py_None;

        } else {
            k = PyObjC_IdToPython(key);
            if (k == NULL) {
                Py_XDECREF(v);
                PyObjC_GIL_FORWARD_EXC();
            }
        }

        if (likely(PyDict_CheckExact(value))) {
            if (unlikely(PyDict_SetItem(value, k, v) < 0)) {
                Py_XDECREF(v);
                Py_XDECREF(k);
                PyObjC_GIL_FORWARD_EXC();
            }

        } else {
            if (unlikely(PyObject_SetItem(value, k, v) < 0)) {
                Py_XDECREF(v);
                Py_XDECREF(k);
                PyObjC_GIL_FORWARD_EXC();
            }
        }

        Py_DECREF(v);
        Py_DECREF(k);

    PyObjC_END_WITH_GIL
}


-(void)removeObjectForKey:key
{
    PyObject* k;

    PyObjC_BEGIN_WITH_GIL
        if (unlikely(key == [NSNull null])) {
            Py_INCREF(Py_None);
            k = Py_None;

        } else {
            k = PyObjC_IdToPython(key);
            if (unlikely(k == NULL)) {
                PyObjC_GIL_FORWARD_EXC();
            }
        }

        if (PyDict_CheckExact(value)) {
            if (unlikely(PyDict_DelItem(value, k) < 0)) {
                Py_DECREF(k);
                PyObjC_GIL_FORWARD_EXC();
            }

        } else {
            if (unlikely(PyObject_DelItem(value, k) < 0)) {
                Py_DECREF(k);
                PyObjC_GIL_FORWARD_EXC();
            }
        }
        Py_DECREF(k);

    PyObjC_END_WITH_GIL
}

-(NSEnumerator *)keyEnumerator
{
    if (value == NULL) {
            return nil;
    }

    if (PyDict_CheckExact(value)) {
        return [OC_PythonDictionaryEnumerator enumeratorWithWrappedDictionary:self];

    } else {
        PyObjC_BEGIN_WITH_GIL
            PyObject* keys = PyObject_CallMethod(value, "keys", NULL);
            if (keys == NULL) {
                PyObjC_GIL_FORWARD_EXC();
            }

            PyObject* iter = PyObject_GetIter(keys);
            Py_DECREF(keys);
            if (iter == NULL) {
                PyObjC_GIL_FORWARD_EXC();
            }

            NSEnumerator* result = [OC_PythonEnumerator enumeratorWithPythonObject:iter];
            PyObjC_GIL_RETURN(result);

        PyObjC_END_WITH_GIL
    }
}


- (id)initWithObjects:(const id[])objects
      forKeys:(const id <NSCopying>[])keys
        count:(NSUInteger)count
{
    /* This implementation is needed for our support for the NSCoding
     * protocol, NSDictionary's initWithCoder: will call this method.
     */
    NSUInteger i;

    PyObjC_BEGIN_WITH_GIL
        for  (i = 0; i < count; i++) {
            PyObject* k;
            PyObject* v;
            int r;

            if (objects[i] == [NSNull null]) {
                v = Py_None;
                Py_INCREF(Py_None);

            } else {
                v = PyObjC_IdToPython(objects[i]);
                if (v == NULL) {
                    PyObjC_GIL_FORWARD_EXC();
                }
            }

            if (keys[i] == [NSNull null]) {
                k = Py_None;
                Py_INCREF(Py_None);

            } else {
                k = PyObjC_IdToPython(keys[i]);
                if (k == NULL) {
                    PyObjC_GIL_FORWARD_EXC();
                }
#if PY_MAJOR_VERSION == 3
                if (PyObjCUnicode_Check(k)) {
                    PyObject* k2 = PyObject_Str(k);
                    if (k2 == NULL) {
                        Py_DECREF(k);
                        PyObjC_GIL_FORWARD_EXC();
                    }
                    PyUnicode_InternInPlace(&k2);
                    Py_DECREF(k);
                    k = k2;
                }
#endif
            }

            r = PyDict_SetItem(value, k, v);
            Py_DECREF(k); Py_DECREF(v);

            if (r == -1) {
                PyObjC_GIL_FORWARD_EXC();
            }
        }
    PyObjC_END_WITH_GIL
    return self;
}

/*
 * Helper method for initWithCoder, needed to deal with
 * recursive objects (e.g. o.value = o)
 */
-(void)pyobjcSetValue:(NSObject*)other
{
    PyObjC_BEGIN_WITH_GIL
        PyObject* v = PyObjC_IdToPython(other);

        SET_FIELD(value, v);
    PyObjC_END_WITH_GIL
}

- (id)initWithCoder:(NSCoder*)coder
{
    int code;
    if ([coder allowsKeyedCoding]) {
        code = [coder decodeInt32ForKey:@"pytype"];
    } else {
        [coder decodeValueOfObjCType:@encode(int) at:&code];
    }

    switch (code) {
    case 1:
        PyObjC_BEGIN_WITH_GIL
            value = PyDict_New();
            if (value == NULL) {
                PyObjC_GIL_FORWARD_EXC();
            }

        PyObjC_END_WITH_GIL

        self = [super initWithCoder:coder];
        return self;

    case 2:
        if (PyObjC_Decoder != NULL) {
            PyObjC_BEGIN_WITH_GIL
                PyObject* cdr = PyObjC_IdToPython(coder);
                PyObject* setValue;
                PyObject* selfAsPython;
                PyObject* v;

                if (cdr == NULL) {
                    PyObjC_GIL_FORWARD_EXC();
                }

                selfAsPython = PyObjCObject_New(self, 0, YES);
                setValue = PyObject_GetAttrString(selfAsPython, "pyobjcSetValue_");

                v = PyObject_CallFunction(PyObjC_Decoder, "OO", cdr, setValue);
                Py_DECREF(cdr);
                Py_DECREF(setValue);
                Py_DECREF(selfAsPython);

                if (v == NULL) {
                    PyObjC_GIL_FORWARD_EXC();
                }

                SET_FIELD(value, v);

                self = PyObjC_FindOrRegisterObjCProxy(value, self);
            PyObjC_END_WITH_GIL

            return self;

        } else {
            [NSException raise:NSInvalidArgumentException
                        format:@"decoding Python objects is not supported"];
            return nil;

        }
    }
    [NSException raise:NSInvalidArgumentException
                    format:@"decoding Python objects is not supported"];
    [self release];
    return nil;
}

-(Class)classForCoder
{
    if (PyDict_CheckExact(value)) {
        return [NSMutableDictionary class];
    } else {
        return [OC_PythonDictionary class];
    }
}

-(Class)classForKeyedArchiver
{
    return [OC_PythonDictionary class];
}

+(NSArray*)classFallbacksForKeyedArchiver
{
    return [NSArray arrayWithObject:@"NSDictionary"];
}

- (void)encodeWithCoder:(NSCoder*)coder
{
    if (PyDict_CheckExact(value)) {
        if ([coder allowsKeyedCoding]) {
            [coder encodeInt32:1 forKey:@"pytype"];

        }
        [super encodeWithCoder:coder];

    } else {
        if ([coder allowsKeyedCoding]) {
            [coder encodeInt32:2 forKey:@"pytype"];

        } else {
            int v = 2;
            [coder encodeValueOfObjCType:@encode(int) at:&v];
        }
        PyObjC_encodeWithCoder(value, coder);

    }
}

-(id)copyWithZone:(NSZone*)zone
{
    if (PyObjC_CopyFunc) {
        NSObject* result;

        PyObjC_BEGIN_WITH_GIL
            PyObject* copy = PyObject_CallFunctionObjArgs(PyObjC_CopyFunc, value, NULL);
            if (copy == NULL) {
                PyObjC_GIL_FORWARD_EXC();
            }

            result = PyObjC_PythonToId(copy);
            Py_DECREF(copy);

            if (PyErr_Occurred()) {
                PyObjC_GIL_FORWARD_EXC();
            }

            [result retain];
        PyObjC_END_WITH_GIL

        return result;

    } else {
            return [super copyWithZone:zone];
    }
}

-(id)mutableCopyWithZone:(NSZone*)zone
{
    if (PyObjC_CopyFunc) {
        NSObject* result;

        PyObjC_BEGIN_WITH_GIL
            PyObject* copy = PyDict_New();
            if (copy == NULL) {
                PyObjC_GIL_FORWARD_EXC();
            }

            int r = PyDict_Update(copy, value);
            if (r == -1) {
                PyObjC_GIL_FORWARD_EXC();
            }

            result = PyObjC_PythonToId(copy);
            Py_DECREF(copy);

            if (PyErr_Occurred()) {
                PyObjC_GIL_FORWARD_EXC();
            }

            [result retain];

            PyObjC_END_WITH_GIL

        return result;

    } else {
            return [super mutableCopyWithZone:zone];
    }
}

@end  // interface OC_PythonDictionary
