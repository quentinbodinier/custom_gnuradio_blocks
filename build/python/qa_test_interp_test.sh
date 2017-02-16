#!/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/quentin/Documents/software/gr-custom_blocks/python
export GR_CONF_CONTROLPORT_ON=False
export PATH=/home/quentin/Documents/software/gr-custom_blocks/build/python:$PATH
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH
export PYTHONPATH=/home/quentin/Documents/software/gr-custom_blocks/build/swig:$PYTHONPATH
/usr/bin/python2 /home/quentin/Documents/software/gr-custom_blocks/python/qa_test_interp.py 
