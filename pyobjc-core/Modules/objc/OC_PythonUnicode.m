#include "pyobjc.h"
#import "OC_PythonUnicode.h"

@implementation OC_PythonUnicode

+(instancetype)unicodeWithPythonObject:(PyObject*)v
{
    OC_PythonUnicode* res;

    res = [[OC_PythonUnicode alloc] initWithPythonObject:v];
    return [res autorelease];
}

-(id)initWithPythonObject:(PyObject*)v
{
    self = [super init];
    if (unlikely(self == nil)) return nil;

    SET_FIELD_INCREF(value, v);
    return self;
}


-(PyObject*)__pyobjc_PythonObject__
{
    if (value == NULL) {
        Py_INCREF(Py_None);
        return Py_None;
    }
    Py_INCREF(value);
    return value;
}

-(PyObject*)__pyobjc_PythonTransient__:(int*)cookie
{
    *cookie = 0;
    Py_INCREF(value);
    return value;
}


-(BOOL)supportsWeakPointers {
    return YES;
}

-(oneway void)release
{
    /* There is small race condition when an object is almost deallocated
     * in one thread and fetched from the registration mapping in another
     * thread. If we don't get the GIL this object might get a -dealloc
     * message just as the other thread is fetching us from the mapping.
     * That's why we need to grab the GIL here (getting it in dealloc is
     * too late, we'd already be dead).
     */
    /* FIXME: Should switch to __weak on OSX 10.7 or later, that should
     * fix this issue without a performance penalty.
     */
    PyObjC_BEGIN_WITH_GIL
        [super release];
    PyObjC_END_WITH_GIL
}

-(void)dealloc
{
    PyObjC_BEGIN_WITH_GIL
        PyObjC_UnregisterObjCProxy(value, self);
        [realObject release];
        realObject = nil;
        Py_CLEAR(value);

#ifdef PyObjC_STR_CACHE_IMP
        imp_length = 0xDEADBEEF;
        imp_charAtIndex = 0xDEADBEEF;
        imp_getCharacters = 0xDEADBEEF;
#endif /* PyObjC_STR_CACHE_IMP */

    PyObjC_END_WITH_GIL

    [super dealloc];
}

#if PY_VERSION_HEX >= 0x03030000

-(id)__realObject__
{
#ifdef Py_DEBUG
    if (!PyUnicode_IS_READY(value)) {
            /* Object should be ready, ensure we crash with the GIL
             * held when it's not.
             */
            PyObjC_BEGIN_WITH_GIL
                PyUnicode_GET_LENGTH(value);
            PyObjC_END_WITH_GIL
    }
#endif

    if (!realObject) {
        switch (PyUnicode_KIND(value)) {
        case PyUnicode_1BYTE_KIND:
            if (PyUnicode_IS_ASCII(value)) {
                realObject = [[NSString alloc]
                    initWithBytesNoCopy:PyUnicode_1BYTE_DATA(value)
                           length:(NSUInteger)PyUnicode_GET_LENGTH(value)
                         encoding:NSASCIIStringEncoding
                     freeWhenDone:NO];
            } else {
                realObject = [[NSString alloc]
                    initWithBytesNoCopy:PyUnicode_1BYTE_DATA(value)
                           length:(NSUInteger)PyUnicode_GET_LENGTH(value)
                         encoding:NSISOLatin1StringEncoding
                     freeWhenDone:NO];

            }
            break;

        case PyUnicode_2BYTE_KIND:
            realObject = [[NSString alloc]
                initWithCharactersNoCopy:PyUnicode_2BYTE_DATA(value)
                       length:(NSUInteger)PyUnicode_GET_LENGTH(value)
                 freeWhenDone:NO];
            break;

        case PyUnicode_WCHAR_KIND:
            /* wchar_t representation, treat same
             * as UCS4 strings
             */
        case PyUnicode_4BYTE_KIND:
            PyObjC_BEGIN_WITH_GIL
                PyObject* utf8 = PyUnicode_AsUTF8String(value);
                if (!utf8) {
                    NSLog(@"failed to encode unicode string to byte string");
                    PyErr_Clear();
                } else {
                    realObject = [[NSString alloc]
                        initWithBytes:PyBytes_AS_STRING(utf8)
                               length:(NSUInteger)PyBytes_GET_SIZE(utf8)
                             encoding:NSUTF8StringEncoding];
                    Py_DECREF(utf8);
                }
            PyObjC_END_WITH_GIL
        }
    }
    return realObject;
}

