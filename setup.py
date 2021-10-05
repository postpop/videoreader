from setuptools import setup, find_packages
import os
import codecs
import re

here = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
    with codecs.open(os.path.join(here, *parts), 'r') as fp:
        return fp.read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


setup(
    name='videoreader',
    version=find_version("src/videoreader.py"),
    author='Jan Clemens',
    python_requires='>=3.5',
    packages=find_packages('src'),
    package_dir={'': 'src'},

    install_requires=['setuptools', 'opencv-python-headless>=3.0',],
    keywords='cv2 opencv videocapture videoreader avi',
)
