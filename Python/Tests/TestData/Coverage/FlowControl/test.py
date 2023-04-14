print('covered')
print('covered')

while False:
    print('uncovered')

for _ in []:
    print('uncovered')

for _ in [1,2,3]:
    print('covered')

try:
    raise Exception('covered')
except:
    print('covered')


try:
    raise Exception('covered')
except StopIteration:
    print('uncovered')
except:
    print('covered')
    
def f():
    return 42
    
a = f()


for _ in [1,2,3]:
    break
for _ in [1,2,3]:
    continue
for i in [1,2,3]:
    if not i:
        break
    print('covered')


for i in [1,2,3]:
    if not i:
        continue
    print('covered')
    
