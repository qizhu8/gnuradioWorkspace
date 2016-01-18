#!/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/uone/gnuradio/gnuradioworkspace/MyModule/gr-howto/python
export GR_CONF_CONTROLPORT_ON=False
export PATH=/home/uone/gnuradio/gnuradioworkspace/MyModule/gr-howto/build/python:$PATH
export LD_LIBRARY_PATH=/home/uone/gnuradio/gnuradioworkspace/MyModule/gr-howto/build/lib:$LD_LIBRARY_PATH
export PYTHONPATH=/home/uone/gnuradio/gnuradioworkspace/MyModule/gr-howto/build/swig:$PYTHONPATH
/usr/bin/python2 /home/uone/gnuradio/gnuradioworkspace/MyModule/gr-howto/python/qa_square_ff.py 
