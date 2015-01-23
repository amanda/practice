import unittest

number_words = {1: 'one',
				2: 'two',
				3: 'three',
				4: 'four',
				5: 'five',
				6: 'six',
				7: 'seven',
				8: 'eight',
				9: 'nine',
				10: 'ten',
				11: 'eleven',
				12: 'twelve',
				13: 'thirteen',
				14: 'fourteen',
				15: 'fifteen',
				16: 'sixteen',
				17: 'seventeen',
				18: 'eighteen',
				19: 'nineteen',
				20: 'twenty',
				30: 'thirty',
				40: 'forty',
				50: 'fifty',
				60: 'sixty',
				70: 'seventy',
				80: 'eighty',
				90: 'ninety'}


def make_number_words(number):
	if number == 1000:
		return 'onethousand'
	
	if number in number_words:
		return number_words[number]
	
	hundreds, potential_tens = divmod(number, 100)
	
	if hundreds == 0:
		wordy_hundreds = ''
	else: 
		wordy_hundreds = number_words[hundreds] + 'hundred'
	
	if potential_tens == 0:
		return wordy_hundreds
	elif potential_tens in number_words:
		wordy_tens = number_words[potential_tens]
		wordy_ones = ''
	else:
		tens, potential_ones = divmod(potential_tens, 10)
		wordy_ones = number_words[potential_ones]
		wordy_tens = number_words[tens * 10]
	
	if wordy_hundreds and (wordy_tens or wordy_ones):
		return wordy_hundreds + 'and' + wordy_tens + wordy_ones
	else:
		return wordy_hundreds + wordy_tens + wordy_ones

def generate_letters(n):
	allnumbers_length = 0
	for i in range(1, n+1):
		no_space_number = make_number_words(i)
		allnumbers_length += len(no_space_number)
	return allnumbers_length

class TestNumberWords(unittest.TestCase):
	def test_hundreds(self):
		self.assertEquals(make_number_words(20), 'twenty')
		self.assertEquals(make_number_words(41), 'fortyone')
		self.assertEquals(make_number_words(101), 'onehundredandone')
		self.assertEquals(make_number_words(1), 'one')
		self.assertEquals(make_number_words(560), 'fivehundredandsixty')
		self.assertEquals(make_number_words(1000), 'onethousand')
		self.assertEquals(make_number_words(75), 'seventyfive')
		self.assertEquals(make_number_words(40), 'forty')
		self.assertEquals(make_number_words(100), 'onehundred')
		self.assertEquals(make_number_words(200), 'twohundred')
		self.assertEquals(make_number_words(21), 'twentyone')
		self.assertEquals(len(make_number_words(342).strip()), 23)
		self.assertEquals(len(make_number_words(115).strip()), 20)

if __name__ == '__main__':
	#unittest.main()
	print generate_letters(1000)
