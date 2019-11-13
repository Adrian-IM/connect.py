from setuptools import setup


setup(
    name='connect',
    author='Ingram Micro',
    version='0.0.0',
    keywords='connect ingram sdk',
    packages=['connect', 'connect.api', 'connect.models'],
    description='Connect Python SDK',
    license='Apache Software License',
    install_requires=['requests==2.21.0']
)
