#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Fri Feb 10 15:50:16 2017
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
from gnuradio import filter
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio.wxgui import fftsink2
from gnuradio.wxgui import forms
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import numpy as np
import wx


class top_block(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Top Block")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.tx_signal_dat = tx_signal_dat = "/home/uone/gnuradio/gnuradioworkspace/BackChannel/dataSet/waveform_all_ones.dat"
        self.tx_ip_rx = tx_ip_rx = "192.168.10.2"
        self.shiftRight = shiftRight = -2*np.pi*14/64
        self.shiftLeft = shiftLeft = 2*np.pi*13/64
        self.samp_rate = samp_rate = 20e6
        self.integration_tap = integration_tap = np.ones(80)
        self.FIR_tap = FIR_tap = [0.00268064371500599, 0.00559769448287630, -0.0185697491724867, -0.0484772257271579, 0.0470013313844807, 0.292949628782855, 0.437635353068854, 0.292949628782855, 0.0470013313844807, -0.0484772257271579, -0.0185697491724867, 0.00559769448287630, 0.00268064371500599]
        self.CarrierFreq = CarrierFreq = 2.4e9

        ##################################################
        # Blocks
        ##################################################
        _shiftRight_sizer = wx.BoxSizer(wx.VERTICAL)
        self._shiftRight_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_shiftRight_sizer,
        	value=self.shiftRight,
        	callback=self.set_shiftRight,
        	label='shiftRight',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._shiftRight_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_shiftRight_sizer,
        	value=self.shiftRight,
        	callback=self.set_shiftRight,
        	minimum=-2*np.pi,
        	maximum=0,
        	num_steps=64,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_shiftRight_sizer)
        _shiftLeft_sizer = wx.BoxSizer(wx.VERTICAL)
        self._shiftLeft_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_shiftLeft_sizer,
        	value=self.shiftLeft,
        	callback=self.set_shiftLeft,
        	label='shiftLeft',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._shiftLeft_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_shiftLeft_sizer,
        	value=self.shiftLeft,
        	callback=self.set_shiftLeft,
        	minimum=0,
        	maximum=2*np.pi,
        	num_steps=64,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_shiftLeft_sizer)
        self.wxgui_fftsink2_0_0_0 = fftsink2.fft_sink_c(
        	self.GetWin(),
        	baseband_freq=0,
        	y_per_div=10,
        	y_divs=10,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=samp_rate,
        	fft_size=64,
        	fft_rate=15,
        	average=False,
        	avg_alpha=None,
        	title='FFT Plot',
        	peak_hold=False,
        )
        self.Add(self.wxgui_fftsink2_0_0_0.win)
        self.wxgui_fftsink2_0_0 = fftsink2.fft_sink_c(
        	self.GetWin(),
        	baseband_freq=0,
        	y_per_div=10,
        	y_divs=10,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=samp_rate,
        	fft_size=64,
        	fft_rate=15,
        	average=False,
        	avg_alpha=None,
        	title='FFT Plot',
        	peak_hold=False,
        )
        self.Add(self.wxgui_fftsink2_0_0.win)
        self.wxgui_fftsink2_0 = fftsink2.fft_sink_c(
        	self.GetWin(),
        	baseband_freq=0,
        	y_per_div=10,
        	y_divs=10,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=samp_rate,
        	fft_size=64,
        	fft_rate=15,
        	average=False,
        	avg_alpha=None,
        	title='FFT Plot',
        	peak_hold=False,
        )
        self.Add(self.wxgui_fftsink2_0.win)
        self.freq_xlating_fft_filter_ccc_0_0 = filter.freq_xlating_fft_filter_ccc(1, (FIR_tap), shiftRight, samp_rate)
        self.freq_xlating_fft_filter_ccc_0_0.set_nthreads(1)
        self.freq_xlating_fft_filter_ccc_0_0.declare_sample_delay(0)
        self.freq_xlating_fft_filter_ccc_0 = filter.freq_xlating_fft_filter_ccc(1, (FIR_tap), shiftLeft, samp_rate)
        self.freq_xlating_fft_filter_ccc_0.set_nthreads(1)
        self.freq_xlating_fft_filter_ccc_0.declare_sample_delay(0)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_gr_complex*1, tx_signal_dat, True)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_file_source_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.freq_xlating_fft_filter_ccc_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.freq_xlating_fft_filter_ccc_0_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.wxgui_fftsink2_0_0_0, 0))
        self.connect((self.freq_xlating_fft_filter_ccc_0, 0), (self.wxgui_fftsink2_0, 0))
        self.connect((self.freq_xlating_fft_filter_ccc_0_0, 0), (self.wxgui_fftsink2_0_0, 0))

    def get_tx_signal_dat(self):
        return self.tx_signal_dat

    def set_tx_signal_dat(self, tx_signal_dat):
        self.tx_signal_dat = tx_signal_dat
        self.blocks_file_source_0.open(self.tx_signal_dat, True)

    def get_tx_ip_rx(self):
        return self.tx_ip_rx

    def set_tx_ip_rx(self, tx_ip_rx):
        self.tx_ip_rx = tx_ip_rx

    def get_shiftRight(self):
        return self.shiftRight

    def set_shiftRight(self, shiftRight):
        self.shiftRight = shiftRight
        self._shiftRight_slider.set_value(self.shiftRight)
        self._shiftRight_text_box.set_value(self.shiftRight)
        self.freq_xlating_fft_filter_ccc_0_0.set_center_freq(self.shiftRight)

    def get_shiftLeft(self):
        return self.shiftLeft

    def set_shiftLeft(self, shiftLeft):
        self.shiftLeft = shiftLeft
        self._shiftLeft_slider.set_value(self.shiftLeft)
        self._shiftLeft_text_box.set_value(self.shiftLeft)
        self.freq_xlating_fft_filter_ccc_0.set_center_freq(self.shiftLeft)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.wxgui_fftsink2_0_0_0.set_sample_rate(self.samp_rate)
        self.wxgui_fftsink2_0_0.set_sample_rate(self.samp_rate)
        self.wxgui_fftsink2_0.set_sample_rate(self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)

    def get_integration_tap(self):
        return self.integration_tap

    def set_integration_tap(self, integration_tap):
        self.integration_tap = integration_tap

    def get_FIR_tap(self):
        return self.FIR_tap

    def set_FIR_tap(self, FIR_tap):
        self.FIR_tap = FIR_tap
        self.freq_xlating_fft_filter_ccc_0_0.set_taps((self.FIR_tap))
        self.freq_xlating_fft_filter_ccc_0.set_taps((self.FIR_tap))

    def get_CarrierFreq(self):
        return self.CarrierFreq

    def set_CarrierFreq(self, CarrierFreq):
        self.CarrierFreq = CarrierFreq


def main(top_block_cls=top_block, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
