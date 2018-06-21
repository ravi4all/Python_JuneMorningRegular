Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import os
>>> os.chdir(r'C:\Users\asus\Documents\Data\DataTransfer\BMPL_Batches\June_2018\Python_MorningRegular\FileHandlingCode\Read_fileBatch')
>>> os.walk
<function walk at 0x0000016B20D32C80>
>>> os.walk()
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    os.walk()
TypeError: walk() missing 1 required positional argument: 'top'
>>> path = '/files'
>>> os.walk(path)
<generator object walk at 0x0000016B232AEDB0>
>>> for x in os.walk(path):
	print(x)

	
>>> for x in os.walk('\files'):
	print(x)

	
>>> path = r'C:\Users\asus\Documents\Data\DataTransfer\BMPL_Batches\June_2018\Python_MorningRegular\FileHandlingCode\Read_fileBatch\'
SyntaxError: EOL while scanning string literal
>>> path = r'C:\Users\asus\Documents\Data\DataTransfer\BMPL_Batches\June_2018\Python_MorningRegular\FileHandlingCode\Read_fileBatch'
>>> for x in os.walk(path):
	print(x)

	
('C:\\Users\\asus\\Documents\\Data\\DataTransfer\\BMPL_Batches\\June_2018\\Python_MorningRegular\\FileHandlingCode\\Read_fileBatch', ['files'], [])
('C:\\Users\\asus\\Documents\\Data\\DataTransfer\\BMPL_Batches\\June_2018\\Python_MorningRegular\\FileHandlingCode\\Read_fileBatch\\files', [], ['00001.7c53336b37003a9286aba55d2945844c', '00002.9c4069e25e1ef370c078db7ee85ff9ac', '00003.860e3c3cee1b42ead714c5c874fe25f7', '00004.864220c5b6930b209cc287c361c99af1', '00005.bf27cdeaf0b8c4647ecd61b1d09da613', '00006.253ea2f9a9cc36fa0b1129b04b806608', '00007.37a8af848caae585af4fe35779656d55', '00008.5891548d921601906337dcf1ed8543cb', '00009.371eca25b0169ce5cb4f71d3e07b9e2d', '00010.145d22c053c1a0c410242e46c01635b3'])
>>> path = r'C:\Users\asus\Documents\Data\DataTransfer\BMPL_Batches\June_2018\Python_MorningRegular\FileHandlingCode\Read_fileBatch\files'
>>> for x in os.walk(path):
	print(x)

	
('C:\\Users\\asus\\Documents\\Data\\DataTransfer\\BMPL_Batches\\June_2018\\Python_MorningRegular\\FileHandlingCode\\Read_fileBatch\\files', [], ['00001.7c53336b37003a9286aba55d2945844c', '00002.9c4069e25e1ef370c078db7ee85ff9ac', '00003.860e3c3cee1b42ead714c5c874fe25f7', '00004.864220c5b6930b209cc287c361c99af1', '00005.bf27cdeaf0b8c4647ecd61b1d09da613', '00006.253ea2f9a9cc36fa0b1129b04b806608', '00007.37a8af848caae585af4fe35779656d55', '00008.5891548d921601906337dcf1ed8543cb', '00009.371eca25b0169ce5cb4f71d3e07b9e2d', '00010.145d22c053c1a0c410242e46c01635b3'])
>>> for root, folder, file in os.walk(path):
	print(file)

	
['00001.7c53336b37003a9286aba55d2945844c', '00002.9c4069e25e1ef370c078db7ee85ff9ac', '00003.860e3c3cee1b42ead714c5c874fe25f7', '00004.864220c5b6930b209cc287c361c99af1', '00005.bf27cdeaf0b8c4647ecd61b1d09da613', '00006.253ea2f9a9cc36fa0b1129b04b806608', '00007.37a8af848caae585af4fe35779656d55', '00008.5891548d921601906337dcf1ed8543cb', '00009.371eca25b0169ce5cb4f71d3e07b9e2d', '00010.145d22c053c1a0c410242e46c01635b3']
>>> s = "hello"
>>> s.join('world')
'whelloohellorhellolhellod'
>>> s.join(' ')
' '
>>> s
'hello'
>>> s.join(',')
','
>>> ' '.join(s)
'h e l l o'
>>> 
