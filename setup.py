from setuptools import find_packages,setup

setup(
    name="cjsoff",
    version="0.0.1",
    description=" Example of a package",
    package_dir= {"":"src"},
    packages=find_packages(where="cjsoff"),
    author="Cristian Diaz",
    license="MIT",
    author_email="crascris1234@gmail.com",
    install_requires=["pandas >=2.2.1"],
    extras_require={
        "dev":["pytest>=7.0","twine>=4.0"]
    },
    python_requires=">=3.10.3"
)