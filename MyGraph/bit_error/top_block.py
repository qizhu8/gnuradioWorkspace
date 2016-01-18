#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Sun Jan 10 13:32:41 2016
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
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.wxgui import forms
from gnuradio.wxgui import numbersink2
from gnuradio.wxgui import scopesink2
from grc_gnuradio import blks2 as grc_blks2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import wx


class top_block(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Top Block")

        ##################################################
        # Variables
        ##################################################
        self.thresh = thresh = 900*10**-3
        self.samp_rate = samp_rate = 32000

        ##################################################
        # Blocks
        ##################################################
        _thresh_sizer = wx.BoxSizer(wx.VERTICAL)
        self._thresh_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_thresh_sizer,
        	value=self.thresh,
        	callback=self.set_thresh,
        	label='thresh',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._thresh_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_thresh_sizer,
        	value=self.thresh,
        	callback=self.set_thresh,
        	minimum=0,
        	maximum=1,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_thresh_sizer)
        self.wxgui_scopesink2_0 = scopesink2.scope_sink_f(
        	self.GetWin(),
        	title="Scope Plot",
        	sample_rate=samp_rate,
        	v_scale=200*10**-3,
        	v_offset=0,
        	t_scale=100*10**-3,
        	ac_couple=False,
        	xy_mode=False,
        	num_inputs=2,
        	trig_mode=wxgui.TRIG_MODE_AUTO,
        	y_axis_label="Counts",
        )
        self.Add(self.wxgui_scopesink2_0.win)
        self.wxgui_numbersink2_0 = numbersink2.number_sink_f(
        	self.GetWin(),
        	unit="Units",
        	minval=0,
        	maxval=1,
        	factor=1.0,
        	decimal_places=6,
        	ref_level=0,
        	sample_rate=samp_rate,
        	number_rate=15,
        	average=False,
        	avg_alpha=None,
        	label="Number Plot",
        	peak_hold=False,
        	show_gauge=True,
        )
        self.Add(self.wxgui_numbersink2_0.win)
        self.digital_glfsr_source_x_0 = digital.glfsr_source_b(6, True, 0, 1)
        self.blocks_xor_xx_0 = blocks.xor_bb()
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_char*1, samp_rate,True)
        self.blocks_threshold_ff_0 = blocks.threshold_ff(thresh, thresh, 0)
        self.blocks_float_to_char_0 = blocks.float_to_char(1, 1)
        self.blocks_add_const_vxx_0 = blocks.add_const_vff((0.5, ))
        self.blks2_error_rate_0 = grc_blks2.error_rate(
        	type='BER',
        	win_size=1280,
        	bits_per_symbol=1,
        )
        self.analog_noise_source_x_0 = analog.noise_source_f(analog.GR_UNIFORM, 0.5, 32)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_noise_source_x_0, 0), (self.blocks_add_const_vxx_0, 0))    
        self.connect((self.blks2_error_rate_0, 0), (self.wxgui_numbersink2_0, 0))    
        self.connect((self.blks2_error_rate_0, 0), (self.wxgui_scopesink2_0, 0))    
        self.connect((self.blocks_add_const_vxx_0, 0), (self.blocks_threshold_ff_0, 0))    
        self.connect((self.blocks_float_to_char_0, 0), (self.blocks_xor_xx_0, 1))    
        self.connect((self.blocks_threshold_ff_0, 0), (self.blocks_float_to_char_0, 0))    
        self.connect((self.blocks_threshold_ff_0, 0), (self.wxgui_scopesink2_0, 1))    
        self.connect((self.blocks_throttle_0, 0), (self.blks2_error_rate_0, 0))    
        self.connect((self.blocks_throttle_0, 0), (self.blocks_xor_xx_0, 0))    
        self.connect((self.blocks_xor_xx_0, 0), (self.blks2_error_rate_0, 1))    
        self.connect((self.digital_glfsr_source_x_0, 0), (self.blocks_throttle_0, 0))    

    def get_thresh(self):
        return self.thresh

    def set_thresh(self, thresh):
        self.thresh = thresh
        self._thresh_slider.set_value(self.thresh)
        self._thresh_text_box.set_value(self.thresh)
        self.blocks_threshold_ff_0.set_hi(self.thresh)
        self.blocks_threshold_ff_0.set_lo(self.thresh)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.wxgui_scopesink2_0.set_sample_rate(self.samp_rate)


def main(top_block_cls=top_block, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
