#!/usr/bin/env python

from globals import *

import xmlrpclib 
server = xmlrpclib.ServerProxy('https://api.webfaction.com/') 
session_id, account = server.login(USERNAME, PASSWORD)
#print repr(session_id)
#print repr(account)
#{'username': 'test5', 'home': '/home2', 'id': 237} 

# Add the domain
r = server.create_domain(session_id, DOMAINNAME)
print "server.create_domain(%s): %s" % (DOMAINNAME, r)
# TODO: Add www and stats subdomains
#server.create_domain(session_id, DOMAINNAME, "www", "stats")

r = server.create_app(session_id, 'my_joomla_app', 'static', False, '')
