from setuptools import setup

setup(
    name='plouf',
    version='0.1',
    py_modules=['plouf'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        plouf=plouf:main
    ''',
)