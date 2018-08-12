from distutils.core import setup

setup(
   name='py2nb',
   version='0.5',
   description='Conversion between python and jupyter notebook',
   author='Bjørn Ådlandsvik',
   author_email='bjorn@imr.no',
   packages=['py2nb'],
   scripts=['scripts/py2nb', 'scripts/nb2py'],
   requires=['nbformat', 'nbconvert']
)
