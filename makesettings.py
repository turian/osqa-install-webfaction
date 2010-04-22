#!/usr/bin/python

from globals import *
import os.path

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
'APP_URL': "http://%s" % FULLDOMAINNAME,
}

import re
for key in values:
    settings_txt = re.sub("\\b%s\\b\\s*=\\s*.*" % key, "%s = '%s'" % (key, values[key]), settings_txt)
print settings_txt
