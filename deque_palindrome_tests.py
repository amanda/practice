#fun with testing~
import unittest
from deque_palindrome import Deque, is_palindrome

class DequeTest(unittest.TestCase):
	def test_adding(self):
		d = Deque()
		d.add_to_front(4)
		d.add_to_front(5)
		d.add_to_back(3)
		self.assertEqual(d.items, [3, 4, 5])

	def test_removal(self):
		d = Deque()
		d.add_to_front(3)
		d.add_to_front(4)
		d.add_to_front(8)
		d.remove_from_back()
		self.assertEqual(d.items, [4, 8])

class PalindromeTest(unittest.TestCase):
	def test_if_palindrome(self):
		self.assertFalse(is_palindrome('dog'))
		self.assertTrue(is_palindrome('radar'))
		self.assertFalse(is_palindrome(''))
		self.assertTrue(is_palindrome('racecar'))
		self.assertFalse(is_palindrome('python'))
