#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = function-redefined
# pylint: disable = invalid-name
# pylint: disable = missing-docstring
# pylint: disable = no-name-in-module
# pylint: disable = too-few-public-methods
# pylint: disable = redefined-outer-name
# pylint: disable = redefined-variable-type

# ------------
# Callables.py
# ------------

from functools import reduce
from types     import FunctionType, MethodType

print("Callables.py")

def my_function (i, j) :
    return i + j

f = my_function

assert isinstance(my_function, FunctionType)
assert isinstance(f,           FunctionType)

assert hasattr(my_function, "__call__")
assert hasattr(f,           "__call__")

assert my_function(2, 3) == 5
assert           f(2, 3) == 5

assert reduce(my_function, [2, 3, 4], 0) == 9
assert reduce(f,           [2, 3, 4], 0) == 9



f = lambda i, j : i + j

assert isinstance(lambda i, j : i + j, FunctionType)
assert isinstance(f,                   FunctionType)

assert hasattr(lambda i, j : i + j, "__call__")
assert hasattr(f,                   "__call__")

assert (lambda i, j : i + j)(2, 3) == 5
assert                     f(2, 3) == 5

assert reduce(lambda i, j : i + j, [2, 3, 4], 0) == 9
assert reduce(f,                   [2, 3, 4], 0) == 9



def my_lambda () :
    return lambda i, j : i + j

f = my_lambda()

assert isinstance(my_lambda(), FunctionType)
assert isinstance(f,           FunctionType)

assert hasattr(my_lambda(), "__call__")
assert hasattr(f,           "__call__")

assert my_lambda()(2, 3) == 5
assert           f(2, 3) == 5

assert reduce(my_lambda(), [2, 3, 4], 0) == 9
assert reduce(f,           [2, 3, 4], 0) == 9



i = 2
f = lambda j : i + j

assert isinstance(lambda j : i + j, FunctionType)
assert isinstance(f,                FunctionType)

assert hasattr(lambda j : i + j, "__call__")
assert hasattr(f,                "__call__")

assert (lambda j : i + j)(3) == 5
assert                  f(3) == 5

assert list(map(lambda j : i + j, [2, 3, 4])) == [4, 5, 6]
assert list(map(f,                [2, 3, 4])) == [4, 5, 6]



def my_closure (j) :
    return lambda i : i + j

assert isinstance(my_closure(2), FunctionType)
assert isinstance(f,             FunctionType)

assert hasattr(my_closure(2), "__call__")
assert hasattr(f,             "__call__")

assert my_closure(2)(3) == 5
assert             f(3) == 5

assert list(map(my_closure(2), [2, 3, 4])) == [4, 5, 6]
assert list(map(f,             [2, 3, 4])) == [4, 5, 6]



class A (object) :
    def __init__ (self, j) :
        self.j = j

    def my_method (self, i) :
        return i + self.j

x = A(2)
assert isinstance(x, A)

f = x.my_method

assert isinstance(x.my_method, MethodType)
assert isinstance(f,           MethodType)

assert x.my_method(3) == 5
assert f(3)           == 5

assert list(map(x.my_method, [2, 3, 4])) == [4, 5, 6]
assert list(map(f,           [2, 3, 4])) == [4, 5, 6]



f = A.my_method

assert isinstance(A.my_method, FunctionType)
assert isinstance(f,           FunctionType)

assert A.my_method(x, 3) == 5
assert           f(x, 3) == 5



class A (object) :
    def __init__ (self, j) :
        self.j = j

    def __call__ (self, i) :
        return i + self.j

f = A(2)
assert isinstance(f, A)

assert hasattr(A(2), "__call__")
assert hasattr(f,    "__call__")

assert A(2)(3) == 5
assert    f(3) == 5

print("Done.")
