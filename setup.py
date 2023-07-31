from setuptools import setup, find_packages

setup(
    name='bookdir',
    version='1.0.0',
    url='https://github.com/Mkbonner/bookRepository/tree/main/bookdir',
    author='Matthew Bonner',
    author_email='fake_email@hotmail.com',
    description='Describes fans of books for class',
    packages=find_packages(),    
    install_requires=['numpy >= 1.11.1', 'pandas >= 1.1'],
)
