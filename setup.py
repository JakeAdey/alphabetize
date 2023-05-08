from setuptools import setup

setup(
    name='alphabetize',
    version='0.0.1',
    description='Alphabetize your file content!',
    py_modules=['alphabetize'],
    package_dir={'': 'src'},
    entry_points={'console_scripts': ['alphabetize = alphabetize:parse_args']}
)
