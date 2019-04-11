from setuptools import setup, find_packages

setup(
    name='plouf',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        plouf=plouf.plouf:main
    ''',
)