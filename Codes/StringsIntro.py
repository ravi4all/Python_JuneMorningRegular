Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a = 'hello'
>>> a = "hello"
>>> a = 'I don't understand this'
SyntaxError: invalid syntax
>>> a = "I don't understand this"
>>> a
"I don't understand this"
>>> print(a)
I don't understand this
>>> a = "Hello "World""
SyntaxError: invalid syntax
>>> a = 'Hello "World"'
>>> print(a)
Hello "World"
>>> a
'Hello "World"'
>>> a = 'Hello World'
>>> len(a)
11
>>> a[0]
'H'
>>> a[4]
'o'
>>> a[10]
'd'
>>> a[-1]
'd'
>>> a[0:4]
'Hell'
>>> a[0:5]
'Hello'
>>> a[:]
'Hello World'
>>> a[0:]
'Hello World'
>>> a[:8]
'Hello Wo'
>>> a = "Hello world this is python"
>>> len(a)
26
>>> a[0:20:2]
'Hlowrdti s'
>>> a = "python"
>>> a[::-1]
'nohtyp'
>>> a[0] = 'x'
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    a[0] = 'x'
TypeError: 'str' object does not support item assignment
>>> 
