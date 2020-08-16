#!/usr/bin/env python

"""The setup script."""

import os
from setuptools import setup, find_packages

import cookietemple_website as module


def walker(base, *paths):
    file_list = set([])
    cur_dir = os.path.abspath(os.curdir)

    os.chdir(base)
    try:
        for path in paths:
            for dname, dirs, files in os.walk(path):
                for f in files:
                    file_list.add(os.path.join(dname, f))
    finally:
        os.chdir(cur_dir)

    return list(file_list)


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('CHANGELOG.rst') as history_file:
    history = history_file.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest>=3', ]

setup(
    author="Imipenem",
    author_email='philipp_ehm@protonmail.com',
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="cookietemple_website. A best practice .",
    entry_points={
        'console_scripts': [
            'cookietemple_website={}.server:main'.format(module.__name__),
        ],
    },
    install_requires=requirements,
    license="MIT",
    long_description=readme + '\n\n',
    include_package_data=True,
    keywords='cookietemple_website',
    name='cookietemple_website',
    packages=find_packages(include=['cookietemple_website', 'cookietemple_website.*']),
    package_data={
        module.__name__: walker(
            os.path.dirname(module.__file__),
            'templates', 'static', 'translations'
        ),
    },
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/cookiejar/cookietemple_website',
    version='0.1.0',
    zip_safe=False,
)