#elif defined(PyObjC_UNICODE_FAST_PATH)

-(id)__realObject__
{
    if (!realObject) {
        realObject = [[NSString alloc]
            initWithCharactersNoCopy:PyUnicode_AS_UNICODE(value)
                   length:(NSUInteger)PyUnicode_GET_SIZE(value)
             freeWhenDone:NO];
    }
    return realObject;
}

#else // !PyObjC_UNICODE_FAST_PATH */

-(id)__realObject__
{
    if (!realObject) {
        PyObjC_BEGIN_WITH_GIL
            PyObject* utf8 = PyUnicode_AsUTF8String(value);
            if (!utf8) {
                NSLog(@"failed to encode unicode string to byte string");
                PyErr_Clear();
            } else {
                realObject = [[NSString alloc]
                    initWithBytes:PyBytes_AS_STRING(utf8)
                           length:(NSUInteger)PyBytes_GET_SIZE(utf8)
                         encoding:NSUTF8StringEncoding];
                Py_DECREF(utf8);
            }
        PyObjC_END_WITH_GIL
    }
    return realObject;
}
#endif

-(NSUInteger)length
{
    return [[self __realObject__] length];
}

-(unichar)characterAtIndex:(NSUInteger)anIndex
{
    return [[self __realObject__] characterAtIndex:anIndex];
}

-(void)getCharacters:(unichar *)buffer range:(NSRange)aRange
{
    return [[self __realObject__] getCharacters:buffer range:aRange];
}

-(void)getCharacters:(unichar*)buffer
{
    return [[self __realObject__] getCharacters:buffer];
}

/*
 * NSCoding support
 */
- (id)initWithCharactersNoCopy:(unichar *)characters
            length:(NSUInteger)length
          freeWhenDone:(BOOL)flag
{
    int byteorder = 0;
    PyObjC_BEGIN_WITH_GIL
        /* Decode as a UTF-16 string in native byteorder */
        value = PyUnicode_DecodeUTF16(
                (const char*)characters,
                length * 2,
                NULL,
                &byteorder);
        if (value == NULL) {
            PyObjC_GIL_FORWARD_EXC();
        }

    PyObjC_END_WITH_GIL;
    if (flag) {
        free(characters);
    }
    return self;
}

