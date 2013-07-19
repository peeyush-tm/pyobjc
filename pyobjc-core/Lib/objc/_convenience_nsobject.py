"""
Generic conveniences for NSObject

The type is defined in Foundation, but NSObject is important
to the behavior of the bridge and therefore these conveniences
are kept in the core.
"""

__all__ = ()
import sys
from objc._convenience import addConvenienceForClass

if sys.version_info[0] == 2:  # pragma: no 3.x cover
    STR_TYPES=(str, unicode)
else:
    STR_TYPES=str


def nsobject_hash(self, _max=sys.maxsize, _const=((sys.maxsize + 1) * 2)):
    rval = self.hash()
    if rval > _max:
        rval -= _const
        # -1 is not a valid hash in Python and hash(x) will
        # translate a hash of -1 to -2, so we might as well
        # do it here so that it's not too surprising..
        if rval == -1:
            rval = -2
    return int(rval)

def nsobject__eq__(self, other):
    return bool(self.isEqualTo_(other))

def nsobject__ne__(self, other):
    return bool(self.isNotEqualTo_(other))

def nsobject__gt__(self, other):
    return bool(self.isGreaterThan_(other))

def nsobject__ge__(self, other):
    return bool(self.isGreaterThanOrEqualTo_(other))

def nsobject__lt__(self, other):
    return bool(self.isLessThan_(other))

def nsobject__le__(self, other):
    return bool(self.isLessThanOrEqualTo_(other))

class kvc (object):
    """
    Key-Value-Coding accessor for Cocoa objects.

    Both attribute access and dict-like indexing will attempt to
    access the requested item through Key-Value-Coding.
    """
    __slots__ = ('__object',)
    def __init__(self, value):
        self.__object = value

    def __repr__(self):
        return "<KVC accessor for %r>"%(self.__object,)

    def __getattr__(self, key):
        try:
            return self.__object.valueForKey_(key)
        except KeyError as msg:
            if (hasattr(msg, '_pyobjc_info_')
                    and msg._pyobjc_info_['name'] == 'NSUnknownKeyException'):
                raise AttributeError(key)

            raise

    def __setattr__(self, key, value):
        if not key.startswith('_'):
            return self.__object.setValue_forKey_(value, key)
        else:
            super(kvc, self).__setattr__(key, value)

    def __getitem__(self, key):
        if not isinstance(key, STR_TYPES):
            raise TypeError("Key must be string")

        return self.__object.valueForKey_(key)

    def __setitem__(self, key, value):
        if not isinstance(key, STR_TYPES):
            raise TypeError("Key must be string")

        return self.__object.setValue_forKey_(value, key)


addConvenienceForClass("NSObject", (
    ('__hash__', nsobject_hash),
    ('__eq__', nsobject__eq__),
    ('__ne__', nsobject__ne__),
    ('__gt__', nsobject__gt__),
    ('__ge__', nsobject__ge__),
    ('__lt__', nsobject__lt__),
    ('__le__', nsobject__le__),
    ('_',   property(kvc)),
))

if sys.version_info[0] == 2:  # pragma: no 3.x cover
    def nsobject__cmp__(self, other):
        try:
            func = self.compare_

        except AttributeError:
            return NotImplemented
            if self < other:
                return -1
            elif self > other:
                return 1
            else:
                return 0

        else:
            return func(other)

    addConvenienceForClass("NSObject", (
        ("__cmp__", nsobject__cmp__),
    ))
