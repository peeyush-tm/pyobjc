import sys, os

def somefunc():
    print "Hello from py2app"

    print "frozen", repr(getattr(sys, "frozen", None))

    import __main__
    print __main__.__file__
    print "sys.path", sys.path
    print "sys.executable", sys.executable
    print "sys.prefix", sys.prefix
    print "sys.argv", sys.argv
    print "os.getcwd()", os.getcwd()

if __name__ == '__main__':
    somefunc()
