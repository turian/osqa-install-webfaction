#!/usr/bin/python

import os
import globals

for var in dir(globals):
    if var[0] == "_": continue
    val = globals.__dict__[var]
    if val is None: val = "None"
    print "export OSQA_%s=%s" % (var, val)
