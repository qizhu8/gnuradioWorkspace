#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Thu Jan 21 15:54:23 2016
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from gnuradio import analog
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.ctrlport.monitor import *
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.wxgui import scopesink2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import wx


class top_block(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Top Block")

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 32e3

        ##################################################
        # Blocks
        ##################################################
        self.wxgui_scopesink2_0 = scopesink2.scope_sink_f(
        	self.GetWin(),
        	title="Scope Plot",
        	sample_rate=samp_rate,
        	v_scale=0,
        	v_offset=0,
        	t_scale=0,
        	ac_couple=False,
        	xy_mode=False,
        	num_inputs=1,
        	trig_mode=wxgui.TRIG_MODE_AUTO,
        	y_axis_label="Counts",
        )
        self.Add(self.wxgui_scopesink2_0.win)
        self.digital_map_bb_0 = digital.map_bb(([1, -1]))
        self.blocks_vector_source_x_0 = blocks.vector_source_i((1, 1, 1, 0), True, 1, [])
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_int*1, samp_rate,True)
        self.blocks_int_to_float_0 = blocks.int_to_float(1, 1)
        self.blocks_float_to_char_0 = blocks.float_to_char(1, 1)
        self.blocks_ctrlport_monitor_performance_0 = not True or monitor("gr-perf-monitorx")
        self.blocks_char_to_float_0 = blocks.char_to_float(1, 1)
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.analog_const_source_x_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, 0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_const_source_x_0, 0), (self.blocks_add_xx_0, 1))    
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_float_to_char_0, 0))    
        self.connect((self.blocks_char_to_float_0, 0), (self.wxgui_scopesink2_0, 0))    
        self.connect((self.blocks_float_to_char_0, 0), (self.digital_map_bb_0, 0))    
        self.connect((self.blocks_int_to_float_0, 0), (self.blocks_add_xx_0, 0))    
        self.connect((self.blocks_throttle_0, 0), (self.blocks_int_to_float_0, 0))    
        self.connect((self.blocks_vector_source_x_0, 0), (self.blocks_throttle_0, 0))    
        self.connect((self.digital_map_bb_0, 0), (self.blocks_char_to_float_0, 0))    

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.wxgui_scopesink2_0.set_sample_rate(self.samp_rate)


def main(top_block_cls=top_block, options=None):

    tb = top_block_cls()
    tb.Start(True)
    (tb.blocks_ctrlport_monitor_performance_0).start()
    tb.Wait()


if __name__ == '__main__':
    main()
