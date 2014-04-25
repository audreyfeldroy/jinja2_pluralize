===============================
Jinja2 Pluralize
===============================

.. image:: https://badge.fury.io/py/jinja2_pluralize.png
    :target: http://badge.fury.io/py/jinja2_pluralize
    
.. image:: https://travis-ci.org/audreyr/jinja2_pluralize.png?branch=master
        :target: https://travis-ci.org/audreyr/jinja2_pluralize

.. image:: https://pypip.in/d/jinja2_pluralize/badge.png
        :target: https://pypi.python.org/pypi/jinja2_pluralize


Jinja2 pluralize filters.

* Free software: BSD license
* Documentation: http://jinja2_pluralize.rtfd.org.

Features
--------

1. Simple pluralize filter based on inflect.py. For example, this renders as `geese`:

.. code-block:: jinja2

    {{ 'goose'|pluralize }}

2. Django-style pluralize filter. Works as described in the `Django docs`_. For example, this renders as `votes`:

.. code-block:: jinja2

    vote{{ 0|pluralize }}

.. _Django docs: https://docs.djangoproject.com/en/dev/ref/templates/builtins/#pluralize

Usage
-----

To use it with Jinja2, update the `filters` dict on the environment like this:

.. code-block:: python

    from jinja2 import Environment
    from jinja2_pluralize import pluralize_dj

    env = Environment()
    env.filters['pluralize'] = pluralize_dj
    tmpl = env.from_string('vote{{ 0|pluralize }}')
    assert tmpl.render() == 'votes'

