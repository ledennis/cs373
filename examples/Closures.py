#!/usr/bin/env python3

# -----------
# Closures.py
# -----------

print("Closures.py")

x = A()
assert x.get() == []
x.add(2)
assert x.get() == [2]
x.add(3)
assert x.get() == [2, 3]
x.a += [4]                   # violation of interface
assert x.get() == [2, 3, 4]
x.a = None                   # violation of interface
assert x.get() == None
assert "a"     in x.__dict__
del x.a                      # violation of interface
assert "a" not in x.__dict__

def A () :
    a = []

    class B :
        def get (self) :
            return a

        def add (self, v) :
            a.append(v)

    return B()

x = A()
assert x.get() == []
x.add(2)
assert x.get() == [2]
x.add(3)
assert x.get() == [2, 3]
#x.a += [4]                  # AttributeError: 'A' object has no attribute 'a'
assert x.get() == [2, 3]
#del x.a                     # AttributeError: a
assert "a" not in x.__dict__
x.a = None                   # ?
assert "a"     in x.__dict__
assert x.get() == [2, 3]

print("Done.")
