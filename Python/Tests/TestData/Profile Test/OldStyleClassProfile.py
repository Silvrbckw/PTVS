import time

class C:
	def f(self):
		for _ in xrange(10000):
			time.sleep(0)

a = C()
a.f()
