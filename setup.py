from setuptools import setup

setup(
    name = 'fortune-cookie',
    version = '0.1.0',
    packages = ['cli'],
    entry_points = {
        'console_scripts': [
            'fortune-cookie = cli.__main__:main'
        ]
    })