#!/bin/sh

AWDIR="$HOME/webapps/$OSQA_AWSTATS_APPNAME"
CONFFILE="$AWDIR/cgi-bin/awstats.conf"
perl -i -pe 's/DNSLookup=2/DNSLookup=1/g;' $CONFFILE;
perl -i -pe 's/#LoadPlugin="hashfiles"/LoadPlugin="hashfiles"/g;' $CONFFILE;
perl -i -pe "s/SiteDomain=.*/SiteDomain=\"$OSQA_FULLDOMAINNAME\"/g;" $CONFFILE;
perl -i -pe "s/HostAliases=.*/HostAliases=\"localhost 127.0.0.1 REGEX[$OSQA_FULLDOMAINNAME_dotsfixed]\"/g;" $CONFFILE;
perl -i -pe "s/SkipHosts=.*/SkipHosts=\"193.164.138.35\"/g;" $CONFFILE;
perl -i -pe "s/SkipFiles=.*/SkipFiles=\"REGEX[^\\/awstats] REGEX[^$OSQA_URLPATH_RELATEDQUESTIONS_slashfixed]\"/g;" $CONFFILE;
#perl -i -pe "s/SkipFiles=.*/REGEX\[\^$OSQA_URLPATH_RELATEDQUESTIONS\]\"/g;" $CONFFILE;
#perl -i -pe "s/SkipFiles=.*/$OSQA_URLPATH_RELATEDQUESTIONS_slashfixed/g;" $CONFFILE;
perl -i -pe 's/CreateDirDataIfNotExists=0/CreateDirDataIfNotExists=1/g' $CONFFILE;
perl -i -pe 's/ArchiveLogRecords=0/ArchiveLogRecords=1/g' $CONFFILE;
perl -i -pe 's/KeepBackupOfHistoricFiles=0/KeepBackupOfHistoricFiles=1/g' $CONFFILE;

cd $AWDIR ;
perl -i -pe 's/\.1/.*/g;' ./update_awstats.sh
./update_awstats.sh
