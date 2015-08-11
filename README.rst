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

What you get with pyramid_html_minifier
---------------------------------------

* **bandwith and performance.** Save precious kilobytes (~50-80% depending on your templates).
  It is quite important for bandwith usage and improved performance,
  even more important if you have to manage a big and fat
  ``Pylons/Pyramid`` based website with a lot of traffic.
  See https://www.npmjs.com/package/html-minifier

* **no overhead.** The minification is based on a build step (a sort of
  gulp/grunt based collectstatic). So no minification on the fly

* **safe template/html minification**. It works even with ``macros``
  and ``slots``.
  This pattern has been adopted on production websites with no issues
  after 1 year. So I dare say it is a safe pattern after a
  1-year quarantine without any sort of problems. You should only
  remember to disable too aggressive minification options (see next
  sections)

What pyramid_html_minifier does
-------------------------------

What ``pyramid_html_minifier`` introduces:

* a custom ``.html`` renderer (interpreted as ``Chameleon`` templates)

* support for ``dist`` vs ``app``, commonly used in ``Yeoman``
  projects. ``app`` will be used for development, while ``dist``
  in production mode (based on a template minification build).

This way you can start developing static mock applications (even
heavily Javascript based) using the ``Yeoman`` workflow and use your
modified html files enriched by macros and slots as ``Chameleon``
templates.

How to use pyramid_html_minifier
--------------------------------

Here you can see how to enable Chameleon templates minification in your
``Pylons/Pyramid`` web application:

* put your ``Chameleon`` template file in ``templates/app/master.html`` and its
  minified version in ``templates/dist/master.html`` (the ``.html`` extension is
  important). Obviously don't do minification by hand, add ``Yeoman`` in your
  development workflow with its related tools for automation.
  This package does not provide any ``gulp`` or ``grunt`` configuration,
  you are supposed to create your own setup

* register a normal ``Pylons/Pyramid`` callable view with
  ``renderer="your_plugin:templates/{0}/master.html"``. The ``{0}`` is only
  a placeholder that ``pyramid_html_minifier`` will fill depending on your
  settings. See next step

* tell ``pyramid_html_minifier`` if you want to pick up standard templates or
  minified ones adding the ``pyramid_html_minifier.placeholder`` setting to your
  ``.ini`` file. Typical value for development is ``app`` (the default one),
  while ``dist`` is usually used for prodcution environments.
  Example: ``pyramid_html_minifier.placeholder = dist``

* add ``pyramid_html_minifier`` to your pyramid.includes setting

The final .ini file should looks like the following one::

    pyramid.includes =
        ...
        pyramid_html_minifier
    
    ...
    
    pyramid_html_minifier.placeholder = dist

Safe minification options
-------------------------

I suggest to automate the build process integrating the ``Yeoman`` workflow into your
``Pylons/Pyramid`` project for the best developing experience.

I suggest to use the ``html-minifier`` minificator and its friend ``gulp-html-minifier``
disabling too aggressive html minification options.

In particular be sure that the ``keepClosingSlash`` option is enabled and
``removeAttributeQuotes`` is disabled.

Here you can see a real example working configuration::

    const htmlMinifierOptions = {
      collapseBooleanAttributes: true,
      collapseWhitespace: true,
      removeComments: true,
      removeCommentsFromCDATA: true,
      removeEmptyAttributes: true,
      removeRedundantAttributes: true,
      useShortDoctype: true,
      keepClosingSlash: true,
      }
    
    ...
    
    gulp.task('html', ['styles'], () => {
      const assets = $.useref.assets({searchPath: ['.tmp', 'app', '.']});
    
      return gulp.src('app/*.html')
        ..
        .pipe($.if('*.html', $.htmlMinifier(htmlMinifierOptions)))
        ...
        .pipe(gulp.dest('dist'));

Why Yeoman
----------

Why ``Yeoman``:

* better and more modern web development experience

* minification and/or resources concatenation (images, css, Javascript)

* more. See http://yeoman.io/

Links
-----

More details about case studies using the same pattern:

* http://davidemoro.blogspot.it/2014/09/plone-angularjs-yeoman-starter.html

* http://davidemoro.blogspot.com/2014/09/pyramid-starter-seed-yeomam-part-1.html

* http://davidemoro.blogspot.it/2013/08/yeoman-express-and-angularjs.html

Authors
-------

* Davide Moro (https://twitter.com/davidemoro)
