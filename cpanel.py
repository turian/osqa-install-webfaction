"""
WebFaction cpanel helper functions.
"""

import sys

def try_remove(server, session_id, name, type, delete_thing, list_thing, namename="name", delete_extra_params=[]):
    """
    Try to remove something using the webfaction API, if it exists.
    """
    # See if the something already exists.
    r = server.__getattr__(list_thing)(session_id)
    to_delete = False
    for i in r:
#        print >> sys.stderr, i
        if i[namename] == name:
            to_delete = True
            break
    
    # If the something already exists, remove it before adding it
    if to_delete:
        import time
        for i in range(10, 0, -1):
            print >> sys.stderr, "Going to remove %s %s (%s), sleeping %d seconds..." % (type, name, `delete_extra_params`, i)
            time.sleep(1)

        print >> sys.stderr, "%s %s already exists. Removing..." % (type, name)
#        print >> sys.stderr, delete_thing, ([session_id, name] + delete_extra_params)
        r = server.__getattr__(delete_thing)(*([session_id, name] + delete_extra_params))
        print >> sys.stderr, "server.%s: %s" % (delete_thing, r)

def force_create(server, session_id, name, type, create_thing, delete_thing, list_thing, create_parameters=[], namename="name", delete_extra_params=[], overwrite=True):
    """
    Force the creation of something using the webfaction API.
    overwrite determines whether to delete the entity if it exists.
    """
    print >> sys.stderr, tuple([repr(s) for s in [server, session_id, name, type, create_thing, delete_thing, list_thing, create_parameters]])
    print >> sys.stderr, "force_create(server=%s, session_id=%s, name=%s, type=%s, create_thing=%s, delete_thing=%s, list_thing=%s, create_parameters=%s)" % tuple([repr(s) for s in [server, session_id, name, type, create_thing, delete_thing, list_thing, create_parameters]])

    if overwrite:
        try_remove(server, session_id, name, type, delete_thing, list_thing, namename=namename, delete_extra_params=delete_extra_params)
    
    # Create the something
    #print [session_id, name] + create_parameters
    r = server.__getattr__(create_thing)(*([session_id, name] + create_parameters))
    print >> sys.stderr, "server.%s: %s" % (create_thing, r)
    return r

