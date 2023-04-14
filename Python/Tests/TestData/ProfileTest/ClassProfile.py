import time

class C(object):
	def f(self):
		for _ in range(10000):
			time.sleep(0)

a = C()
a.f()