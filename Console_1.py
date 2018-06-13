Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> print("hello world")
hello world
>>> a = 10
>>> b = 12.55
>>> c = 'hello'
>>> d = True
>>> type(a)
<class 'int'>
>>> type(b)
<class 'float'>
>>> type(c)
<class 'str'>
>>> type(d)
<class 'bool'>
>>> import keywords
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    import keywords
ModuleNotFoundError: No module named 'keywords'
>>> import keyword
>>> keyword.kwlist()
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    keyword.kwlist()
TypeError: 'list' object is not callable
>>> keyword.kwlist
['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
>>> a
10
>>> b
12.55
>>> s = a + b
>>> z = a - b
>>> k = a * b
>>> d = a / b
>>> s
22.55
>>> k
125.5
>>> d
0.796812749003984
>>> z
-2.5500000000000007
>>> a = 'hello'
>>> a * 5
'hellohellohellohellohello'
>>> 
