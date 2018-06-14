Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> data = [12,3,4,5,'hello','hi',10.5,11.5,True]
>>> data[0]
12
>>> data[5]
'hi'
>>> data[-1]
True
>>> data[0:5]
[12, 3, 4, 5, 'hello']
>>> data[:]
[12, 3, 4, 5, 'hello', 'hi', 10.5, 11.5, True]
>>> data[0] = 'python'
>>> data
['python', 3, 4, 5, 'hello', 'hi', 10.5, 11.5, True]
>>> dir(list)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> data = []
>>> data.append(5)
>>> data
[5]
>>> data.append(10)
>>> data
[5, 10]
>>> data = []
>>> for i in range(1,11):
	data.append(5*i)

	
>>> data
[5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
>>> data.pop()
50
>>> data
[5, 10, 15, 20, 25, 30, 35, 40, 45]
>>> data.pop(5)
30
>>> data.remove(2)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    data.remove(2)
ValueError: list.remove(x): x not in list
>>> data.remove(20)
>>> data
[5, 10, 15, 25, 35, 40, 45]
>>> data.count(5)
1
>>> data_2 = [10,20,30,40,50,60]
>>> data.extend(data_2)
>>> data
[5, 10, 15, 25, 35, 40, 45, 10, 20, 30, 40, 50, 60]
>>> data.insert(3,20)
>>> data
[5, 10, 15, 20, 25, 35, 40, 45, 10, 20, 30, 40, 50, 60]
>>> data = [12,34,67,11,15,18,92,17,56]
>>> sorted(data)
[11, 12, 15, 17, 18, 34, 56, 67, 92]
>>> sorted(data, reverse = True)
[92, 67, 56, 34, 18, 17, 15, 12, 11]
>>> data
[12, 34, 67, 11, 15, 18, 92, 17, 56]
>>> data.sort()
>>> data
[11, 12, 15, 17, 18, 34, 56, 67, 92]
>>> data.sort(reverse = True)
>>> data
[92, 67, 56, 34, 18, 17, 15, 12, 11]
>>> 
