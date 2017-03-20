#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from gnuradio import gr

class complex_to_power(gr.decim_block):
    """
    docstring for block complex_to_power
    """
    def __init__(self, vlen):
        gr.decim_block.__init__(self,
            name="complex_to_power",
            in_sig=[(np.complex,vlen)],
            out_sig=[(np.complex,vlen)])


    def work(self, input_items, output_items):
        in0 = input_items[0]
        out = output_items[0]
        # <+signal processing here+>
        out[:,:] = np.square(np.abs(np.asarray(in0)))
        return len(output_items[0])

