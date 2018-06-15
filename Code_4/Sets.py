Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> s1 = {2,3,4,5,7,81,2,4,56,34}
>>> s2 = {4,6,7,9,9,43,2,5,67}
>>> s1
{2, 3, 4, 5, 34, 7, 81, 56}
>>> s2
{2, 67, 4, 5, 6, 7, 9, 43}
>>> s1 & s2
{2, 4, 5, 7}
>>> s1.intersection(s2)
{2, 4, 5, 7}
>>> s1 | s2
{2, 3, 4, 5, 34, 7, 67, 6, 9, 43, 81, 56}
>>> s1.union(s2)
{2, 3, 4, 5, 34, 7, 67, 6, 9, 43, 81, 56}
>>> test_1 = "Hello this is python programming and python is used for machine learning"
>>> test_2 = "hello world python is a general purpose programming and also used for machine learning and game development"
>>> token_1 = test_1.split()
>>> token_1
['Hello', 'this', 'is', 'python', 'programming', 'and', 'python', 'is', 'used', 'for', 'machine', 'learning']
>>> stopwords = ['is','am','are','this','and','for','a','also']
>>> t1 = set(token_1)
>>> t1
{'is', 'used', 'learning', 'programming', 'machine', 'python', 'Hello', 'and', 'for', 'this'}
>>> stopwords = set(stopwords)
>>> stopwords.difference(t1)
{'a', 'am', 'also', 'are'}
>>> t1.difference(stopwords)
{'used', 'learning', 'programming', 'machine', 'python', 'Hello'}
>>> set_1 = t1.difference(stopwords)
>>> token_2 = test_2.split()
>>> t2 = set(token_2)
>>> set_2 = t2.difference(stopwords)
>>> set_1
{'used', 'learning', 'programming', 'machine', 'python', 'Hello'}
>>> set_2
{'used', 'purpose', 'learning', 'programming', 'general', 'machine', 'world', 'python', 'game', 'hello', 'development'}
>>> set_1 & set_2
{'used', 'learning', 'programming', 'machine', 'python'}
>>> len(set_1 & set_2) / len(set_1 | set_2)
0.4166666666666667
>>> 
