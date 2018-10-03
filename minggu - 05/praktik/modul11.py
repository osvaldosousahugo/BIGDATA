Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import reprlib
>>> reprlib.repr(set('suoercalifragilisticexpialidocious'))
"{'a', 'c', 'd', 'e', 'f', 'g', ...}"
>>> 
>>> 
>>> import pprint
>>> t = [[[['black', 'cyan'], 'white', ['green','red']], [['magenta',
							   'yellow'], 'blue']]]
>>> pprint.pprint(t, width=30).
SyntaxError: invalid syntax
>>> pprint.pprint(t, width=30)
[[[['black', 'cyan'],
   'white',
   ['green', 'red']],
  [['magenta', 'yellow'],
   'blue']]]
>>> import textwrap
>>> doc = """the wrap () method is just like fill () except that it returns a list of strings instead of one big string with newlines to separate the wrapped lines."""
>>> print(textwrap.fill(doc, width=40))
the wrap () method is just like fill ()
except that it returns a list of strings
instead of one big string with newlines
to separate the wrapped lines.
>>> import locale
>>> locale.setlocale(locale.LC_ALL, 'English_United States.1252')'English_United States.1252'
SyntaxError: invalid syntax
>>> locale.setlocale(locale.LC_ALL, 'English_United States.1252')
'English_United States.1252'
>>> conv = locale.localeconv()
>>> x = 1234567.8
>>> locale.format("%d", x, grouping=True)

Warning (from warnings module):
  File "__main__", line 1
DeprecationWarning: This method will be removed in a future version of Python. Use 'locale.format_string()' instead.
'1,234,567'
>>> locale.format_string ("%s%.*f", (conv['currency_symbol'],
				     conv['frac_digits'], x), grouping=True)
