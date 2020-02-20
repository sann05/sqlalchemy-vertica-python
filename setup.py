from setuptools import setup
from setuputils import TestCoverageRatchetCommand, VerifyVersionCommand

__version__ = '0.5.6'
setup(
    name='sqlalchemy-vertica-python',
    version=__version__,
    description='Vertica dialect for sqlalchemy using vertica_python',
    long_description=open("README.rst").read(),
    license="MIT",
    url='https://github.com/bluelabsio/sqlalchemy-vertica-python',
    download_url = 'https://github.com/bluelabsio/sqlalchemy-vertica-python/tarball/{}'.format(__version__),
    author='Luke Emery-Fertitta',
    maintainer='Vince Broz',
    maintainer_email='opensource@bluelabs.com',
    packages=[
        'sqla_vertica_python',
    ],
    entry_points="""
    [sqlalchemy.dialects]
    vertica.vertica_python = sqla_vertica_python.vertica_python:VerticaDialect
    """,
    install_requires=[
        'vertica_python'
    ],
    cmdclass={
        'coverage_ratchet': TestCoverageRatchetCommand,
        'verify': VerifyVersionCommand,
    },
)
