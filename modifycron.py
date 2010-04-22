#!/usr/bin/python

from globals import *
import os.path
import sys

crontxt = '''
#!/bin/sh

WORKON_HOME=%s
PROJECT_ROOT=%s

# activate virtual environment
. $WORKON_HOME/bin/activate

cd $PROJECT_ROOT
python manage.py %s >> $PROJECT_ROOT/log/cron_mail.log 2>&1
'''

names = {
"send_email_alerts": "1 0,12 * * *",    # Twice a day
"multi_award_badges": "4,19,34,49 * * * *", # Four times an hour
"once_award_badges": "14,29,44,59 * * * *", # Four times an hour
}

outtxt = ""

for name in names:
    cronfilename = os.path.join(PROJECTDIR, "cron/%s" % name)
    print >> sys.stderr, "Writing to %s" % cronfilename
    open(cronfilename, "wt").write(crontxt % (ENVDIR, PROJECTDIR, "send_emails"))
    outtxt += "%s\t\t%s\n" % (names[name], cronfilename)

print >> sys.stderr, "Please run 'crontab -e' and add the following lines"
print
print outtxt
