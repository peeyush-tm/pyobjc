#include "pyobjc.h"
#import "OC_PythonDate.h"

@implementation OC_PythonDate

+ (instancetype)dateWithPythonObject:(PyObject*)v
{
    OC_PythonDate* res;

    res = [[OC_PythonDate alloc] initWithPythonObject:v];
    return [res autorelease];
}

- (id)initWithPythonObject:(PyObject*)v
{
    self = [super init];
    if (unlikely(self == nil)) return nil;

    oc_value = nil;

    SET_FIELD_INCREF(value, v);
    return self;
}

-(PyObject*)__pyobjc_PythonObject__
{
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
    /* See comment in OC_PythonUnicode */
    PyObjC_BEGIN_WITH_GIL
        [super release];

    PyObjC_END_WITH_GIL
}

-(void)dealloc
{
    [oc_value  release];
    oc_value = nil;

    PyObjC_BEGIN_WITH_GIL
        PyObjC_UnregisterObjCProxy(value, self);
        Py_XDECREF(value);

    PyObjC_END_WITH_GIL

    [super dealloc];
}


- (void)encodeWithCoder:(NSCoder*)coder
{
    PyObjC_encodeWithCoder(value, coder);
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
    value = NULL;

    if (PyObjC_Decoder != NULL) {
        PyObjC_BEGIN_WITH_GIL
            PyObject* cdr = PyObjC_IdToPython(coder);
            if (cdr == NULL) {
                PyObjC_GIL_FORWARD_EXC();
            }

            PyObject* setValue;
            PyObject* selfAsPython = PyObjCObject_New(self, 0, YES);
            setValue = PyObject_GetAttrString(selfAsPython, "pyobjcSetValue_");

            PyObject* v = PyObject_CallFunction(PyObjC_Decoder, "OO", cdr, setValue);
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

-(NSDate*)_make_oc_value
{
    if (oc_value == nil) {
        PyObjC_BEGIN_WITH_GIL
            PyObject* v;

            v = PyObject_CallMethod(value, "strftime", "s",
                "%Y-%m-%d %H:%M:%S %z");
            if (v == NULL) {
                /* Raise ObjC exception */
                PyObjC_GIL_FORWARD_EXC();
            }


            oc_value = [NSDate dateWithString: PyObjC_PythonToId(v)];
            [oc_value retain];
            Py_DECREF(v);

            if (oc_value == nil) {
                /* The first try will fail when the date/datetime object
                 * isn't timezone aware, try again with a default timezone
                 */
                char buf[128];

                NSTimeZone* zone = [NSTimeZone defaultTimeZone];
                NSInteger offset = [zone secondsFromGMT];
                char posneg;
                if (offset < 0) {
                    posneg = '-';
                    offset = -offset;
                } else {
                    posneg = '+';
                }
                offset = offset / 60; /* Seconds to minutes */

                NSInteger minutes = offset % 60;
                NSInteger hours = offset / 60;



                snprintf(buf, sizeof(buf), "%%Y-%%m-%%d %%H:%%M:%%S %c%02ld%02ld",
                    posneg, (long)hours, (long)minutes);
                v = PyObject_CallMethod(value, "strftime", "s", buf);
                if (v == NULL) {
                    /* Raise ObjC exception */
                }

                oc_value = [NSDate dateWithString: PyObjC_PythonToId(v)];
                [oc_value retain];
                Py_DECREF(v);
            }

        PyObjC_END_WITH_GIL
    }
    return oc_value;
}

-(NSTimeInterval)timeIntervalSinceReferenceDate
{
    return [[self _make_oc_value] timeIntervalSinceReferenceDate];
}


#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"

- (id)addTimeInterval:(NSTimeInterval)seconds
{
    return [[self _make_oc_value] addTimeInterval:seconds];
}

#pragma clang diagnostic pop

- (NSComparisonResult)compare:(NSDate *)anotherDate
{
    return [[self _make_oc_value] compare:anotherDate];
}

- (NSCalendarDate *)dateWithCalendarFormat:(NSString *)formatString timeZone:(NSTimeZone *)timeZone
{
    return [[self _make_oc_value] dateWithCalendarFormat:formatString timeZone:timeZone];
}

- (NSString*)description
{
    return [[self _make_oc_value] description];
}

- (NSString *)descriptionWithCalendarFormat:(NSString *)formatString timeZone:(NSTimeZone *)aTimeZone locale:(id)localeDictionary
{
    return [[self _make_oc_value] descriptionWithCalendarFormat:formatString timeZone:aTimeZone locale:localeDictionary];
}

- (NSString *)descriptionWithLocale:(id)localeDictionary
{
    return [[self _make_oc_value] descriptionWithLocale:localeDictionary];
}

- (NSDate *)earlierDate:(NSDate *)anotherDate
{
    if ([[self _make_oc_value] earlierDate:anotherDate] == self) {
        return self;
    } else {
        return anotherDate;
    }
}


- (BOOL)isEqualToDate:(NSDate *)anotherDate
{
    return [[self _make_oc_value] isEqualToDate:anotherDate];
}


- (NSDate *)laterDate:(NSDate *)anotherDate
{
    if ([[self _make_oc_value] laterDate:anotherDate] == self) {
        return self;
    } else {
        return anotherDate;
    }
}

- (NSTimeInterval)timeIntervalSince1970
{
    return [[self _make_oc_value] timeIntervalSince1970];
}

- (NSTimeInterval)timeIntervalSinceDate:(NSDate *)anotherDate
{
    return [[self _make_oc_value] timeIntervalSinceDate:anotherDate];
}

- (NSTimeInterval)timeIntervalSinceNow
{
    return [[self _make_oc_value] timeIntervalSinceNow];
}


@end /* implementation OC_PythonDate */
