===============================
Jinja2 Pluralize
===============================

.. image:: https://badge.fury.io/py/jinja2_pluralize.png
    :target: http://badge.fury.io/py/jinja2_pluralize
    
.. image:: https://travis-ci.org/audreyr/jinja2_pluralize.png?branch=master
        :target: https://travis-ci.org/audreyr/jinja2_pluralize

.. image:: https://pypip.in/d/jinja2_pluralize/badge.png
        :target: https://pypi.python.org/pypi/jinja2_pluralize


Jinja2 pluralize filter, adapted from Django's pluralize filter.

* Free software: BSD license
* Documentation: http://jinja2_pluralize.rtfd.org.

Features
--------

* Super-lightweight, for when you don't want to require Django as a dependency.

Usage
-----

See https://docs.djangoproject.com/en/dev/ref/templates/builtins/#pluralize

To use it with Jinja2, update the `filters` dict on the environment like this:

.. code-block:: python

    from jinja2 import Environment
    from jinja2_pluralize import pluralize

    env = Environment()
    env.filters['pluralize'] = pluralize
    tmpl = env.from_string('vote{{ 0|pluralize }}')
    assert tmpl.render() == 'votes'
