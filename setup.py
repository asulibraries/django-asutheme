from codecs import open
from setuptools import setup

with open('README.rst', 'r', 'utf-8') as f:
    readme = f.read()

setup(
    name='django-asutheme',
    version='0.2.7',
    description='Base templates for Django that adhere to ASU Web Standards.',
    long_description=readme,
    author='Matt Cordial',
    author_email='matt.cordial@asu.edu',
    url='https://github.com/asulibraries/django-asutheme',
    license='Apache 2.0',
    packages=['asutheme'],
    include_package_data=True,
    keywords=['Arizona State University'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'License :: Free for non-commercial use',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Environment :: Web Environment',
        'Topic :: Software Development :: User Interfaces',
    ]
)
