#!/bin/sh

mkdir -p $OSQA_PROJECTDIR
svn co http://svn.osqa.net/svnroot/osqa/trunk $OSQA_PROJECTDIR
cd $OSQA_PROJECTDIR

# Make a directory for logs
mkdir log

# We need python2.5 to be compatible with WSGI
python2.5 ~/utils/bin/pip install -E $OSQA_ENVDIR -r osqa-requirements.txt
source $OSQA_ENVDIR/bin/activate

# REMOVEME: Should modify osqa-requirements.txt to use this instead of markdown2
easy_install-2.5 --prefix $OSQA_ENVDIR markdown

# [Optional] If you want a MySQL database
easy_install-2.5 --prefix $OSQA_ENVDIR mysql-python

## [Optional] If you want a PostgreSQL database
#easy_install-2.5 --prefix $OSQA_ENVDIR psycopg2

mkdir -p ~/utils/src/
cd ~/utils/src/
wget -nc http://initd.org/pub/software/psycopg/psycopg2-2.0.14.tar.gz
tar zxf psycopg2-2.0.14.tar.gz
cd psycopg2-2.0.14
# edit the line reading "#pg_config=" so that it reads pg_config=/usr/local/pgsql/bin/pg_config:
perl -i -pe 's/^#pg_config\s*=.*/pg_config=\/usr\/local\/pgsql\/bin\/pg_config/' setup.cfg
python setup.py build
python setup.py install
