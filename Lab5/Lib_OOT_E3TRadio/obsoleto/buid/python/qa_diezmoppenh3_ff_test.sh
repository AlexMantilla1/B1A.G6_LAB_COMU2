#!/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/uis-e3t/MisGits/comdig_Lib_OOT_E3TRadio/python
export GR_CONF_CONTROLPORT_ON=False
export PATH=/home/uis-e3t/MisGits/comdig_Lib_OOT_E3TRadio/buid/python:$PATH
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH
export PYTHONPATH=/home/uis-e3t/MisGits/comdig_Lib_OOT_E3TRadio/buid/swig:$PYTHONPATH
/usr/bin/python2 /home/uis-e3t/MisGits/comdig_Lib_OOT_E3TRadio/python/qa_diezmoppenh3_ff.py 
