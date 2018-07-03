Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> text = "Ram is 45 years old and email id is ram213@gmail.com and Shyam is 40 years old and email id is shyam_1212@gmail.com"
>>> import re
>>> re.findall('/([A-Z]\w+)/',text)
[]
>>> re.findall(/([A-Z]\w+)/,text)
SyntaxError: invalid syntax
>>> re.findall('/([A-Z])/',text)
[]
>>> re.findall('([A-Z])',text)
['R', 'S']
>>> re.findall('([A-Z]\w+)',text)
['Ram', 'Shyam']
>>> re.findall('([0-0])',text)
['0']
>>> re.findall('([0-9])',text)
['4', '5', '2', '1', '3', '4', '0', '1', '2', '1', '2']
>>> re.findall('([0-9]\w+)',text)
['45', '213', '40', '1212']
>>> re.findall('([0-9]\w+[\s])',text)
['45 ', '40 ']
>>> re.findall('[a-z | 0-9]\w+[@]\w+[.]\w+')
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    re.findall('[a-z | 0-9]\w+[@]\w+[.]\w+')
TypeError: findall() missing 1 required positional argument: 'string'
>>> re.findall('[a-z | 0-9]\w+[@]\w+[.]\w+', text)
[' ram213@gmail.com', ' shyam_1212@gmail.com']
>>> pattern = '[a-z | 0-9]\w+[@]\w+[.]\w+'
>>> email_id = 'ram123@gmail.com'
>>> re.match(pattern, text)
>>> x = re.match(pattern, text)
>>> print()x
SyntaxError: invalid syntax
>>> print(x)
None
>>> re.match(pattern, email_id)
<_sre.SRE_Match object; span=(0, 16), match='ram123@gmail.com'>
>>> re.search(pattern, email_id)
<_sre.SRE_Match object; span=(0, 16), match='ram123@gmail.com'>
>>> if re.match(pattern, email_id):
	print("Valid")
else:
	print("Invalid")

	
Valid
>>> email_id = "Ram123@gmail.com"
>>> if re.match(pattern, email_id):
	print("Valid")
else:
	print("Invalid")

	
Invalid
>>> email_id = "123ram@gmail.com"
>>> if re.match(pattern, email_id):
	print("Valid")
else:
	print("Invalid")

	
Valid
>>> 
