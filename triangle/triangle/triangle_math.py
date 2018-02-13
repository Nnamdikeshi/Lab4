def area(base, height):
	'''Compute he are of a triangle with the given base and height'''
	
	
	'''Raises value error if base or height or both are negative'''
	if base < 0 or height < 0:
		raise ValueError('Base and height must be positive. \ Was given base: {}, height {}'.format(base, height))
		
	area = base * height / 2
	return area