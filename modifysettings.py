#!/usr/bin/python

from globals import *
import os.path
import sys

settings_txt = open(os.path.join(PROJECTDIR, "settings_local.py.dist")).read()
#print settings_txt

values = {
'DATABASE_ENGINE': 'mysql',
'DATABASE_NAME': DATABASENAME,
'DATABASE_USER': DATABASENAME,
'DATABASE_PASSWORD': DATABASEPASSWORD,
'EMAIL_HOST': 'smtp.webfaction.com',
'EMAIL_HOST_USER': MAILBOXUSERNAME,
'EMAIL_HOST_PASSWORD': MAILBOXPASSWORD,
'EMAIL_PORT': '25',
'DEFAULT_FROM_EMAIL': EMAILADDRESS,
'SERVER_EMAIL': EMAILADDRESS,
'CONTACT_EMAIL': EMAILADDRESS,
'APP_URL': "http://%s" % FULLURL,
}

import re
for key in values:
    regex = "\\b%s\\b\\s*=\\s*.*" % key
    newstr = "%s = '%s'" % (key, values[key])
    if not re.search(regex, settings_txt):
        print >> sys.stderr, "Could not find setting for %s, prepending" % key
        settings_txt = "%s\n%s" % (newstr, settings_txt)
    else:
        settings_txt = re.sub(regex, newstr, settings_txt)
print >> sys.stderr, "Writing to %s" % os.path.join(PROJECTDIR, "settings_local.py")
open(os.path.join(PROJECTDIR, "settings_local.py"), "wt").write(settings_txt)
