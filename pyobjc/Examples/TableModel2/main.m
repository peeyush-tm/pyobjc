#import <Python.h>
#import <Foundation/Foundation.h>
#import <sys/param.h>

int pyobjc_main(int argc, const char *argv[])
{
    NSAutoreleasePool *pool = [[NSAutoreleasePool alloc] init];
    NSString *pythonBinPath = [[NSUserDefaults standardUserDefaults] stringForKey: @"PythonBinPath"];

    pythonBinPath = pythonBinPath ? pythonBinPath : @"/usr/bin/python";
    [pythonBinPath retain];
    Py_SetProgramName((char *)[pythonBinPath cString]); 
    Py_Initialize();

    NSString *mainPyFile = [[[NSBundle mainBundle] infoDictionary] objectForKey: @"PrincipalPythonFile"];
    NSString *mainPyPath = nil;

    if (mainPyFile)
        mainPyPath = [[NSBundle mainBundle] pathForResource: mainPyFile ofType: nil];

    if ( !mainPyPath ) {
        NSLog(@"*** WARNING *** PrincipalPythonFile key either did not exist in Info.plist or the file it referred to did not exist.  Trying 'Main.py'.");
        mainPyPath = [[NSBundle mainBundle] pathForResource: @"Main.py" ofType: nil];
    }

    if ( !mainPyPath )
        [NSException raise: NSInternalInconsistencyException
                    format: @"%s:%d pyobjc_main() Failed to find main python entry point for application.  Exiting.", __FILE__, __LINE__];
    [mainPyPath retain];

    FILE *mainPy = fopen([mainPyPath cString], "r");
    int result = PyRun_SimpleFile(mainPy, (char *)[[mainPyPath lastPathComponent] cString]);

    if ( result != 0 )
        [NSException raise: NSInternalInconsistencyException
                    format: @"%s:%d pyobjc_main() Failed to run the python file at '%@'.", __FILE__, __LINE__, mainPyPath];
    
    [pool release];

    return NSApplicationMain(argc, argv);
}

int main(int argc, const char *argv[])
{
    return pyobjc_main(argc, argv);
}
