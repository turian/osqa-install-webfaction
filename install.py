#!/usr/bin/env python

from globals import *

import xmlrpclib 
server = xmlrpclib.ServerProxy('https://api.webfaction.com/') 
session_id, account = server.login(USERNAME, PASSWORD)
#print repr(session_id)
#print repr(account)
#{'username': 'test5', 'home': '/home2', 'id': 237} 

#for i in server.list_emails(session_id):
#    print i


def force_create(server, session_id, name, type, create_thing, delete_thing, list_thing, create_parameters=[], namename="name", delete_extra_params=[]):
    """
    Force the creation of something using the webfaction API.
    """
    print tuple([repr(s) for s in [server, session_id, name, type, create_thing, delete_thing, list_thing, create_parameters]])
    print "force_create(server=%s, session_id=%s, name=%s, type=%s, create_thing=%s, delete_thing=%s, list_thing=%s, create_parameters=%s)" % tuple([repr(s) for s in [server, session_id, name, type, create_thing, delete_thing, list_thing, create_parameters]])
    # See if the something already exists.
    r = server.__getattr__(list_thing)(session_id)
    to_delete = False
    for i in r:
#        print i
        if i[namename] == name:
            to_delete = True
            break
    
    # If the something already exists, remove it before adding it
    if to_delete:
        print "%s %s already exists. Removing..." % (type, name)
        r = server.__getattr__(delete_thing)(*([session_id, name] + delete_extra_params))
        print "server.%s: %s" % (delete_thing, r)
    
    # Create the something
    r = server.__getattr__(create_thing)(*([session_id, name] + create_parameters))
    print "server.%s: %s" % (create_thing, r)
    return r


r = force_create(server, session_id, DOMAINNAME, "domain", "create_domain", "delete_domain", "list_domains", namename="domain")

r = force_create(server, session_id, APPNAME, "app", "create_app", "delete_app", "list_apps", ['mod_wsgi25_25', False, ''])
PORT = r["port"]

if SERVERIP is None:
    SERVERIP = server.list_websites(session_id)[0]["ip"]
    print "No SERVERIP given. Using %s" % SERVERIP
# TODO: Add https here
# TODO: Add subdomains www and stats here
# TODO: Add path location of application here
r = force_create(server, session_id, WEBSITENAME, "website", "create_website", "delete_website", "list_websites",  [SERVERIP, False, [DOMAINNAME], [APPNAME, "/"]])

if DATABASEPASSWORD is None:
    import randompassword
    DATABASEPASSWORD = randompassword.GenPasswd2()
    print "No DATABASEPASSWORD given. Using %s" % DATABASEPASSWORD
r = force_create(server, session_id, DATABASENAME, "db", "create_db", "delete_db", "list_dbs", ["mysql", DATABASEPASSWORD], delete_extra_params=["mysql"])

# TODO: Add a static media server

if MAILBOXPASSWORD is None:
    import randompassword
    MAILBOXPASSWORD = randompassword.GenPasswd2()
    print "No MAILBOXPASSWORD given. Using %s" % MAILBOXPASSWORD
r = force_create(server, session_id, MAILBOXUSERNAME, "mailbox", "create_mailbox", "delete_mailbox", "list_mailboxes", [False, False, '', False, ''], namename='mailbox')
r = server.change_mailbox_password(session_id, MAILBOXUSERNAME, MAILBOXPASSWORD)
print "server.change_mailbox_password: %s" % r


TARGETS = '%s,%s' % (MAILBOXUSERNAME, YOUREMAIL)
r = force_create(server, session_id, EMAILADDRESS, "email", "create_email", "delete_email", "list_emails", [TARGETS], namename='email_address')
