#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Onoff Bare Test
# Generated: Fri Oct  4 16:28:22 2013
##################################################

from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio import filter
from gnuradio.filter import firdes
from gnuradio.wxgui import forms
from gnuradio.wxgui import scopesink2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import numpy
import wx
from time import sleep

class onoff_flat_test(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Onoff Bare Test")

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 200000
        self.onoff = onoff = 1

        ##################################################
        # Blocks
        ##################################################
        self.sinusoid = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, 1000, 10, 0)
        self.throttle = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate)

        # This is the ON block (a very CPU intensive block)
        self.ONblock = filter.interp_fir_filter_ccc(1, 5000*(1,) )

        # This is the OFF block (a low CPU intensity block)
        self.OFFblock=blocks.multiply_const_cc(1.0)

        # null sink
        self.null_sink = blocks.null_sink(gr.sizeof_gr_complex*1)

        # An auxiliary null source+header 0  to connect the disconnected blocks
        self.nsa=blocks.null_source(gr.sizeof_gr_complex*1)
        self.head_aux=blocks.head(gr.sizeof_gr_complex*1, 0)
        self.connect(self.nsa, self.head_aux)

        # An auxiliary null sink  to connect the disconnected blocks
        self.nullsink_aux=blocks.null_sink(gr.sizeof_gr_complex*1)

        self._onoff_chooser = forms.button(
        	parent=self.GetWin(),
        	value=self.onoff,
        	callback=self.set_onoff,
        	label="On/Off",
        	choices=[0,1],
        	labels=['Off', 'On'],
        )
        self.Add(self._onoff_chooser)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.sinusoid, 0), (self.throttle, 0))

        if self.onoff==1:
          self.connect(self.throttle, self.ONblock)
          self.connect(self.ONblock, self.null_sink)
          self.connect(self.head_aux,self.OFFblock)
          self.connect(self.OFFblock,self.nullsink_aux)
        else:
          self.connect(self.throttle, self.OFFblock)
          self.connect(self.OFFblock, self.null_sink)
          self.connect(self.head_aux,self.ONblock)
          self.connect(self.ONblock,self.nullsink_aux)



    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.sinusoid.set_sampling_freq(self.samp_rate)
        self.throttle.set_sample_rate(self.samp_rate)

    def get_onoff(self):
        return self.onoff


    def _disconnect_on(self):
        """
        Disconnect from the on position
        """
        print "Start disconnecting on"
        self.disconnect(self.throttle, self.ONblock)
        self.disconnect(self.ONblock,self.null_sink)
        self.disconnect(self.head_aux,self.OFFblock)
        self.disconnect(self.OFFblock,self.nullsink_aux)
        print "Stop disconnecting on"

    def _disconnect_off(self):
        """
        Disconnect from the off position
        """
        print "Start disconnecting off"
        self.disconnect(self.throttle, self.OFFblock)
        self.disconnect(self.OFFblock,self.null_sink)
        self.disconnect(self.head_aux,self.ONblock)
        self.disconnect(self.ONblock,self.nullsink_aux)
        print "Stop disconnecting off"

    def _connect_on(self):
        """
        Connect to the on position
        """
        print "Start connecting on"
        self.connect(self.throttle, self.ONblock)
        self.connect(self.ONblock,self.null_sink)
        self.connect(self.head_aux,self.OFFblock)
        self.connect(self.OFFblock,self.nullsink_aux)
        print "Stop connecting on"

    def _connect_off(self):
        """
        Connect to the off position
        """
        print "Start connecting off"
        self.connect(self.throttle, self.OFFblock)
        self.connect(self.OFFblock,self.null_sink)
        self.connect(self.head_aux,self.ONblock)
        self.connect(self.ONblock,self.nullsink_aux)
        print "Stop connecting off"


    def set_onoff(self, onoff):
        """
        Restructure block
        """
        print "Starting restructuring graph from ", self.onoff, " to ", onoff
        print "Locking..."
        self.lock()
        print "Locked"
        if self.onoff==0:
          self._disconnect_off()
          self._connect_on()
        else:
          self._disconnect_on()
          self._connect_off()
        print "Sleep..."
        sleep(0.1)
        print "Unlocking..."
        self.unlock()
        print "Unlocked"
        print "Ending restructuring graph from ", self.onoff, " to ", onoff
        self.onoff = onoff
        self._onoff_chooser.set_value(onoff)



if __name__ == '__main__':
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    tb = onoff_flat_test()
    tb.Start(True)
    tb.Wait()

