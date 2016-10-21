#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring

# ----------
# Project.py
# ----------

# http://en.wikipedia.org/wiki/Projection_(relational_algebra)

def project_yield (r, *t) :
    for d in r :
        x = {}
        for a in t :
            if a in d :
                x[a] = d[a]
        yield x

def project_comprehension (r, *t) :
    for d in r :
        yield {a : d[a] for a in t if a in d}

def project_generator (r, *t) :
    return ({a : d[a] for a in t if a in d} for d in r)
