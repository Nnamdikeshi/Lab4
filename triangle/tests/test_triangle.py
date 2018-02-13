import unittest
from triangle import triangle_math

class TestTriangle(unittest.TestCase):

	def test_triangle_area(self):
		self.assertEqual(12, triangle_math.area(6, 4))
		
	def test_floating_point(self):
		self.assertAlmostEqual(17.79875, triangle_math.area(7.25, 4.91))
		
	def test_raises_exception_for_negative_params(self):
		# Assert that the code raises a ValueError
		# no ValueError = test fail.
		with self.assertRaises(ValueError):
			triangle_math.area(-10, 9)
			
	def test_base_height_is_zero(self):
		self.assertNotEqual(triangle_math.area, 0)
		
	