
print('test import worked1')

from setuptools import setup

print('test import worked2')

setup(
   name='test_python_imports',
   version='1.0',
   description='A useful module',
   author='billfreeman44',
   author_email='foomail@foo.com',
   packages=['test_python_imports']
)

print('test import worked3')
