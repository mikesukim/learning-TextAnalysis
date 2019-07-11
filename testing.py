l = list()
l.append('x')
l.append(10)
l += [1,2,3]
t = tuple()
#for tuple, once its variable is set, can't be modify.
d = dict()
s = set()
#duplicated variable saved once in set.
#Like hashTable
s.add('x')
s.add(10)
s.add(10)
s.discard(100) #Not Error
#s.remove(100) #Error Occured


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person('michael', 40)
p.hatColor = 'red'
