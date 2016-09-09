from distutils.core import setup
from cx_Freeze import setup, Executable

setup(
    name='clipboard',
    version='0.1',
    url='',
    license='',
    author='vmaksimenko',
    author_email='',
    description='',
    executables=[Executable("main.py")],
    requires=[
        'pyrebase',
        'pyperclip'
    ]
)
