# -- Path setup --------------------------------------------------------------

from sys import path
from os.path import abspath
path.insert(0, abspath('../..'))


# -- Project information -----------------------------------------------------

project = 'randword'
copyright = '2022, Artyom Bezmenov'
author = 'Artyom Bezmenov (8nhuman)'

release = '2.11.1'


# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode'
]

master_doc = 'index'

templates_path = ['_templates']

exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

html_theme = 'alabaster'

html_static_path = ['_static']
