#!/usr/bin/python

from globals import *
import os.path
import sys

conftxt = '''
ServerAdmin %s
ServerRoot %s
ServerName %s

LoadModule dir_module modules/mod_dir.so
LoadModule env_module modules/mod_env.so
#LoadModule setenvif_module modules/mod_setenvif.so
LoadModule log_config_module modules/mod_log_config.so
LoadModule mime_module modules/mod_mime.so
LoadModule rewrite_module modules/mod_rewrite.so
LoadModule wsgi_module modules/mod_wsgi.so

KeepAlive Off
Listen %s
LogFormat "%%{X-Forwarded-For}i %%l %%u %%t \\"%%r\\" %%>s %%b \\"%%{Referer}i\\" \\"%%{User-Agent}i\\"" combined
CustomLog %s combined
ErrorLog %s
ServerLimit 2

#SetEnvIf X-Forwarded-SSL on HTTPS=1

WSGIPythonPath %s
WSGIScriptAlias / %s

LoadModule alias_module modules/mod_alias.so
WSGIDaemonProcess osqaWSGI user=%s group=%s threads=25 python-path=%s
WSGIProcessGroup osqaWSGI

NameVirtualHost 127.0.0.1:%s

#ErrorLog "logs/MYOSQA_2009_05_06.log"
SetHandler none
#Alias /site_media /home/USERNAME/webapps/static/MYOSQA/site_media

#force all content to be served as static files
#otherwise django will be crunching images through itself wasting time
Alias /content/ %s
Alias /forum/admin/media/ %s
#AliasMatch /([^/]*\\.css) /home/USERNAME/webapps/osqa_server/projects/MYOSQA/templates/content/style/$1
<Directory "%s">
#    Order deny,allow
#    Allow from all
</Directory>
'''

conffilename = os.path.join(os.environ["HOME"], "webapps/%s/apache2/conf/httpd.conf" % APPNAME)
print >> sys.stderr, "Writing to %s" % conffilename
open(conffilename, "wt").write(conftxt % (EMAILADDRESS, os.path.join(os.environ["HOME"], "webapps/%s/apache2/" % APPNAME), FULLDOMAINNAME, PORT, os.path.join(os.environ["HOME"], "logs/user/access_%s_log" % WEBSITENAME), os.path.join(os.environ["HOME"], "logs/user/error_%s_log" % WEBSITENAME), os.path.join(ENVDIR, "lib/python2.5/site-packages/"), os.path.join(PROJECTDIR, "osqa.wsgi"), os.environ["USER"], os.environ["USER"], os.path.join(ENVDIR, "lib/python2.5/site-packages/"), PORT, os.path.join(PROJECTDIR, "templates/content/"), os.path.join(ENVDIR, "lib/python2.5/site-packages/django/contrib/admin/media/"), os.path.join(PROJECTDIR, "templates/content/")))