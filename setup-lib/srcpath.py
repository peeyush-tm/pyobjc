import os, sys
__all__ = ['srcpath', 'modpath', 'libpath', 'buildpath']
setupmodule = sys.modules.get('setup', sys.modules['__main__']).__file__
RELBASE = os.path.dirname(os.path.realpath(setupmodule))
SRCDIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
os.chdir(SRCDIR)
    
def srcpath(*args):
    return os.path.join(*args)

def buildpath(*args):
    return os.path.join('build', *args)

def modpath(*args):
    return srcpath('Modules', *args)

def libpath(*args):
    return srcpath('Lib', *args)
