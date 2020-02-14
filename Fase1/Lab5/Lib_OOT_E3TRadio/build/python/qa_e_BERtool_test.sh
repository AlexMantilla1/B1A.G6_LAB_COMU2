#!/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/onchip/Documents/Alex/2019-2/ComuII/B1A.G6_LAB_COMU2/Lab5/comdig_Lib_OOT_E3TRadio/python
export GR_CONF_CONTROLPORT_ON=False
export PATH=/home/onchip/Documents/Alex/2019-2/ComuII/B1A.G6_LAB_COMU2/Lab5/comdig_Lib_OOT_E3TRadio/build/python:$PATH
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH
export PYTHONPATH=/home/onchip/Documents/Alex/2019-2/ComuII/B1A.G6_LAB_COMU2/Lab5/comdig_Lib_OOT_E3TRadio/build/swig:$PYTHONPATH
/usr/bin/python2 /home/onchip/Documents/Alex/2019-2/ComuII/B1A.G6_LAB_COMU2/Lab5/comdig_Lib_OOT_E3TRadio/python/qa_e_BERtool.py 
