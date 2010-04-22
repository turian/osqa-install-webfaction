#!/usr/bin/python

from globals import *
import os.path
import sys

wsgitxt = '''
import os
import sys

# redirect sys.stdout to sys.stderr for bad libraries like geopy that uses
# print statements for optional import exceptions.
sys.stdout = sys.stderr

from os.path import abspath, dirname, join
from site import addsitedir

# add the virtual environment site-packages to the path
from site import addsitedir
addsitedir('%s')

sys.path.insert(0, abspath(join(dirname(__file__), "../")))
sys.path.append(abspath(dirname(__file__)))

from django.conf import settings
os.environ["DJANGO_SETTINGS_MODULE"] = "osqa.settings"

#print sys.path

from django.core.handlers.wsgi import WSGIHandler
application = WSGIHandler()
'''

wsgifilename = os.path.join(PROJECTDIR, "osqa.wsgi")
print >> sys.stderr, "Writing to %s" % wsgifilename
open(wsgifilename, "wt").write(wsgitxt % (os.path.join(ENVDIR, "lib/python2.5/site-packages")))
