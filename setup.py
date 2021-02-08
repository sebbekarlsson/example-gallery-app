from setuptools import setup, find_packages


setup(
    name='gallery',
    version='1.0.0',
    install_requires=[
        'flask',
        'sqlalchemy',
        'pymysql'
    ],
    packages=find_packages(),
    entry_points={
        'console_scripts': [
        ]
    }
)
