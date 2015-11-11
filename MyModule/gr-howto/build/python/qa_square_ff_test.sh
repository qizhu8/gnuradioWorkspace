#!/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/Users/yuwang/gnuradio/workspace/gnuradioworkspace/MyModule/gr-howto/python
export GR_CONF_CONTROLPORT_ON=False
export PATH=/Users/yuwang/gnuradio/workspace/gnuradioworkspace/MyModule/gr-howto/build/python:$PATH
export DYLD_LIBRARY_PATH=/Users/yuwang/gnuradio/workspace/gnuradioworkspace/MyModule/gr-howto/build/lib:$DYLD_LIBRARY_PATH
export PYTHONPATH=/Users/yuwang/gnuradio/workspace/gnuradioworkspace/MyModule/gr-howto/build/swig:$PYTHONPATH
/opt/local/bin/python2.7 /Users/yuwang/gnuradio/workspace/gnuradioworkspace/MyModule/gr-howto/python/qa_square_ff.py 
