from setuptools import setup, find_packages

setup(
    name='my_code_as_package',
    version='0.1',
    description='My awesome package',
    author='Kamran Ahmad',
    author_email='kahmad595@gmail.com',
    packages=find_packages(),
    install_requires=requirements.txt,
    entry_points={
        'console_scripts': [
            'my_code_as_pkg=src.__main__.:main'
        ]
    },
)
