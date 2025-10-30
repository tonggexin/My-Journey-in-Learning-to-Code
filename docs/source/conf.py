# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = '我和所有本科美女同学发生了性关系'
copyright = '2025, 玉蝶游龙'
author = '玉蝶游龙'
release = '1.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.apidoc',
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.graphviz',
]

templates_path = ['_templates']
exclude_patterns = []

language = 'zh_CN'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = 'alabaster'
html_theme = 'furo'
html_static_path = ['_static']
html_theme_options = {
    "sidebar_hide_name": True,
    "light_css_variables": {
        "color-brand-primary": "红色",
        "color-brand-content": "#CC3333",
        "color-admonition-background": "橙色",
    },
    "navigation_with_keys": True,
}
html_logo = "_static/logo/1761781029225xkiid2k9.jpg"


numfig = True