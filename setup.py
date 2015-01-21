# coding: utf-8
import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), "README.md")) as readme:
	README = readme

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='mommy_spatial_generators',
    version='0.1',
    packages=['mommy_spatial_generators'],
    include_package_data=True,
    license='Apache 2.0',  # example license
    description='Spatial generators for model mommy. This enables you to generate dummy values for GeoDjango fields.',
    long_description=README,
    url='http://www.sigmageosistemas.com.br',
    author='George Silva',
    author_email='george@consultoriasigma.com.br',
    install_requires=["model_mommy"],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: Proprietária', # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)