from setuptools import setup

plist = dict(NSMainNibFile='PyInterpreter')
setup(
    plugin = ["InjectInterpreterPlugin.py"],
    data_files = ["PyInterpreter.nib"],
    options = dict(py2app=dict(plist=plist)),
    setup_requires=["py2app"],
    install_requires=["pyobjc"],
)
