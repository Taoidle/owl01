import setuptools

setuptools.setup(
  name = "owl01",
  version = "0.0.3",
  description = "A polyfill version OWL01 for run in pyodide package",
  # https://stackoverflow.com/questions/51286928/what-is-where-argument-for-in-setuptools-find-packages
  # DO NOT pack mock (like js) into output
  packages = setuptools.find_packages(where = 'src'),
  # special the root
  package_dir = {
    '': 'src',
  },
  classifiers = [
  ],
  author = 'Jeremie',
  author_email = 'lucheng989898@protonmail.com',
  python_requires = '>=3.6',
)

# pip install mypy
# mypy src/owl01/__init__.py
# stubgen src/owl01/

# https://blog.ganssle.io/articles/2021/10/setup-py-deprecated.html
# pip install build
# python -m build
