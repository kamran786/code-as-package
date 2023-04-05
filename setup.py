from setuptools import setup, find_packages


with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='my_code_as_package',
    version='0.4',
    description='My awesome package',
    author='Kamran Ahmad',
    author_email='kahmad595@gmail.com',
    packages=find_packages(),
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'my_code_as_pkg=src.__main__:__main__'
        ]
    },
)
