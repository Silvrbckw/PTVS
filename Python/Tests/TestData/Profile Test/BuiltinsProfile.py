import time
import marshal
import array

def f():
	a = 'abc'
	x = array.array('b')
	for _ in range(10000):
		a.startswith('a')		# instance method, in __builtin__ 
		isinstance('', str)		# static method, in __builtin__
		x.tostring()			# instance method, in module
		marshal.dumps(a)		# static method, in module


f()