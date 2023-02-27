import setuptools

setuptools.setup(
  name = "owl01",
  version = "0.0.1",
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