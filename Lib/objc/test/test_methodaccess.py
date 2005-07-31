import unittest
import objc
import sys

NSObject = objc.lookUpClass('NSObject')
_NSZombie = objc.lookUpClass('_NSZombie')
NSProxy = objc.lookUpClass('NSProxy')



class MethodAccessTest (unittest.TestCase):

    def testObjCObject(self):
        # Trying to access the methods of objc.objc_object should not
        # crash the interpreter.
        self.assertRaises(AttributeError, getattr, objc.objc_object.pyobjc_classMethods, 'func_code')
        self.assertRaises(AttributeError, getattr, objc.objc_object.pyobjc_instanceMethods, 'func_code')

    def testNSProxyStuff(self):
        # NSProxy is incompatitble with pyobjc_{class,instance}Methods, but
        # this should not crash the interpreter
        self.assertRaises(AttributeError, getattr, NSProxy.pyobjc_instanceMethods, 'foobar')
        self.assertRaises(AttributeError, getattr, NSProxy.pyobjc_classMethods, 'foobar')
        self.assertRaises(AttributeError, getattr, NSProxy, 'foobar')

    if sys.platform == 'darwin':
        def testNSZombie(self):
            self.assertRaises(AttributeError, getattr, _NSZombie.pyobjc_instanceMethods, "foobar")
            self.assertRaises(AttributeError, getattr, _NSZombie.pyobjc_classMethods, "foobar")
            self.assertRaises(AttributeError, getattr, _NSZombie, "foobar")


    def testDir(self):
        o = NSObject.new()

        d = dir(o.pyobjc_instanceMethods)
        self.assert_(len(d) > 10)
        self.assert_("init" in d)

        d = dir(NSObject.pyobjc_classMethods)
        self.assert_(len(d) > 10)
        self.assert_("alloc" in d)

        d = dir(NSObject.pyobjc_instanceMethods)
        self.assert_(len(d) > 10)
        self.assert_("init" in d)

    def testDict(self):
        o = NSObject.new()

        d = o.pyobjc_instanceMethods.__dict__.keys()
        self.assert_(len(d) > 10)
        self.assert_("init" in d)

        d = NSObject.pyobjc_classMethods.__dict__.keys()
        self.assert_(len(d) > 10)
        self.assert_("alloc" in d)

        d = NSObject.pyobjc_instanceMethods.__dict__.keys()
        self.assert_(len(d) > 10)
        self.assert_("init" in d)

        # XXX: We'd like 'd' to be immutable, but that would break
        # ``__builtin__.dir``, see the source for more information.

    def testAttributes(self):
        o = NSObject.new()

        self.assert_(hasattr(o.pyobjc_instanceMethods, "init"))

        self.assert_(not hasattr(o, 'pyobjc_classMethods'))

        m = o.pyobjc_instanceMethods.init
        self.assert_(isinstance(m, objc.selector))
        self.assert_(m.im_self is o)
        self.assert_(not m.isClassMethod)
        self.assert_(m.definingClass is NSObject)

        self.assert_(hasattr(NSObject.pyobjc_classMethods, "alloc"))
        m = NSObject.pyobjc_classMethods.alloc
        self.assert_(isinstance(m, objc.selector))
        self.assert_(m.im_self is NSObject)
        self.assert_(m.definingClass is type(NSObject))
        self.assert_(m.isClassMethod)


class ClassAndInstanceMethods(unittest.TestCase):
    def testClassThroughInstance(self):
        # Class methods are not accessible through instances.
        self.assertRaises(AttributeError, getattr, NSObject.new(), 'alloc')

if __name__ == "__main__":
    unittest.main()
