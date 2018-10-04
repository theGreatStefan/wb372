import re

def is_integer(str):
	'''Question 1'''
	pattern = re.compile('[-+]?\d+')
	leading_zeros = re.compile('0+\d+')
	if pattern.match(str):
		if leading_zeros.match(str):
			return False
		else:
			return True
	else:
		return False

def is_english_number:
	'''Questio 2'''
	pattern = re.compile('\d{1,3}|\d{1,3},\d{1,3}|\d{1,3},\d{1,3},\d{1,3}')
	pass
