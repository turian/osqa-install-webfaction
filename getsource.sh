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
