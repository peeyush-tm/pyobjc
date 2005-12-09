"""
Custom 'sdist' action for setup.py
"""

# distutils doesn't know about subversion and I'm to lazy to reverse engineer
# distutils in the hope of detecting how to specify that all svn directories
# should be removed.
from setuptools import Distribution
sdist_base = Distribution().get_command_class("sdist")

class sdist (sdist_base):

    def run(self):
        self.run_command('build_html')
        sdist_base.run(self)

cmdclass = dict(sdist=sdist)
