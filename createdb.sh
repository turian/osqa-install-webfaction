#!/bin/sh

cd $OSQA_PROJECTDIR
source $OSQA_ENVDIR/bin/activate
print "Write the following:"
print "yes"
print ADMINUSERNAME
print EMAILADDRESS
print ADMINPASSWORD
print ADMINPASSWORD

python manage.py syncdb

# The following are just to test the database out
./cron/multi_award_badges
./cron/once_award_badges
