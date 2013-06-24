from setuptools import setup, find_packages

setup(
    name="djangoauthencoding.main",
    version="0.1",
    packages=find_packages("src"),
    package_dir={"": "src"},
    namespace_packages=["djangoauthencoding"],
    install_requires=["setuptools",
                      "Zope2"],
)