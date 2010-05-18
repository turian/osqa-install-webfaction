#!/usr/bin/python

from globals import *
import os.path
import sys

generalconftxt = '''
ServerRoot %s
LoadModule dir_module modules/mod_dir.so
LoadModule env_module modules/mod_env.so
#LoadModule setenvif_module modules/mod_setenvif.so
LoadModule log_config_module modules/mod_log_config.so
LoadModule mime_module modules/mod_mime.so
LoadModule rewrite_module modules/mod_rewrite.so
LoadModule wsgi_module modules/mod_wsgi.so

KeepAlive Off
ServerLimit 4

#SetEnvIf X-Forwarded-SSL on HTTPS=1

WSGIPythonPath %s

LoadModule alias_module modules/mod_alias.so
WSGIDaemonProcess osqaWSGI user=%s group=%s threads=25 python-path=%s
WSGIProcessGroup osqaWSGI

#ErrorLog "logs/MYOSQA_2009_05_06.log"
SetHandler none
#Alias /site_media /home/USERNAME/webapps/static/MYOSQA/site_media

#AliasMatch /([^/]*\\.css) /home/USERNAME/webapps/osqa_server/projects/MYOSQA/templates/content/style/$1
#<Directory "%s">
#    Order deny,allow
#    Allow from all
#</Directory>

Include conf/osqa/*.conf
'''

specificconftxt = '''
Listen %s
NameVirtualHost 127.0.0.1:%s

<VirtualHost 127.0.0.1:%s>
    ServerAdmin %s
    ServerName %s
    LogFormat "%%{X-Forwarded-For}i %%l %%u %%t \\"%%r\\" %%>s %%b \\"%%{Referer}i\\" \\"%%{User-Agent}i\\"" combined
    CustomLog %s combined
    ErrorLog %s
    WSGIScriptAlias / %s
    #force all content to be served as static files
    #otherwise django will be crunching images through itself wasting time
    Alias /content/ %s
    Alias /forum/admin/media/ %s
    Alias /admin_media/ %s
</VirtualHost>
'''

apacheconfdir = os.path.join(os.environ["HOME"], "webapps/%s/apache2/conf/" % APPALLOSQA)

generalconffilename = os.path.join(apacheconfdir, "httpd.conf")
print >> sys.stderr, "Writing to %s" % generalconffilename
open(generalconffilename, "wt").write(generalconftxt % (os.path.join(os.environ["HOME"], "webapps/%s/apache2/" % APPALLOSQA), os.path.join(ENVDIR, "lib/python2.5/site-packages/"), os.environ["USER"], os.environ["USER"], os.path.join(ENVDIR, "lib/python2.5/site-packages/"), os.path.join(PROJECTDIR, "templates/content/")))

specificconfdir = os.path.join(apacheconfdir, "osqa")
if not os.path.exists(specificconfdir):
    print >> sys.stderr, "mkdir %s" % specificconfdir
    os.mkdir(specificconfdir)

specificconffilename = os.path.join(specificconfdir, "%s.conf" % APPNAME)
print >> sys.stderr, "Writing to %s" % specificconffilename
open(specificconffilename, "wt").write(specificconftxt % (PORT, PORT, PORT, \
    EMAILADDRESS, FULLDOMAINNAME,
    os.path.join(os.environ["HOME"], "logs/user/access_%s_log" % WEBSITENAME), os.path.join(os.environ["HOME"], "logs/user/error_%s_log" % WEBSITENAME), os.path.join(PROJECTDIR, "osqa.wsgi"),
    os.path.join(PROJECTDIR, "templates/content/"), os.path.join(ENVDIR, "lib/python2.5/site-packages/django/contrib/admin/media/"), os.path.join(ENVDIR, "lib/python2.5/site-packages/django/contrib/admin/media/")))
