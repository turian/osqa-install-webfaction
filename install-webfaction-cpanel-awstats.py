#!/usr/bin/env python

from globals import *
from moreglobals import *
import sys

from cpanel import try_remove, force_create

import xmlrpclib 
server = xmlrpclib.ServerProxy('https://api.webfaction.com/') 
session_id, account = server.login(USERNAME, PASSWORD)
#print >> sys.stderr, repr(session_id)
#print >> sys.stderr, repr(account)
#{'username': 'test5', 'home': '/home2', 'id': 237} 

#for i in server.list_emails(session_id):
#    print >> sys.stderr, i

r = force_create(server, session_id, AWSTATS_APPNAME, "app", "create_app", "delete_app", "list_apps", ['awstats68', False, WEBSITENAME])

if SERVERIP is None:
    SERVERIP = server.list_websites(session_id)[0]["ip"]
    print >> sys.stderr, "No SERVERIP given. Using %s" % SERVERIP
r = force_create(server, session_id, WEBSITENAME, "website", "create_website", "delete_website", "list_websites",  [SERVERIP, False, [FULLDOMAINNAME], [APPNAME, URLPATH], [AWSTATS_APPNAME, AWSTATS_URLPATH]])
