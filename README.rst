pyramid_html_minifier
=====================

|build status|_
|code coverage|_

.. |build status| image:: https://secure.travis-ci.org/davidemoro/pyramid_html_minifier.png?branch=master
.. _build status: http://travis-ci.org/davidemoro/pyramid_html_minifier
.. |code coverage| image:: http://codecov.io/github/davidemoro/pyramid_html_minifier/coverage.svg?branch=master
.. _code coverage: http://codecov.io/github/davidemoro/pyramid_html_minifier?branch=master

``pyramid_html_minifier`` introduces *safe* html minification
with *no overhead* for ``Pylons/Pyramid`` applications powered by:

* ``Chameleon`` templates (``ZPT`` based template implementation). ``Chameleon``
  templates are still valid ``XML``, so they can be safely minified with not
  too aggressive minification options

* ``Yeoman`` workflow integration and related tools (gulp/grunt, npm, etc)

``pyramid_html_minifier`` is not meant to be used as a standalone
Pylons/Pyramid package and it's up to you creating your own ``Yeoman`` setup.
Here you can find a project using ``pyramid_html_minifier``:

* https://github.com/Kotti/kotti_frontend

What you get with pyramid_html_minifier
---------------------------------------

* save precious kilobytes (~50-80% depending on your templates).
  It is quite important for bandwith usage and improved performance,
  even more important if you have to manage a big and fat
  ``Pylons/Pyramid`` based website with a lot of traffic.
  See https://www.npmjs.com/package/html-minifier

* no overhead, the minification is based on a build step (a sort of
  gulp/grunt based collectstatic)

* safe templaet/html minification. This pattern has been adopted on production
  websites with no issues after 1 year. So I dare say it is a safe pattern
  after a 1-year quarantine

What pyramid_html_minifier does
-------------------------------

What ``pyramid_html_minifier`` introduces:

* a custom ``.html`` renderer (interpreted as ``Chameleon`` templates)

* support for ``dist`` vs ``app``, commonly used in ``Yeoman``
  projects. ``app`` will be used for development, while ``dist``
  in production mode (based on a template minification build).

This way you can start developing static mock applications (even
heavily Javascript based) using the ``Yeoman`` workflow and use your
modified html files as ``Chameleon`` templates:

How to use pyramid_html_minifier
--------------------------------

* first of all create a new Yeoman project in your Pyramid templates dir (eg: ``webapp``).
  It's up to you creating choosing the right Yeoman scaffolding or starting from
  scratch

* remove too aggressive html minification options (tested with ``html-minifier`` and its friend
  ``gulp-html-minifier`` with ``keepClosingSlash`` enabled)

* if you want you can add ZPT/Chameleon macros and slots to your base ``index.html`` template

* add on your ``.ini`` file ``pyramid_html_minifier.placeholder = app`` or ``dist`` depending on
  if you want to run in development or production mode (will be used minificated templates in such
  case)

* register your callable views with ``renderer="your_package:templates/webapp/{0}/webapp/index.html"``.
  The ``.html`` renderer provided by ``pyramid_html_minifier`` will automatically
  pick up the right template depending on your ``.ini`` file settings.

Why Yeoman
----------

Why ``Yeoman``:

* better and more modern web development experience

* minification and/or resources concatenation (images, css, Javascript)

* more. See http://yeoman.io/

Links
-----

More details about projects and case studies using this pattern:

* http://davidemoro.blogspot.it/2014/09/plone-angularjs-yeoman-starter.html

* http://davidemoro.blogspot.com/2014/09/pyramid-starter-seed-yeomam-part-1.html

* http://davidemoro.blogspot.it/2013/08/yeoman-express-and-angularjs.html

Authors
-------

* Davide Moro (https://twitter.com/davidemoro)
