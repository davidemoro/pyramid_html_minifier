import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.rst')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.rst')) as f:
    CHANGES = f.read()

requires = [
    'pyramid',
    'pyramid_chameleon',
    ]

tests_require = [
    'pytest>=2.4.2',
    'pytest-cov',
    'pytest-pep8!=1.0.3',
    'mock',
    ]

setup(name='pyramid_html_minifier',
      version='0.1',
      description='pyramid_html_minifier',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='Davide Moro',
      author_email='davide.moro@gmail.com',
      url='https://github.com/davidemoro/pyramid_html_minifier',
      keywords='web pyramid pylons',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_require=tests_require,
      test_suite="pyramid_html_minifier",
      entry_points="""\
      """,
      extras_require={
          'testing': tests_require,
          },
      )
