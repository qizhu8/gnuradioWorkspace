#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Fri Apr 21 16:11:30 2017
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
from gnuradio import uhd
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio.wxgui import fftsink2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import time
import wx


class top_block(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Top Block")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.tx_signal_dat = tx_signal_dat = "/home/uone/gnuradio/gnuradioworkspace/BackChannel/dataSet/sending/waveform_fsk"
        self.tx_ip_rx = tx_ip_rx = "192.168.10.2"
        self.samp_rate = samp_rate = 20e6
        self.rx_signal_dat = rx_signal_dat = "/home/uone/gnuradio/gnuradioworkspace/BackChannel/dataSet/receiving/waveform_rec_fsk"
        self.payloadSize = payloadSize = 100
        self.extra_notation = extra_notation = "_85db_"
        self.CarrierFreq = CarrierFreq = 1.5e9
        self.BandWidth = BandWidth = 40e6

        ##################################################
        # Blocks
        ##################################################
        self.wxgui_fftsink2_1 = fftsink2.fft_sink_c(
        	self.GetWin(),
        	baseband_freq=0,
        	y_per_div=10,
        	y_divs=10,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=samp_rate,
        	fft_size=1024,
        	fft_rate=15,
        	average=False,
        	avg_alpha=None,
        	title='FFT Plot',
        	peak_hold=False,
        )
        self.Add(self.wxgui_fftsink2_1.win)
        self.uhd_usrp_source_0 = uhd.usrp_source(
        	",".join(("", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_source_0.set_samp_rate(samp_rate)
        self.uhd_usrp_source_0.set_center_freq(CarrierFreq, 0)
        self.uhd_usrp_source_0.set_gain(30, 0)
        self.uhd_usrp_source_0.set_antenna('RX2', 0)
        self.uhd_usrp_source_0.set_bandwidth(BandWidth, 0)
        self.file_sink = blocks.file_sink(gr.sizeof_gr_complex*1, rx_signal_dat+"_"+str(payloadSize)+extra_notation+".dat", False)
        self.file_sink.set_unbuffered(False)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.uhd_usrp_source_0, 0), (self.file_sink, 0))
        self.connect((self.uhd_usrp_source_0, 0), (self.wxgui_fftsink2_1, 0))

    def get_tx_signal_dat(self):
        return self.tx_signal_dat

    def set_tx_signal_dat(self, tx_signal_dat):
        self.tx_signal_dat = tx_signal_dat

    def get_tx_ip_rx(self):
        return self.tx_ip_rx

    def set_tx_ip_rx(self, tx_ip_rx):
        self.tx_ip_rx = tx_ip_rx

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.wxgui_fftsink2_1.set_sample_rate(self.samp_rate)
        self.uhd_usrp_source_0.set_samp_rate(self.samp_rate)

    def get_rx_signal_dat(self):
        return self.rx_signal_dat

    def set_rx_signal_dat(self, rx_signal_dat):
        self.rx_signal_dat = rx_signal_dat
        self.file_sink.open(self.rx_signal_dat+"_"+str(self.payloadSize)+self.extra_notation+".dat")

    def get_payloadSize(self):
        return self.payloadSize

    def set_payloadSize(self, payloadSize):
        self.payloadSize = payloadSize
        self.file_sink.open(self.rx_signal_dat+"_"+str(self.payloadSize)+self.extra_notation+".dat")

    def get_extra_notation(self):
        return self.extra_notation

    def set_extra_notation(self, extra_notation):
        self.extra_notation = extra_notation
        self.file_sink.open(self.rx_signal_dat+"_"+str(self.payloadSize)+self.extra_notation+".dat")

    def get_CarrierFreq(self):
        return self.CarrierFreq

    def set_CarrierFreq(self, CarrierFreq):
        self.CarrierFreq = CarrierFreq
        self.uhd_usrp_source_0.set_center_freq(self.CarrierFreq, 0)

    def get_BandWidth(self):
        return self.BandWidth

    def set_BandWidth(self, BandWidth):
        self.BandWidth = BandWidth
        self.uhd_usrp_source_0.set_bandwidth(self.BandWidth, 0)


def main(top_block_cls=top_block, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
