#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup


requirements = [
    'face_recognition_models>=0.3.0',
    'Click>=6.0',
    'Cmake',
    'dlib>=19.7',
    'numpy',
    'Pillow',
    'flask',
    'flask_cors',
]

test_requirements = [
    'tox',
    'flake8'
]

setup(
    name='face_recognition',
    version='1.4.0',
    description="Recognize faces from Python or from the command line",
    long_description='',
    author="Daniil Brezhnev",
    author_email='danbrezh@gmail.com',
    packages=[
        'face_recognition',
    ],
    package_dir={'face_recognition': 'face_recognition'},
    package_data={
        'face_recognition': ['models/*.dat']
    },
    entry_points={
        'console_scripts': [
            'face_recognition=face_recognition.face_recognition_cli:main',
            'face_detection=face_recognition.face_detection_cli:main'
        ]
    },
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='face_recognition',
    classifiers=[
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    test_suite='tests',
    tests_require=test_requirements
)