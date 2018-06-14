Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> data = (2,3,4,6,7)
>>> type(data)
<class 'tuple'>
>>> data[0]
2
>>> data[0:4]
(2, 3, 4, 6)
>>> data[0] = 10
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    data[0] = 10
TypeError: 'tuple' object does not support item assignment
>>> data = list(data)
>>> data
[2, 3, 4, 6, 7]
>>> data[0] = 10
>>> data
[10, 3, 4, 6, 7]
>>> data = tuple(data)
>>> data
(10, 3, 4, 6, 7)
>>> emp = {'id':1,'name':'Ram','age':30,'sal':34000}
>>> emp[0]
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    emp[0]
KeyError: 0
>>> emp['name']
'Ram'
>>> emp.keys()
dict_keys(['id', 'name', 'age', 'sal'])
>>> emp.values()
dict_values([1, 'Ram', 30, 34000])
>>> emp.items()
dict_items([('id', 1), ('name', 'Ram'), ('age', 30), ('sal', 34000)])
>>> emp['company'] = 'TCS'
>>> emp
{'id': 1, 'name': 'Ram', 'age': 30, 'sal': 34000, 'company': 'TCS'}
>>> employees = {'id':[1,2,3,4,5],'name':['Ram','Shyam','Ajay','Mohan','Gopal'],'company':['TCS','HCL','TCS','HCL','HCL']}
>>> employees
{'id': [1, 2, 3, 4, 5], 'name': ['Ram', 'Shyam', 'Ajay', 'Mohan', 'Gopal'], 'company': ['TCS', 'HCL', 'TCS', 'HCL', 'HCL']}
>>> employees['id']
[1, 2, 3, 4, 5]
>>> employees['name']
['Ram', 'Shyam', 'Ajay', 'Mohan', 'Gopal']
>>> employees['id'][0]
1
>>> employees['name'][0]
'Ram'
>>> employees['company'][0]
'TCS'
>>> for data in employees:
	print(data)

	
id
name
company
>>> employees['id'][0]
1
>>> employees['id'][1]
2
>>> employees['id'][2]
3
>>> employees['id'][3]
4
>>> for j in range(len(employees[0])):
	print(employees['id'][i], employees['name'][i], employees['company'][i])

	
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    for j in range(len(employees[0])):
KeyError: 0
>>> for i in range(len(employees['id'])):
	print(employees['id'][i], employees['name'][i], employees['company'][i])

	
1 Ram TCS
2 Shyam HCL
3 Ajay TCS
4 Mohan HCL
5 Gopal HCL
>>> 
