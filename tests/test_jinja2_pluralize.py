#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_jinja2_pluralize
----------------------------------

Tests for `jinja2_pluralize` module.
"""

import unittest

from jinja2 import Environment

from jinja2_pluralize import pluralize, pluralize_dj


class TestPluralize(unittest.TestCase):

    def setUp(self):
        pass

    def test_pluralize(self):
        """ 
        Tests pluralize() as a Python function.
        """
        self.assertEqual(pluralize('vote'), 'votes')
        self.assertEqual(pluralize('class'), 'classes')
        self.assertEqual(pluralize('candy'), 'candies')
        self.assertEqual(pluralize('goose'), 'geese')
        self.assertEqual(pluralize('Moose'), 'Moose')
    
    def test_pluralize_as_filter(self):
        """ Tests pluralize as a Jinja2 filter. """
        env = Environment()
        env.filters['pluralize'] = pluralize
        tmpl = env.from_string("{{ 'vote'|pluralize }}")
        assert tmpl.render() == 'votes'
        tmpl = env.from_string("{{ 'goose'|pluralize }}")
        assert tmpl.render() == 'geese'
    
    def test_pluralize_dj(self):
        """ 
        Tests pluralize_dj() as a Python function.
        From django.tests.defaultfilters.tests: http://git.io/Jem7Ng
        """
        self.assertEqual(pluralize_dj(1), '')
        self.assertEqual(pluralize_dj(0), 's')
        self.assertEqual(pluralize_dj(2), 's')
        self.assertEqual(pluralize_dj([1]), '')
        self.assertEqual(pluralize_dj([]), 's')
        self.assertEqual(pluralize_dj([1, 2, 3]), 's')
        self.assertEqual(pluralize_dj(1, 'es'), '')
        self.assertEqual(pluralize_dj(0, 'es'), 'es')
        self.assertEqual(pluralize_dj(2, 'es'), 'es')
        self.assertEqual(pluralize_dj(1, 'y,ies'), 'y')
        self.assertEqual(pluralize_dj(0, 'y,ies'), 'ies')
        self.assertEqual(pluralize_dj(2, 'y,ies'), 'ies')
        self.assertEqual(pluralize_dj(0, 'y,ies,error'), '')
    
    def test_pluralize_dj_as_filter(self):
        """ Tests pluralize_dj as a Jinja2 filter. """
        env = Environment()
        env.filters['pluralize'] = pluralize_dj
        tmpl = env.from_string('vote{{ 0|pluralize }}')
        assert tmpl.render() == 'votes'

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
