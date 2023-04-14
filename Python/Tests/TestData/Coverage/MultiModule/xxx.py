import foo
import code
import yyy
def f():  x = 1

def g():
    def h():
        return 42

    if True:
        print('hi')
    else:
        print('bye')
    x = 2
    print(h())
    return x
    
def func(a, b, c):
    return a + b + c

class C:
    class D: 
        def __init__(self):
            self.value = None
    
    x = 1
    def __init__(self, value):
        self.value = value
        self.x = C.D()
        
a = C(42)

f()
f()
g()


func(
  1,
  2,
  3
)