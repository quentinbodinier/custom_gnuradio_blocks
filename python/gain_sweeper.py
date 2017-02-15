#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright 2017 CentraleSupélec
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

import numpy as np
from gnuradio import gr

class gain_sweeper(gr.sync_block):
    """
    Gain Sweeper block
    """
    def __init__(self, gain_range,segment_length):
        """
        Makes gain sweeper block

        Args:
            gain_range: list of gains to iteratively apply to the input signal
            segment_length: gain increases all segment_length samples
        """
        gr.sync_block.__init__(self,
            name="gain_sweeper",
            in_sig=[np.complex64],
            out_sig=[np.complex64])

        self.gain_range = gain_range
        self.segment_length = segment_length
        self.k=0


    def work(self, input_items, output_items):
        in0 = input_items[0]
        out = output_items[0]
        # <+signal processing here+>
        out[:] = in0*self.gain_range[(self.k/self.segment_length)%len(self.gain_range)]
        self.k += 1 
        return len(output_items[0])

