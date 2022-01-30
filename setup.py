from distutils.core import setup
setup(
  name = 'pyqtCuWi',         # How you named your package folder (MyLib)
  packages = ['pyqtCuWi'],   # Chose the same as "name"
  version = '1.4.1',      # Start with a small number and increase it with every change you make
  license='GPL v3.0',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Custom Widgets For PyQt5',   # Give a short description about your library
  author = 'Mücahit Yusuf Yasin Gündüz',                   # Type in your name
  author_email = 'myygunduz@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/myygunduz/pyqtCuWi',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/myygunduz/pyqtCuWi/archive/refs/tags/1.4.1.tar.gz',    # I explain this later on
  keywords = ['PyQt5', 'python', 'GUI'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          "PyQt5",
          "pyqt5-plugins",
          "PyQt5-Qt5",
          "PyQt5-sip",
          "pyqt5-tools",
          "pyqt5Custom",
          "Pygments",
          "Beautifulsoup4"
      ],
  classifiers=[
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    "Operating System :: OS Independent"
  ],
)