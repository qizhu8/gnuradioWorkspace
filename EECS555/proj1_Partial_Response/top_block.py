#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Sun Jan 10 18:13:37 2016
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

from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.wxgui import scopesink2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import numpy
import wx


class top_block(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Top Block")

        ##################################################
        # Variables
        ##################################################
        self.signal_rate = signal_rate = 1000
        self.SRRC_coeff_len = SRRC_coeff_len = 10
        self.samp_rate = samp_rate = SRRC_coeff_len * signal_rate
        self.SRRC_coeff = SRRC_coeff = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]

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
        self.blocks_vector_to_stream_0 = blocks.vector_to_stream(gr.sizeof_float*1, SRRC_coeff_len)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_int*1, samp_rate,True)
        self.blocks_stream_to_vector_0 = blocks.stream_to_vector(gr.sizeof_float*1, SRRC_coeff_len)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((SRRC_coeff))
        self.blocks_int_to_float_0 = blocks.int_to_float(1, 1)
        self.analog_random_source_x_0 = blocks.vector_source_i(map(int, numpy.random.randint(0, 2, signal_rate)), True)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_random_source_x_0, 0), (self.blocks_throttle_0, 0))    
        self.connect((self.blocks_int_to_float_0, 0), (self.blocks_stream_to_vector_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_vector_to_stream_0, 0))    
        self.connect((self.blocks_stream_to_vector_0, 0), (self.blocks_multiply_const_vxx_0, 0))    
        self.connect((self.blocks_throttle_0, 0), (self.blocks_int_to_float_0, 0))    
        self.connect((self.blocks_vector_to_stream_0, 0), (self.wxgui_scopesink2_0, 0))    

    def get_signal_rate(self):
        return self.signal_rate

    def set_signal_rate(self, signal_rate):
        self.signal_rate = signal_rate
        self.set_samp_rate(self.SRRC_coeff_len * self.signal_rate)

    def get_SRRC_coeff_len(self):
        return self.SRRC_coeff_len

    def set_SRRC_coeff_len(self, SRRC_coeff_len):
        self.SRRC_coeff_len = SRRC_coeff_len
        self.set_samp_rate(self.SRRC_coeff_len * self.signal_rate)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.wxgui_scopesink2_0.set_sample_rate(self.samp_rate)

    def get_SRRC_coeff(self):
        return self.SRRC_coeff

    def set_SRRC_coeff(self, SRRC_coeff):
        self.SRRC_coeff = SRRC_coeff
        self.blocks_multiply_const_vxx_0.set_k((self.SRRC_coeff))


def main(top_block_cls=top_block, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
