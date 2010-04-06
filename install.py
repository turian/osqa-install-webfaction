#!/usr/bin/env python

from globals import *

import xmlrpclib 
server = xmlrpclib.ServerProxy('https://api.webfaction.com/') 
session_id, account = server.login(USERNAME, PASSWORD)
#print repr(session_id)
#print repr(account)
#{'username': 'test5', 'home': '/home2', 'id': 237} 



# Add the domain
# TODO: See if the domain exists and remove it if it does?
r = server.create_domain(session_id, DOMAINNAME)
print "server.create_domain(%s): %s" % (DOMAINNAME, r)
# TODO: Add www and stats subdomains
#server.create_domain(session_id, DOMAINNAME, "www", "stats")




# See if the application already exists.
r = server.list_apps(session_id)
to_delete = False
for app in r:
    if app["name"] == APPNAME:
        to_delete = True
        break

# If the application already exists, remove it before adding it
if to_delete:
    print "Application %s already exists. Removing..." % APPNAME
    r = server.delete_app(session_id, APPNAME)
    print "server.delete_app: %s" % r

# Create an application: A mod_wsgi-2.5/Python 2.5 site with name APPNAME
r = server.create_app(session_id, APPNAME, 'mod_wsgi25_25', False, '')
print "server.create_app: %s" % r
PORT = r["port"]

if SERVERIP is None:
    SERVERIP = server.list_websites(session_id)[0]["ip"]
    print "No SERVERIP given. Using %s" % SERVERIP





# See if the website already exists.
r = server.list_websites(session_id)
to_delete = False
for website in r:
    if website["name"] == WEBSITENAME:
        to_delete = True
        break

# If the website already exists, remove it before adding it
if to_delete:
    print "Website %s already exists. Removing..." % WEBSITENAME 
    r = server.delete_website(session_id, WEBSITENAME)
    print "server.delete_website: %s" % r

# TODO: Add https here
# TODO: Add subdomains www and stats here
# TODO: Add path location of application here
r = server.create_website(session_id, WEBSITENAME, SERVERIP, False, [DOMAINNAME], [APPNAME, "/"])
print "server.create_website: %s" % r




if DATABASEPASSWORD is None:
    import randompassword
    DATABASEPASSWORD = randompassword.GenPasswd2()
    print "No DATABASEPASSWORD given. Using %s" % DATABASEPASSWORD

# Create the database
# TODO: Allow PostgreSQL
r = server.create_db(session_id, DATABASENAME, "mysql", DATABASEPASSWORD)
print "server.create_db: %s" % r


# TODO: Add a static media server


if MAILBOXPASSWORD is None:
    import randompassword
    MAILBOXPASSWORD = randompassword.GenPasswd2()
    print "No MAILBOXPASSWORD given. Using %s" % MAILBOXPASSWORD

# Configure mailbox
for i in server.list_mailboxes(session_id):
    print i
r = server.create_mailbox(session_id, MAILBOXUSERNAME, enable_spam_protection=True, discard_spam=False, spam_redirect_folder='', use_manual_procmailrc=False, manual_procmailrc='')
print "server.create_mailbox: %s" % r
r = server.change_mailbox_password(session_id, MAILBOXUSERNAME, MAILBOXPASSWORD)
print "server.change_mailbox_password: %s" % r
