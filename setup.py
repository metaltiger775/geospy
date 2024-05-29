from setuptools import setup, find_packages

setup(
    name='geospy',
    version='0.1.8',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    author='metaltiger775',
    description='AI powered geo-location to uncover the location of photos.',
    url='https://github.com/metaltiger775/geospy',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
