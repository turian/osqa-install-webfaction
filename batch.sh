#!/bin/sh
rm moreglobals.py*
./install-webfaction-cpanel.py && eval $(./makeenv.py ) && ./getsource.sh && ./modifysettings.py && ./configurebackup.pl && ./modifycron.py && ./createdb.sh
./modifyhttpdconf.py && ./modifywsgi.py && ./startapache.sh
chmod go-rwx globals.py* moreglobals.py* && cp globals.py moreglobals.py $OSQA_WEBAPPDIR ; chmod go-rwx $OSQA_WEBAPPDIR/globals.py $OSQA_WEBAPPDIR/moreglobals.py
