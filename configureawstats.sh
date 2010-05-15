#!/bin/sh

AWDIR="$HOME/webapps/$OSQA_AWSTATS_APPNAME"
CONFFILE="$AWDIR/cgi-bin/awstats.conf"
perl -i -pe 's/DNSLookup=2/DNSLookup=1/g;' $CONFFILE;
perl -i -pe 's/#LoadPlugin="hashfiles"/LoadPlugin="hashfiles"/g;' $CONFFILE;
perl -i -pe "s/SiteDomain=.*/SiteDomain=\"$OSQA_FULLDOMAINNAME\"/g;" $CONFFILE;
perl -i -pe 's/SkipFiles=.*/SkipFiles="REGEX[^\\\/awstats]"/g;' $CONFFILE;

cd $AWDIR ;
perl -i -pe 's/\.1/.*/g;' ./update_awstats.sh
./update_awstats.sh
