#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from gnuradio import gr

class triggered_vector_interruptor(gr.sync_block):
    """
    docstring for block triggered_vector_interruptor
    """
    def __init__(self, default, trigger, vector_length, selector):
        gr.sync_block.__init__(self,
            name="triggered_vector_interruptor",
            in_sig=[(np.complex64, vector_length)],
            out_sig=[(np.complex64, vector_length)])
        self.toSend=np.asarray(default,dtype=complex)
        self.trigger=trigger
	self.selector=selector


    def work(self, input_items, output_items):
        in0 = input_items[0]
        out = output_items[0]
        if self.trigger==1:
        	self.toSend[self.selector]=in0[-1,self.selector]
		self.trigger=0
        out[:, :] = np.tile(self.toSend,(out.shape[0],1))
        return len(output_items[0])


    def set_trigger(self, trigger):
    	self.trigger=trigger
