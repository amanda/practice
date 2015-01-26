import unittest

def to_numeral(some_int):
	if some_int == 0 or type(some_int) != int:
		raise TypeError #the romans didn't have 0 :'(

	numeral = ''
	numerals = [('M', 1000), ('CM', 900), ('D', 500), ('CD', 400), ('C', 100), ('XC', 90), ('L', 50), ('XL', 40), ('X', 10), ('IX', 9), ('V', 5), ('IV', 4), ('I', 1)]

	for (roman, arabic) in numerals:
		if some_int >= arabic:
			numeral += roman * (some_int//arabic)
			some_int %= arabic

	return numeral


class TestRomanNumerals(unittest.TestCase):
	def test_to_numeral(self):
		self.assertEqual(to_numeral(8), 'VIII')
		self.assertEqual(to_numeral(50), 'L')
		self.assertEqual(to_numeral(3999), 'MMMCMXCIX')
		self.assertEqual(to_numeral(345), 'CCCXLV')
		self.assertEqual(to_numeral(777), 'DCCLXXVII')
		self.assertRaises(TypeError, lambda: to_numeral(0))
