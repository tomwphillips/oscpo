try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name='oscpo',
      version=0.1,
      author='Tom Phillips',
      author_email='me@tomwphillips.co.uk',
      url='https://github.com/tomwphillips/oscpo',
      py_modules=['oscpo'],
      description='A little interface to the OS Code-Point Open database',
      license='MIT'
      )
