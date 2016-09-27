from setuptools import setup, find_packages
from codecs import open
from os import path

__version__ = '{{cookiecutter.version}}'

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


install_requires = []

def setup_package():
    setup(
        name='{{cookiecutter.app_name}}',
        description='{{cookiecutter.project_short_description}}',
        long_description=long_description,
        url='https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.app_name}}',
        license='BSD',
        classifiers=[
          'Programming Language :: Python',
        ],
        keywords='',
        packages=find_packages(exclude=['docs', 'tests*']),
        setup_requires=['setuptools_scm'],
        use_scm_version=True,
        zip_safe=False,
        include_package_data=True,
        author='{{cookiecutter.full_name}}',
        install_requires=install_requires,
        author_email='{{cookiecutter.email}}'
    )

if __name__ == "__main__":
    setup_package()
