#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring
# pylint: disable = no-member
# pylint: disable = protected-access

# ----------
# Classes.py
# ----------

print("Classes.py")

class A :
    __cv = 0 # private

    def __init__ (self) :
        A.__cv    += 1
        self.__iv  = 0 # private
#       cm()           # NameError: name 'cm' is not defined
        A.cm()
#       sm()           # NameError: name 'sm' is not defined
        A.sm()
#       im()           # NameError: name 'im' is not defined
        self.im()

    @classmethod
    def cm (cls) :     # cls might be bound to a child type
        A.__cv    += 1
        cls.__cv  += 1
#       sm()           # NameError: name 'sm' is not defined
        A.sm()
        cls.sm()
#       self.__iv += 1 # NameError: name 'self' is not defined
#       self.im()      # NameError: name 'self' is not defined

    @staticmethod
    def sm () :
        A.__cv    += 1
#       cm()           # NameError: name 'cm' is not defined
#       A.cm()
#       self.__iv += 1 # NameError: global name 'self' is not defined
#       self.im()      # NameError: global name 'self' is not defined

    def im (self) :
        A.__cv    += 1
        self.__iv += 1
#       cm()           # NameError: name 'cm' is not defined
        A.cm()
        self.cm()      # misleading
#       sm()           # NameError: name 'sm' is not defined
        A.sm()
        self.sm()      # misleading

assert A._A__cv == 0 # not so private!

A.cm()
A.sm()
#A.im() # TypeError: im() missing 1 required positional argument: 'self'

x = A()
assert x._A__iv == 1 # not so private!
x.cm()               # misleading
x.sm()               # misleading

x.im()
A.im(x) # methods are really just functions

print("Done.")
