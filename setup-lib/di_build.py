import os
from setuptools import Distribution

build = Distribution().get_command_class("build")

class pyobjc_build(build):

    def initialize_options(self):
        build.initialize_options(self)
        self.build_base = os.path.join(
            self.build_base, self.distribution.get_name())

cmdclass = dict(build=pyobjc_build)
