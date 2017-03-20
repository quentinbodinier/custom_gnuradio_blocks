#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from gnuradio import gr

class moving_average(gr.sync_block):
    """
    docstring for block moving_average
    """
    def __init__(self, a, vlen):
        gr.sync_block.__init__(self,
            name="moving_average",
            in_sig=[(np.float32,vlen)],
            out_sig=[(np.float32,vlen)])
        self.a = a
        self.memory = None


    def work(self, input_items, output_items):
        in0 = input_items[0]
        out = output_items[0]
        # <+signal processing here+>
        if self.memory is None:
            self.memory = in0[1,:]
            m = in0
        else:
            m = in0*self.a+np.tile(self.memory*(1-self.a),(in0.shape[0],1))
            self.memory = m[1,:]
        out[:,:] = m
        return len(output_items[0])

