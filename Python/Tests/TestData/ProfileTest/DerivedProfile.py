import time

class C(object):
	def f(self):
		for _ in range(10000):
			time.sleep(0)

class D(C): pass
        
a = D()        
a.f()
