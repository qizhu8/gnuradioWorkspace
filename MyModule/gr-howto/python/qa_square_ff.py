#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright 2015 <+YOU OR YOUR COMPANY+>.
# 
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
# 
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
# 

'''
from gnuradio import gr, gr_unittest
from gnuradio import blocks
import howto_swig as howto

class qa_square_ff (gr_unittest.TestCase):

    def setUp (self):
        self.tb = gr.top_block ()

    def tearDown (self):
        self.tb = None

    def test_001_t (self):
        src_data = (-3, 4, -5.5, 2, 3)
	expected_result = (9, 16, 30.25, 4, 9)
	src = block.vector_source_f(src_data)  # the src_data will go into the block from there
	sqr = howto.square_ff()  # the block we made
	dst = block.vector_sink_f()  # the couput of the block will be gathered from here
	self.tb.connect(src, sqr) # connect src set to the block
	self.tb.connect(sqr, dst) # connect the block to the dst set
        # set up fg
        self.tb.run () # run the graph until all the blocks finished working
        # check data
	result_data = dst.data() # get the data from the structure
	self.assertFloatTuplesAlmostEqual(expected_result, result_data, 6) # check the data


if __name__ == '__main__':
    gr_unittest.run(qa_square_ff, "qa_square_ff.xml")
'''
from gnuradio import gr, gr_unittest
from gnuradio import blocks
import howto_swig as howto

class qa_square_ff (gr_unittest.TestCase):

    def setUp (self):
        self.tb = gr.top_block ()

    def tearDown (self):
        self.tb = None

    def test_001_square_ff(self):
        src_data = (-3, 4, -5.5, 2, 3)
        expected_result = (9, 16, 30.25, 4, 9)
        src = blocks.vector_source_f(src_data)
        sqr = howto.square_ff()
        dst = blocks.vector_sink_f()
        self.tb.connect(src, sqr)
        self.tb.connect(sqr, dst)
        self.tb.run()
        result_data = dst.data()
        self.assertFloatTuplesAlmostEqual(expected_result, result_data, 6)

if __name__ == '__main__':
    gr_unittest.run(qa_square_ff, "qa_square_ff.xml")