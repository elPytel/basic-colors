from setuptools import setup, find_packages

setup(
    version='0.1.0',
    name='my-colors',
    py_modules=["my_colors"],
    author='elPytel',
    author_email='jaroslav.korner1@gmail.com',
    description='A module for printing colored text to the terminal',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/elPytel/my-colors',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)