'$1,234,567.80'
>>> t = Template('Return the $item to $owner.')
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    t = Template('Return the $item to $owner.')
NameError: name 'Template' is not defined
>>> d = dict(item='unladen swallow')
>>> t.substitute(d)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    t.substitute(d)
AttributeError: 'list' object has no attribute 'substitute'
>>> t.safe_substitute(d)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    t.safe_substitute(d)
AttributeError: 'list' object has no attribute 'safe_substitute'
>>> 
>>> import time, os.path
>>> photofiles = ['img_1074.jpg', 'img_1076.jpg', 'img_1077.jpg']
>>> class BatchRename(Template):
	delimiter = '%'

	
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    class BatchRename(Template):
NameError: name 'Template' is not defined
>>> fmt = input('Enter rename style (%d-date %n-seqnum %f-format):  ')
Enter rename style (%d-date %n-seqnum %f-format):  Ashley_%n%f
>>> t = BatchRename(fmt)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    t = BatchRename(fmt)
NameError: name 'BatchRename' is not defined
>>> date = time.strftime('%d%b%y')
>>> for i, filename in enumerate(photofiles):
	base, ext = os.path.splitext(filename
			newname = t.substitute(d=date, n=i, f=ext
					       
SyntaxError: invalid syntax
>>> for i, filename in enumerate(photofiles):
	 base, ext = os.path.splitext(filename
	 newname = t.substitute(d=date, n=i, f=ext
				
SyntaxError: invalid syntax
>>> for i, filename in enumerate(photofiles):
	base, ext = os.path.splitext(filename
	base, ext = os.path.splitext(filename)
				     
SyntaxError: invalid syntax
>>> for i, filename in enumerate(photofiles):
	base, ext = os.path.splitext(filename)
	newname = t.substitute(d=date, n=i, f=ext)
	print('{0} --> {1}'.format(filename, newname))

				     
Traceback (most recent call last):
  File "<pyshell#49>", line 3, in <module>
    newname = t.substitute(d=date, n=i, f=ext)
AttributeError: 'list' object has no attribute 'substitute'
>>> import time, os.path
				     
>>> photofiles = ['img_1074.jpg', 'img_1076.jpg', 'img_1077.jpg']
				     
>>> class BatchRename(Template):
	delimiter = '%'

				     
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    class BatchRename(Template):
NameError: name 'Template' is not defined
>>> fmt = input('Enter rename style (%d-date %n-seqnum %f-format):  ')
				     
Enter rename style (%d-date %n-seqnum %f-format):  Ashley_%n%f
>>> t = BatchRename(fmt)
				     
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    t = BatchRename(fmt)
NameError: name 'BatchRename' is not defined
>>> date = time.strftime('%d%b%y')
				     
>>> for i, filename in enumerate(photofiles):
	base, ext = os.path.splitext(filename)
	newname = t.substitute(d=date, n=i, f=ext)
	print('{0} --> {1}'.format(filename, newname))

				     
Traceback (most recent call last):
  File "<pyshell#62>", line 3, in <module>
    newname = t.substitute(d=date, n=i, f=ext)
AttributeError: 'list' object has no attribute 'substitute'
>>> import struct
				     
>>> with open('myfile.zip', 'rb') as f:
	data = f.read()
start = 0
				     
SyntaxError: invalid syntax
>>> for i in range(3):       # show the first 3 file headers
	start += 14
	fields = struct.unpack('<IIIHH', data[start:start+16])
	crc32, comp_size, uncomp_size, filenamesize, extra_size = fields

				     
Traceback (most recent call last):
  File "<pyshell#71>", line 2, in <module>
    start += 14
NameError: name 'start' is not defined
>>> 
				     
>>> import threading, zipfile
				     
>>> class AsyncZip(threading.Thread):
	def __init__(self, infile, outfile):
	    threading.Thread.__init__(self)
	    self.infile = infile
	    self.outfile = outfile
	def run(self):
	    f = zipfile.ZipFile(self.outfile, 'w', zipfile.ZIP_DEFLATED)
		f.write(self.infile)
				     
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> f.write(self.infile)
				     
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    f.write(self.infile)
NameError: name 'f' is not defined
>>> import threading, zipfile
				     
>>> class AsyncZip(threading.Thread):
	def __init__(self, infile, outfile):
	     threading.Thread.__init__(self)
	     self.infile = infile
	     self.outfile = outfile
	def run(self):
	    f = zipfile.ZipFile(self.outfile, 'w', zipfile.ZIP_DEFLATED)
	    f.write(self.infile)
	    f.close()
	    print('Finished background zip of:', self.infile)
background = AsyncZip('mydata.txt', 'myarchive.zip')
				     
SyntaxError: invalid syntax
>>> background = AsyncZip('mydata.txt', 'myarchive.zip')
				     
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    background = AsyncZip('mydata.txt', 'myarchive.zip')
NameError: name 'AsyncZip' is not defined
>>> background.start()
				     
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    background.start()
NameError: name 'background' is not defined
>>> print('The main program continues to run in foreground.')
				     
The main program continues to run in foreground.
>>> background.join()
				     
Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    background.join()
NameError: name 'background' is not defined
>>> print('Main program waited until background was done.')
				     
Main program waited until background was done.
>>> import logging
				     
>>> logging.debug('Debugging information')
				     
>>> logging.info('Informational message')
				     
>>> logging.warning('Warning:config file %s not found', 'server.conf')
				     
WARNING:root:Warning:config file server.conf not found
>>> logging.error('Error occurred')
				     
ERROR:root:Error occurred
>>> logging.critical('Critical error -- shutting down')
				     
CRITICAL:root:Critical error -- shutting down
>>> 
				     
>>> import weakref, gc
				     
>>> class A:
	def __init__(self, value):
	    self.value = value
	def __repr__(self):
	    return str(self.value)

				     
>>> a = A(10)
				     
>>> d = weakref.WeakValueDictionary()
				     
>>> d['primary'] = a
				     
>>> d['primary']
				     
10
>>>  del a
				     
SyntaxError: unexpected indent
>>> gc.collect()
				     
0
>>> d['primary']
				     
10
>>> 
				     
>>> from array import array
				     
>>> a = array('H', [4000, 10, 700, 22222])
				     
>>> sum(a)
				     
26932
>>> a[1:3]
				     
array('H', [10, 700])
>>> 
				     
>>> from collections import deque
				     
>>> d = deque(["task1", "task2", "task3"])
				     
>>> d.append("task4")
				     
>>> print("Handling", d.popleft())
				     
Handling task1
>>> 
				     
>>> import bisect
				     
>>> scores = [(100, 'perl'), (200, 'tcl'), (400, 'lua'), (500, 'python')]
				     
>>> bisect.insort(scores, (300, 'ruby'))
				     
>>> scores
				     
[(100, 'perl'), (200, 'tcl'), (300, 'ruby'), (400, 'lua'), (500, 'python')]
>>> 
				     
>>> from heapq import heapify, heappop, heappush
				     
>>> data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
				     
>>> heapify(data)
				     
>>> heappush(data, -5)
				     
>>> [heappop(data) for i in range(3)]
				     
[-5, 0, 1]
>>> 
				     
>>> from decimal import *
				     
>>> round(Decimal('0.70') * Decimal('1.05'), 2)
				     
Decimal('0.74')
>>> round(.70 * 1.05, 2)
				     
0.73
>>> 
				     
>>> 
KeyboardInterrupt
>>> Decimal('1.00') % Decimal('.10')
				     
Decimal('0.00')
>>> 1.00 % 0.10
				     
0.09999999999999995
>>> sum([Decimal('0.1')]*10) == Decimal('1.0')
				     
True
>>> sum([0.1]*10) == 1.0
				     
False
>>> 
				     
>>> getcontext().prec = 36
				     
>>> Decimal(1) / Decimal(7)
				     
Decimal('0.142857142857142857142857142857142857')
>>> 