-(id)initWithBytes:(const void*)bytes length:(NSUInteger)length encoding:(NSStringEncoding)encoding
{
    char* py_encoding = NULL;
    int byteorder = 0;

    /* Detect some often used single-byte encodings that can be created in Python without
     * creating an intermediate object.
     */

    switch (encoding) {
    case NSASCIIStringEncoding: py_encoding = "ascii"; break;
    case NSUTF8StringEncoding: py_encoding = "UTF-8"; break;
    case NSISOLatin1StringEncoding: py_encoding = "latin1"; break;
    }

    if (py_encoding != NULL) {
        PyObjC_BEGIN_WITH_GIL
            value = PyUnicode_Decode(bytes, length, py_encoding, NULL);
            if (value == NULL) {
                PyObjC_GIL_FORWARD_EXC();
            }
        PyObjC_END_WITH_GIL
        return self;
    }

    /* UTF-16 encodings can also be decoded without an intermediate object */
    byteorder = 2;
    switch (encoding) {
    case NSASCIIStringEncoding: byteorder = 0; break;
    case NSUTF8StringEncoding:  byteorder = -1; break;
    case NSISOLatin1StringEncoding:  byteorder = 1; break;
    }
    if (byteorder != 2) {
        PyObjC_BEGIN_WITH_GIL
            /* Decode as a UTF-16 string in native byteorder */
            value = PyUnicode_DecodeUTF16(
                    bytes,
                    length,
                    NULL,
                    &byteorder);
            if (value == NULL) {
                PyObjC_GIL_FORWARD_EXC();
            }

        PyObjC_END_WITH_GIL;
        return self;
    }

    /* And finally: first use the Cocoa decoder to create an NSString, copy the unichars into
     * a temporary buffer and use that to create a Python unicode string using the UTF16 decoder.
     *
     * This can be slightly optimized on systems where sizeof(Py_UNICODE) == sizeof(unichar), but
     * that's not worth the additional complexity and won't work on Python 3.3 or later anyway.
     */

    NSString* tmpval = [[NSString alloc] initWithBytes:bytes length:length encoding:encoding];
    Py_ssize_t charcount = [tmpval length];

    /* NOTE: the malloc() call can be avoided when sizeof(unichar) == sizeof(Py_UNICODE) and
     * we're on python 3.2 or earlier. That's not worth the added complexity.
     */
    unichar* chars = malloc(charcount*2);

    if (chars == NULL) {
        [self release];
        return nil;
    }
    [tmpval getCharacters:chars];
    [tmpval release];

    PyObjC_BEGIN_WITH_GIL
        /* Decode as a UTF-16 string in native byteorder */
        byteorder = 0;
        value = PyUnicode_DecodeUTF16(
                (const char*)chars,
                length * 2,
                NULL,
                &byteorder);
        free(chars);
        if (value == NULL) {
            PyObjC_GIL_FORWARD_EXC();
        }

    PyObjC_END_WITH_GIL;
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

-(id)initWithCoder:(NSCoder*)coder
{
    int ver;
    if ([coder allowsKeyedCoding]) {
        ver = [coder decodeInt32ForKey:@"pytype"];
    } else {
        [coder decodeValueOfObjCType:@encode(int) at:&ver];
    }
    if (ver == 1) {
        /* Version 1: plain unicode string (not subclass).
         * emitted by some versions of PyObjC (< 2.4.1, < 2.5.1, <2.6)
         */
        self = [super initWithCoder:coder];
        return self;
    } else if (ver == 2) {

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
    } else {
        [NSException raise:NSInvalidArgumentException
            format:@"encoding Python unicode objects is not supported"];
        return nil;
    }
}

-(void)encodeWithCoder:(NSCoder*)coder
{
    int is_exact_unicode;
    PyObjC_BEGIN_WITH_GIL
        is_exact_unicode = PyUnicode_CheckExact(value);
    PyObjC_END_WITH_GIL

    if (is_exact_unicode) {
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

-(NSObject*)replacementObjectForArchiver:(NSArchiver*)archiver
{
    (void)(archiver);
    return self;
}

-(NSObject*)replacementObjectForKeyedArchiver:(NSKeyedArchiver*)archiver
{
    (void)(archiver);
    return self;
}

-(NSObject*)replacementObjectForCoder:(NSCoder*)archiver
{
    (void)(archiver);
    return self;
}

-(NSObject*)replacementObjectForPortCoder:(NSPortCoder*)archiver
{
    (void)(archiver);
    return self;
}

/*
 * Plain unicode objects (not subclasses) are archived as "real"
 * NSString objects. This means you won't get the same object type back
 * when reading them back, but does allow for better interop with code
 * that uses a non-keyed archiver.
 */
-(Class)classForCoder
{
    Class result;
    PyObjC_BEGIN_WITH_GIL
        if (PyUnicode_CheckExact(value)) {
            result = [NSString class];
        } else {
            result = [OC_PythonUnicode class];
        }
    PyObjC_END_WITH_GIL
    return result;
}

-(Class)classForKeyedArchiver
{
    return [OC_PythonUnicode class];
}


/* Ensure that we can be unarchived as a generic string by pure ObjC
 * code.
 */
+(NSArray*)classFallbacksForKeyedArchiver
{
    return [NSArray arrayWithObject:@"NSString"];
}


@end /* implementation OC_PythonUnicode */
