import os
import pathlib
import shutil
import sys

from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext


class DubExtension(Extension):

    def __init__(self, name):
        # don't invoke the original build_ext for this special extension
        super().__init__(name, [])
        # self.source_dir = pathlib.Path(source_dir).resolve()


class DubBuildExt(build_ext):

    def run(self):
        print("Usage:")
        for ext in self.extensions:
            self.build_dub(ext)
        super().run()

    def build_dub(self, ext):
        cwd = pathlib.Path().absolute()
        print(cwd)
        extdir_real = pathlib.Path(ext.name)
        extdir = pathlib.Path(self.get_ext_fullpath(ext.name))
        extdir.parent.mkdir(parents=True, exist_ok=True)

        os.chdir(extdir_real) # ext.source_dir)
        major, minor = sys.version_info[:2]
        minor = minor if minor <= 11 else 11
        self.spawn(['dub', "build", "-c", f"python{major}{minor}" , "-b", "release"])
        print(extdir)
        os.chdir(str(cwd))
        shutil.copyfile(extdir_real / "libpyprovision.so", extdir)


setup(
    name='pyprovision',
    version='0.0.1',
#    packages=['pyprovision'],
    ext_modules=[DubExtension('pyprovision', ["pyprovision"])],
    cmdclass={
        'build_ext': DubBuildExt,
    }
)
