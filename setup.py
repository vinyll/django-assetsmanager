# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


setup(
    name='assetsmanager',
    version='1.1.0',
    description='Django app to easily manage and your js and css dependencies.',
    long_description="""Django assets manager allows you to classify stylesheet and javascript files 
by collection and manage a collection's dependencies.
You can then simply call a collection within a template and it will include all its assets.""",
    author='Vincent Agnano',
    author_email='vincent.agnano@particul.es',
    url='http://github.com/vinyll/django-assetsmanager',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities',
    ]
)