# setup.py for a python package


from setuptools import setup, find_packages


setup(
    name='pytubepubsub',
    version='0.1',
    description='A python package for simplifying YouTube pubsubhubbub subscriptions',
    author='Evan Calzolaio',

    packages=find_packages(),

    install_requires=[
        'requests',
    ]
)
