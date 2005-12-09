from setuptools import setup

plist = dict(NSMainNibFile='ClassBrowser')
setup(
    plugin = ["InjectBrowserPlugin.py"],
    data_files = ["ClassBrowser.nib"],
    options = dict(py2app=dict(plist=plist)),
    setup_requires=["py2app"],
    install_requires=["pyobjc"],
)
