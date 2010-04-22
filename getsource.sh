#!/bin/sh

cd ~/utils/src/
svn co http://svn.osqa.net/svnroot/osqa/trunk osqa
cd osqa

# We need python2.5 to be compatible with WSGI
python2.5 ~/utils/bin/pip install -E ~/envs/$OSQA_APPNAME -r osqa-requirements.txt
source ~/envs/osqa/bin/activate

# [Optional] If you want a MySQL database
easy_install-2.5 --prefix ~/envs/$OSQA_APPNAME/ mysql-python
