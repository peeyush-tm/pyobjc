__all__ = ['FFI_CFLAGS', 'FFI_SOURCE']
from srcpath import srcpath
def ffipath(*args):
    return srcpath('libffi-src', *args)

FFI_CFLAGS=['-I' + ffipath('include')]

# The list below includes the source files for all CPU types that we run on
# this makes it easier to build fat binaries on Mac OS X.
FFI_SOURCE=map(ffipath, [
    "src/types.c",
    "src/prep_cif.c",
    "src/x86/ffi_darwin.c",
    "src/x86/darwin.S",
    "src/powerpc/ffi_darwin.c",
    "src/powerpc/darwin.S",
    "src/powerpc/darwin_closure.S",
])

# Patch distutils: it needs to compile .S files as well.
from distutils.unixccompiler import UnixCCompiler
UnixCCompiler.src_extensions.append('.S')
del UnixCCompiler
