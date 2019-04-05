from setuptools import setup

setup(
   name='City Traffic Simulation',
   version='1.0',
   description='This is a simulation of city traffic',
   author='Huy Vuong',
   author_email='huynguyenvuong99@gmail.com',
   packages=['Simulation'],  #same as name
   install_requires=['numpy', 'PyQt5'], #external packages as dependencies
)