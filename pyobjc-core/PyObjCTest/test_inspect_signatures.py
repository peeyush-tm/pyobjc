from PyObjCTools.TestSupport import *
import objc
import types
import inspect

class TestInspectSignatures (TestCase):

    @min_python_release("3.4")
    def test_module_functions_signature(self):
        for nm in dir(objc):
            obj = getattr(objc, nm)
            if isinstance(obj, types.BuiltinMethodType):
                try:
                    value = inspect.signature(obj)

                except ValueError:
                    value = None

                if value is None:
                    self.fail("No inspect.signature for %s"%(nm,))

    @min_python_release("3.4")
    def test_class_signature(self):
        class_list = [objc.ObjCPointer, objc.objc_meta_class, objc.objc_class,
            objc.objc_object, objc.pyobjc_unicode, objc.selector, objc.FSRef,
            objc.FSSpec, objc.ivar, objc.informal_protocol, objc.formal_protocol,
            objc.varlist, objc.function, objc.IMP, objc.super]
        if hasattr(objc, 'WeakRef'):
            class_list.append(objc.WeakRef)
        for cls in class_list:
            for nm in dir(cls):
                if nm in ('__new__', '__subclasshook__', '__abstractmethods__', '__prepare__'):
                    continue
                obj = getattr(cls, nm)
                if isinstance(obj, types.BuiltinMethodType):
                    try:
                        value = inspect.signature(obj)
                    except ValueError:
                        value = None

                    if value is None:
                        self.fail("No inspect.signature for %s.%s"%(cls.__name__, nm,))

if __name__ == "__main__":
    main()
