#!/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/Users/yuwang/gnuradio/workspace/gnuradioworkspace/MyModule/gr-howto/lib
export GR_CONF_CONTROLPORT_ON=False
export PATH=/Users/yuwang/gnuradio/workspace/gnuradioworkspace/MyModule/gr-howto/build/lib:$PATH
export DYLD_LIBRARY_PATH=/Users/yuwang/gnuradio/workspace/gnuradioworkspace/MyModule/gr-howto/build/lib:$DYLD_LIBRARY_PATH
export PYTHONPATH=$PYTHONPATH
test-howto 
