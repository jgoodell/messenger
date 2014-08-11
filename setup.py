import os
import shutil
from setuptools import setup

"""The setuptools setup script.

README:    The README.md text.
setup:     The setup meta.
"""

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# Move the files to a location where setuptools is not confused
try:
    os.mkdir('package')
except OSError:
    os.remove('package/models.py')
    os.remove('package/views.py')
    os.remove('package/tests.py')
    os.remove('package/__init__.py')
    os.rmdir('package')
    os.mkdir('package')

shutil.copy2('models.py', 'package/models.py')
shutil.copy2('views.py', 'package/views.py')
shutil.copy2('tests.py', 'package/tests.py')
shutil.copy2('__init__.py', 'package/__init__.py')

#os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='messenger',
    version='v0.1.0',
    packages=['package'],
    include_package_data=True,
    license='MIT License',
    description='A simple app, part of a Hudson Bay project.',
    long_description=README,
    url='',
    author='Jason Goodell',
    author_email='jason.goodell@harrison.edu',
    )
    
