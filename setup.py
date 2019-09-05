from setuptools import setup, find_packages
import sys

__version__ = '0.6'


python_major = sys.version_info.major
python_minor = sys.version_info.minor


# Dependencies have different max versions based on python version
if sys.version_info < (3, 5):  # Python < 3.5
    version_based_dependencies = [
        'scikit-learn<0.21.0',
        'scipy<1.3.0',  # Scikit-learn dependency
        'pandas<0.25.0',
    ]
else:
    version_based_dependencies = [
        'scikit-learn',
        'pandas',
    ]

# Different extras
postgres_dependencies = ["psycopg2"]
deep_learning_dependencies = ["keras", "tensorflow", "hickle"]
cloud_dependencies = ["onedrivesdk", "apache-libcloud", "pycrypto", "sshtunnel"]


setup(
    name='simpleml',
    version=__version__,
    description='Simplified Machine Learning',
    author='Elisha Yadgaran',
    author_email='ElishaY@alum.mit.edu',
    license='BSD-3',
    url='https://github.com/eyadgaran/SimpleML',
    download_url='https://github.com/eyadgaran/SimpleML/archive/v{}.tar.gz'.format(__version__),
    packages=find_packages(),
    keywords=['machine-learning', 'deep-learning', 'automated-learning'],
    install_requires=[
        'sqlalchemy',
        'sqlalchemy_mixins',
        'alembic',
        'numpy',
        'dill',
        'future',
        'configparser',
        'simplejson',
    ] + version_based_dependencies,
    dependency_links=["https://github.com/absent1706/sqlalchemy-mixins/tarball/master#egg=sqlalchemy_mixins"],
    extras_require={
        'postgres': postgres_dependencies,
        'deep-learning': deep_learning_dependencies,
        'cloud': cloud_dependencies,
        'all': postgres_dependencies + deep_learning_dependencies + cloud_dependencies
    },
    zip_safe=False,
    test_suite='nose.collector',
    tests_require=['nose'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ],
    python_requires='>=2.7,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*,!=3.4.*,>=3.5',
)
