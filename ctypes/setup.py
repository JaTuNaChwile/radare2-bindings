from distutils.core import setup

with open('README.md') as readme_file:
    readme = readme_file.read()

setup(
    name='radare2-ctypes',
    version='0.1.0',
    license='MIT',
    description='Autogenerated CTypes Bindings for Radare2 using Valabind',
    long_description=readme,
    author='pancake',
    author_email='pancake@nopcode.org',
    url='https://rada.re',
    package_dir={'radare2-ctypes': 'radare2-ctypes'},
    packages=['radare2-ctypes']
)
