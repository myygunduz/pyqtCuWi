import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
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
    download_url="https://github.com/myygunduz/pyqtCuWi/archive/refs/tags/1.4.0.tar.gz",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent"
    ],
    keywords = ["PyQt5","Custom Widgets","myygunduz","python"],
    python_requires='>=3.8.0',
    install_requires=[
        "beautifulsoup4>=4.10.0",
        "Pygments>=2.11.2"
        "PyQt5>=5.15.4"
        "pyqt5-plugins>=5.15.4.2.2"
        "PyQt5-Qt5>=5.15.2"
        "PyQt5-sip>=12.9.0"
        "pyqt5-tools>=5.15.4.3.2"
        "pyqt5Custom>=1.0.1"
        "qt-material>=2.8.19"
        "qt5-applications>=5.15.2.2.2"
        "qt5-tools>=5.15.2.1.2"
    ]
)