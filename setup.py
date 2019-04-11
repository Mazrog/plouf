from setuptools import setup, find_packages

setup(
    name='plouf',
    version='0.1',
    author="Mazrog",
    author_email="maxime.cabanal@outlook.fr",
    description="Little CLI tools to manage projects.",
    long_description_content_type="text/markdown",
    url="https://github.com/Mazrog/plouf",
    
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