from setuptools import find_packages, setup

with open('README.md','r') as f:
    long_description = f.read()
    
setup(
    name='pgbackup',
    version='0.1.0',
    author= 'Luis Juarez',
    author_email='luisj@gruposega.net',
    description='A utility for backup PostgresSQL databases',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/lj-olumatec/PGBackup',
    packages=find_packages('src')
)