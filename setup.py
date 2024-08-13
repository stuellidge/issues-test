from setuptools import find_packages, setup

# Get the version from drode/version.py without importing the package
exec(compile(open('cli/version.py').read(),
             'cli/version.py', 'exec'))

setup(
    name='cli',
    version=__version__, # noqa: F821
    description='A test project for investigating issue resolution',
    author='Stuart Ellidge',
    author_email='anon@example.com',
    license='GPLv3',
    long_description=open('README.md').read(),
    packages=find_packages(exclude=('tests',)),
    package_data={'cli': [
        'migrations/*',
        'migrations/versions/*',
    ]},
    entry_points={'console_scripts': ['cli = cli:main']},
    install_requires=[
    ]
)

