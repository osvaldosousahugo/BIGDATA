Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 2+2
4
>>> 50-5*6
20
>>> (50-5*6) /4
5.0
>>> 8/5
1.6
>>> 
>>> 
>>> 17/3
5.666666666666667
>>> 17//3
5
>>> 17%3
2
>>> 5*3+2
17
>>> 
>>> 
>>> 5**2
25
>>> 2**7
128
>>> 
>>> 
>>> width = 20
>>> height = 5*9
>>> width * height
900
>>> 
>>> 
>>> n
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    n
NameError: name 'n' is not defined
>>> 4*3.75 -1
14.0
>>> 
>>> 
>>> tax = 12.5 / 100
>>> price = 100.50
>>> price * tax
12.5625
>>> price + _
113.0625
>>> round(_,2)
113.06
>>> 
>>> 
>>> 'spam eggs'
'spam eggs'
>>> doesn\ 't'
SyntaxError: unexpected character after line continuation character
>>> doesn\ 't'
SyntaxError: unexpected character after line continuation character
>>> 'doesn\ 't'
SyntaxError: invalid syntax
>>> 'doesn\ 't' '
SyntaxError: invalid syntax
>>> "doesn't"
"doesn't"
>>> '"Yes," they said.'
'"Yes," they said.'
>>> '"Isn\'t," they said.'
'"Isn\'t," they said.'
>>> 
>>> 
>>> '"Isn\'t," they said.'
'"Isn\'t," they said.'
>>> print('"Isn\'t," they said.')
"Isn't," they said.
>>>  s = 'First line.\nSecond line.'
SyntaxError: unexpected indent
>>> s = 'First line.\nSecond line.'
>>> s
'First line.\nSecond line.'
>>> print(s)
First line.
Second line.
>>> print('C:\some\name')
C:\some
ame
>>> print(r'C:\some\name')
C:\some\name
>>> print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to

>>> 3 * 'un' + 'ium'
'unununium'
>>> 'Py' 'thon'
'Python'
>>> 
>>> 
>>> prefix = 'Py'
>>> 
KeyboardInterrupt
>>> prefix 'thon'
SyntaxError: invalid syntax
>>> prefix = 'Py'
>>> prefix 'thon'
SyntaxError: invalid syntax
>>> prefix + 'thon'
'Python'
>>> word = 'Python'
>>> word[0]
'P'
>>> word[5]
'n'
>>> word[0,3]
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    word[0,3]
TypeError: string indices must be integers
>>> word[-1]
'n'
>>> word[-2]
'o'
>>> word[-6]
'P'
>>> word[0:2]
'Py'
>>> word[0:3]
'Pyt'
>>> word[:2] + word[2:]
'Python'
>>> word[:4] + word[4:]
'Python'
>>> word[:2]
'Py'
>>> word[4:]
'on'
>>> word[-2:]
'on'
>>> word[42]
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    word[42]
IndexError: string index out of range
>>> word[4:42]
'on'
>>> word[42:]
''
>>> word[0] = 'J'
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    word[0] = 'J'
TypeError: 'str' object does not support item assignment
>>> word[2:] = 'py'
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    word[2:] = 'py'
TypeError: 'str' object does not support item assignment
>>> 'J' + word[1:]
'Jython'
>>> word[:2] + 'py'
'Pypy'
>>> s = 'supercalifragilisticexpialidocious'
>>> len(s)
34
>>> 
>>> 
>>> 
>>> squares = [1, 4, 9, 16, 25]
>>> squares
[1, 4, 9, 16, 25]
>>> squares[0]
1
>>> squares[-1]
25
>>> squares[-3:]
[9, 16, 25]
>>> squares[:]
[1, 4, 9, 16, 25]
>>> squares + [36, 49, 64, 81, 100]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
>>> cubes = [1, 8, 27, 65, 125]
>>> 4 ** 3
64
>>> cubes[3] = 64
>>> cubes
[1, 8, 27, 64, 125]
>>> 
KeyboardInterrupt
>>> cubes.append(216)
>>> cubes.append(7 ** 3)
>>> cubes
[1, 8, 27, 64, 125, 216, 343]
>>> 
>>> 
>>> 
>>> letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
>>> letters
['a', 'b', 'c', 'd', 'e', 'f', 'g']
>>> # replace some values
>>> letters[2:5] = ['C', 'D', 'E']
>>> letters
['a', 'b', 'C', 'D', 'E', 'f', 'g']
>>> # now remove them
>>> letters[2:5] = []
>>> letters
['a', 'b', 'f', 'g']
>>> # clear the list by replacing all the elements with an empty list
>>> letters[:] = []
>>> letters
[]
>>> 
>>> 
>>> a = ['a', 'b', 'c']
>>> n = [1, 2, 3]
>>> x = [a, n]
>>> x
[['a', 'b', 'c'], [1, 2, 3]]
>>> x[0]
['a', 'b', 'c']
>>> x[0][1]
'b'
>>> 
>>> 
>>> # Fibonacci series:
>>> # the sum of two elements defines the next
>>> while a < 10:
	print(a)
	a, b = b, a+b

	
Traceback (most recent call last):
  File "<pyshell#129>", line 1, in <module>
    while a < 10:
TypeError: '<' not supported between instances of 'list' and 'int'
>>> a, b = 0, 1
>>> while a < 10:
	print(a)
	a, b = b, a+b

0
1
1
2
3
5
8
>>> 
>>> 
>>> i = 256*256
>>> print('The value of i is', i)
The value of i is 65536
>>> a, b = 0, 1
>>> while a < 1000:
	print(a, end=',')
	a, b = b, a+b

0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,
>>> 
