from setuptools import setup, find_packages

version = '0.1.0'

setup(
    name='stemp',
    version=version,
    description=('Simple templating mini-DSL'),
    author='David Hain',
    author_email='dhain@zognot.org',
    url='http://zognot.org/projects/stemp/',
    license='MIT',
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    packages=find_packages(exclude='tests'),
)
