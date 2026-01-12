# Configuration file for the Sphinx documentation builder.

import os
import sys

# Permet à Sphinx d'importer ton code (racine projet)
# docs/source -> remonte à la racine du projet
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
    "sphinxcontrib.openapi",
]

templates_path = ["_templates"]
exclude_patterns = []

# RST + Markdown
source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

# Qualité autodoc (recommandé)
autodoc_member_order = "bysource"
autodoc_typehints = "description"  # met les types dans la doc, pas dans la signature
napoleon_google_docstring = True
napoleon_numpy_docstring = False

# MyST (optionnel mais cool)
myst_heading_anchors = 3  # ancres automatiques pour h1/h2/h3

# -- Options for HTML output -------------------------------------------------
html_theme = "furo"
html_static_path = ["_static"]

# (Optionnel) titre dans l’onglet
html_title = f"{project} documentation"