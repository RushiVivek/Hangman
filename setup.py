import setuptools

from cx_Freeze import setup, Executable

base='Win32GUI' 

includefiles = ['C:\\Users\\rushi\\OneDrive\\Desktop\\Programming\\Python\\Hangman\\5000words.txt', 'C:\\Users\\rushi\\OneDrive\\Desktop\\Programming\\Python\\Hangman\\words.txt', 'C:\\Users\\rushi\\OneDrive\\Desktop\\Programming\\Python\\Hangman\\words_alpha.txt']

shortcut_table = [
    ("DesktopShortcut",        # Shortcut
     "DesktopFolder",          # Directory_
     "Hangman",           # Name
     "TARGETDIR",              # Component_
     "[TARGETDIR]Hangman.exe",# Target
     None,                     # Arguments
     None,                     # Description
     None,                     # Hotkey
     None,                     # Icon
     None,                     # IconIndex
     None,                     # ShowCmd
     'TARGETDIR'               # WkDir
     ),
    ("StartMenuShortcut",        # Shortcut
     "StartMenuFolder",          # Directory_
     "Hangman",           # Name
     "TARGETDIR",              # Component_
     "[TARGETDIR]Hangman.exe",# Target
     None,                     # Arguments
     None,                     # Description
     None,                     # Hotkey
     None,                     # Icon
     None,                     # IconIndex
     None,                     # ShowCmd
     'TARGETDIR'               # WkDir
     )
]

msi_data = {"Shortcut": shortcut_table}

bdist_msi_options = {'data': msi_data}

executables = [Executable("hangman.py", base=base,)]

packages = ["idna", 'time', 'pygame', 'random', 'sys']
options = {
    'build_exe': {    
        'packages':packages,
        'include_files':includefiles,
        "excludes": ["tkinter", "PyQt4.QtSql", "sqlite3", 
                     "scipy.lib.lapack.flapack",
                     "PyQt4.QtNetwork",
                     "PyQt4.QtScript",
                     "numpy.core._dotblas", 
                     "PyQt5",
                     "matplotlib.tests",
                     "numpy.random._examples",
                     "matplotlib.backends",
                     "pandas",
                     "scipy"]
    },
    "bdist_msi": bdist_msi_options,
}

setup(
    name = "Hangman",
    options = options,
    version = "1.0",
    description = 'Hangman game by Rushi',
    executables = executables,
    author = 'Amaram Rushi',
    author_email = 'rushivivek123@gmail.com',
    url = '',
    license = 'MIT',
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Games/Entertainment :: Puzzle Games',
        'Topic :: Games/Entertainment :: Board Games',
    ],
    keywords = 'Hangman Game',
    project_urls = {
        'Source': 'hangman.py',
        'Bug Reports': '',
        'Funding': '',
    },
    python_requires = '>=3.6',
    install_requires = ['pygame'],
    include_package_data = True,
    zip_safe = False,
    entry_points = {
        'console_scripts': [
            'hangman = hangman:main',
        ],
    },
    package_data = {'': ['*.txt']},
    platforms = 'Windows',
    download_url = ''
)