Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> address = ('Delhi','Pune','Noida')
>>> for addr in address:
	print(addr)

	
Delhi
Pune
Noida
>>> for i in range(len(address)):
	print(i)

	
0
1
2
>>> for i in range(len(address)):
	print(i,address[i])

	
0 Delhi
1 Pune
2 Noida
>>> for i in range(len(address)):
	print(i+1,address[i])

	
1 Delhi
2 Pune
3 Noida
>>> for i, addr in enumerate(address):
	print(i,addr)

	
0 Delhi
1 Pune
2 Noida
>>> for i, addr in enumerate(address):
	print(i+1,addr)

	
1 Delhi
2 Pune
3 Noida
>>> id = [1,2,3,4,5,6]
>>> name = ['Ram','Shyam','John','Mike','Mohan','Gopal']
>>> comapny = ['HCL','TCS','Wipro','HCL','TCS','IBM']
>>> for id,name,company in zip(id,name,company):
	print(id,name,company)

	
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    for id,name,company in zip(id,name,company):
NameError: name 'company' is not defined
>>> for id,name,company in zip(id,name,comapny):
	print(id,name,company)

	
1 Ram HCL
2 Shyam TCS
3 John Wipro
4 Mike HCL
5 Mohan TCS
6 Gopal IBM
>>> 
