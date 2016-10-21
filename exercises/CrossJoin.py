#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring

# ------------
# CrossJoin.py
# ------------

# http://en.wikipedia.org/wiki/Cartesian_product

def cross_join_yield (r, s) :
    for u in r :
        for v in s :
            yield dict(u, **v)

def cross_join_generator (r, s) :
    return (dict(u, **v) for u in r for v in s)
