#!/usr/bin/python3
"""
Unittest for the City
"""

import unittest
from models.city import City


class TestCity(unittest.TestCase):
    def setUp(self):
        self.city = City()

    def test_state_id(self):
        self.assertEqual(self.city.state_id, "")

    def test_name(self):
        self.assertEqual(self.city.name, "")
