# Configuration file for the Sphinx documentation builder.

import os
import sys

# Permet à Sphinx d'importer ton code (racine projet)
sys.path.insert(0, os.path.abspath("../.."))

# -- Project information -----------------------------------------------------
project = "tuto-sphinx"
copyright = "2026, Mathieu"
author = "Mathieu"
release = "0"

# -- General configuration ---------------------------------------------------
extensions = [
    "myst_parser",
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
]

templates_path = ["_templates"]
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}