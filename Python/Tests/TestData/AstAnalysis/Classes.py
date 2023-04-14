class C1:
    """C1"""
    pass

class C2(object): pass
class C3(C2): pass
class C4(C1, C2, C3): pass
C5 = C1

class D: pass


class F1:

    class F2: pass


    class F3:
        class F4: pass

    F6 = C1

def f():
    class X: pass
