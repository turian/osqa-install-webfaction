#!/bin/sh

cd $OSQA_PROJECTDIR
source $OSQA_ENVDIR/bin/activate
echo "Write the following:"
echo "yes"; echo $OSQA_ADMINUSERNAME ; echo $OSQA_EMAILADDRESS ; echo $OSQA_ADMINPASSWORD ; echo $OSQA_ADMINPASSWORD
python manage.py syncdb

#(echo "yes"; echo $OSQA_ADMINUSERNAME ; echo $OSQA_EMAILADDRESS ; echo $OSQA_ADMINPASSWORD ; echo $OSQA_ADMINPASSWORD) | python manage.py syncdb

chmod +x ./cron/send_email_alerts ./cron/multi_award_badges ./cron/once_award_badges
# The following are just to test the database out
./cron/multi_award_badges
./cron/once_award_badges
