#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_jinja2_pluralize
----------------------------------

Tests for `jinja2_pluralize` module.
"""

import unittest

from jinja2 import Environment

from jinja2_pluralize import pluralize


class TestPluralize(unittest.TestCase):

    def setUp(self):
        pass

    def test_pluralize(self):
        """ 
        Tests pluralize() as a Python function.
        From django.tests.defaultfilters.tests: http://git.io/Jem7Ng
        """
        self.assertEqual(pluralize(1), '')
        self.assertEqual(pluralize(0), 's')
        self.assertEqual(pluralize(2), 's')
        self.assertEqual(pluralize([1]), '')
        self.assertEqual(pluralize([]), 's')
        self.assertEqual(pluralize([1, 2, 3]), 's')
        self.assertEqual(pluralize(1, 'es'), '')
        self.assertEqual(pluralize(0, 'es'), 'es')
        self.assertEqual(pluralize(2, 'es'), 'es')
        self.assertEqual(pluralize(1, 'y,ies'), 'y')
        self.assertEqual(pluralize(0, 'y,ies'), 'ies')
        self.assertEqual(pluralize(2, 'y,ies'), 'ies')
        self.assertEqual(pluralize(0, 'y,ies,error'), '')

    def test_pluralize_as_filter(self):
        """ Tests pluralize as a Jinja2 filter. """
        env = Environment()
        env.filters['pluralize'] = pluralize
        tmpl = env.from_string('vote{{ 0|pluralize }}')
        assert tmpl.render() == 'votes'

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
