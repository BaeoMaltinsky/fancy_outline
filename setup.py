#! /usr/bin/env python


from setuptools import setup


setup(
    name='fancy_outline',
    version='0.1.2',
    author='Baeo Maltinsky',
    author_email='baeomaltinsky@gmail.com',
    description='mdx_outline with optional "Jump to Top" links',
    py_modules=['fancy_outline'],
    install_requires=['Markdown>=2.0',],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: BSD License',
        'Intended Audience :: Developers',
        'Environment :: Web Environment',
        'Programming Language :: Python',
        'Topic :: Text Processing :: Filters',
        'Topic :: Text Processing :: Markup :: HTML'
    ]
)
