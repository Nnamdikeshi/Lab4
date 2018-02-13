import unittest
import CamelcaseV2
from unittest import TestCase

class TestCamelCase(unittest.TestCase):
	
	def test_camelcaseV2_sentence(self):
		self.assertEqual('helloWorld', CamelcaseV2.camel_case('Hello World'))
	def test_blank(self):
		self.assertEqual('', CamelcaseV2.camel_case(''))
		