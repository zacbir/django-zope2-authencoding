from setuptools import setup, find_packages

setup(
    name="djangoauthencoding.main",
    version="0.1",
    packages=find_packages("src"),
    package_dir={"": "src"},
    data_files=[('djangoauthencoding/main', ['src/djangoauthencoding/main/configure.zcml'])],
    namespace_packages=["djangoauthencoding"],
    install_requires=["setuptools",
                      "Zope2"],
    zip_safe=False,
)