from setuptools import find_packages, setup

with open("README.md") as f1:
    long_description = f1.read()

setup(
    name='alphabetize',
    version='0.0.1',
    description='Alphabetize variables within your files',
    long_description=long_description,
    keywords="variable-sorting",
    author="Jake Adey",
    author_email="jakespenceradey@gmail.com",
    url="https://github.com/JakeAdey/alphabetize",
    license="MIT",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development :: Quality Assurance",
    ],
    # py_modules=['alphabetize'],
    install_requires=["setuptools", "wheel"],
    packages=find_packages("src"),
    package_dir={'': 'src'},
    entry_points={'console_scripts': ['alphabetize = alphabetize:main']},

)
