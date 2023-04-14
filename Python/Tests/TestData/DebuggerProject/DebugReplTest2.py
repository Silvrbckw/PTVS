def outer(x):
    outer_val = x * 2
    inner(outer_val)

def inner(y):
    inner_val = y * 5
    innermost(inner_val)

def innermost(z):
    innermost_val = z + 1

global_val = 5
outer(5)
