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
#"multi_award_badges": "4,19,34,49 * * * *", # Four times an hour
#"once_award_badges": "14,29,44,59 * * * *", # Four times an hour
}

outtxt = ""
outtxt += "echo '0 4 * * *\t\t%s';" % (os.path.join(os.environ["HOME"], "backup/backup-%s-database.pl" % APPNAME))

for name in names:
    cronfilename = os.path.join(PROJECTDIR, "cron/%s" % name)
    print >> sys.stderr, "Writing to %s" % cronfilename
    open(cronfilename, "wt").write(crontxt % (ENVDIR, PROJECTDIR, "send_email_alerts"))
#    outtxt += "%s\t\t%s\n" % (names[name], cronfilename)
    outtxt += "echo '%s\t\t%s'; " % (names[name], cronfilename)

#print >> sys.stderr, "Please run 'crontab -e' and add the following lines"

# Backup the crontab
cmd = "crontab -l > crontab.backup.`date +'%F-%T'`"
print cmd
os.system(cmd)

cmd = "(crontab -l ; echo; %s) | crontab -" % outtxt
print cmd
os.system(cmd)
