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

def is_english_number(str):
	'''Questio 2'''
	pattern = re.compile('^\d{1,3}(,\d{3})*$')
	pattern1 = re.compile('^\d{1,3}$')
	pattern2 = re.compile('^\d{1,3},\d{3}$')
	pattern3 = re.compile('^\d{1,3},\d{3},\d{3}$')
	if pattern.match(str):
		return True
	else:
		return False
	
def is_version(str):
	'''Question 3'''
	pattern = re.compile('^v( )*\d{1,3}$|^version( )*\d{1,3}$')
	if pattern.match(str):
		return True
	else:
		return False
	
def is_uuid(str):
	'''Question 4'''
	pattern = re.compile('^([a,b,c,d,e,f,\d]){8}(-([a,b,c,d,e,f,\d]){4}){3}-([a,b,c,d,e,f,\d]){12}$')
	if pattern.match(str):
		return True
	else:
		return False

def is_ipv4_addr(str):
	'''Question 5'''
	pattern = re.compile('^((25[0-5]|2[0-4][0-9]|[1]?[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|[1]?[1-9]?[0-9])$')
	if pattern.match(str):
		return True
	else:
		return False

def is_email_addr(str):
	'''Question 6'''
	pattern = re.compile('^[a-z,A-Z]([\w,\d,\.,!,#,$,%,&,\',*,+,\-,\/,=,?,^,`,{,|,},~])+\w@([\w])[\w,-]*([\w])+((\.([\w])[\w,-]*([\w]))+)$')
	if pattern.match(str):
		return True
	else:
		return False

def is_ssn(str):
	'''Question 7'''
	pattern = re.compile('^(?!219-09-9999|078-05-1120)(?!666|000|9\d{2})d{3}-(?!00)\d{2}-(?!0{4})\d{4}$')
	if pattern.match(str):
		return True
	else:
		return False
		
def is_valid_password(str):
	'''Question 8'''
	pattern = re.compile('^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&#])[A-Za-z\d@$!%*?&#]{8,}$')
	if pattern.match(str):
		return True
	else:
		return False

		
