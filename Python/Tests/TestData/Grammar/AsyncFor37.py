def test1():
    return iter([])

def test2():
    return (fob for fob in [] if await fob)
