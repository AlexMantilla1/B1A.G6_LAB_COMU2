#!/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/hob/Dropbox/EnUbuntuFull/gr-E3TRadio/python
export GR_CONF_CONTROLPORT_ON=False
export PATH=/home/hob/Dropbox/EnUbuntuFull/gr-E3TRadio/python/python:$PATH
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH
export PYTHONPATH=/home/hob/Dropbox/EnUbuntuFull/gr-E3TRadio/python/swig:$PYTHONPATH
/usr/bin/python2 /home/hob/Dropbox/EnUbuntuFull/gr-E3TRadio/python/qa_diezma_ff.py 
