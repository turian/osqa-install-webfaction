#!/bin/sh
rm moreglobals.py*
./install-webfaction-cpanel.py && install-webfaction-cpanel-awstats.py && eval $(./makeenv.py ) && ./configureawstats.sh && ./getsource.sh && ./modifysettings.py && ./configurebackup.pl && ./modifycron.py && ./createdb.sh
./modifyhttpdconf.py && ./modifywsgi.py && ./startapache.sh
chmod go-rwx globals.py* moreglobals.py* && cp globals.py moreglobals.py $OSQA_WEBAPPDIR ; chmod go-rwx $OSQA_WEBAPPDIR/globals.py $OSQA_WEBAPPDIR/moreglobals.py
