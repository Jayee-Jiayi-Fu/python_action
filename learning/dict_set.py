# dict
d = {'a' :1, 'b':2, 'c':3}
print(d)
print(d['a'],d.get('c'))
d['d']= 4
print(d)
d.pop('d')
print(d)
print('-------------------')


# set
s =set([1,2,3,2,3])
print(s)
s.add('k')
print(s)
s.remove('k')
print(s)
s2 = set([3,4,5])
print(s & s2)
