import os
from distutils.core import setup

def read(filename):
    return open(os.path.join(os.path.dirname(__file__), filename)).read()

setup(
    name='smartcsvsorter',
    version='1.4',
    packages=['smartcsvsorter'],
    package_dir={'smartcsvsorter' : '.'},
    author='Richard Penman, Dionyz Lazar',
    author_email='richard@webscraping.com, contact@dionysio.com',
    description='Sort large CSV files on disk rather than in memory',
    long_description=read('README.rst'),
    keywords=['csv', 'sort', 'large csv'],
    license='lgpl',
    install_requires=[
        "smart_open[s3]==4.2.0",
    ],
)
