import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
with open("requirements.txt", "r", encoding="utf-8") as req:
    requirements = req.readlines()

setuptools.setup(
    name="pyqtCuWi",
    version="1.4.0",
    license="GPL v3.0",
    author="Mücahit Yusuf Yasin Gündüz",
    author_email="myygunduz@gmail.com",
    description="Custom Widgets For PyQt5",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/myygunduz/pyqtCuWi",
    project_urls={
    'Documentation': 'https://github.com/myygunduz/pyqtCuWi/blob/main/documentation.md',
    },
    download_url="https://github.com/myygunduz/pyqtCuWi/archive/refs/tags/2.0.3.tar.gz",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent"
    ],
    keywords = ["PyQt5","Custom Widgets","myygunduz","python"],
    python_requires='>=3.8.0',
    install_requires=[requirements]
)