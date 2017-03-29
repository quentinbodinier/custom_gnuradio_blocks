#!/usr/bin/env python

import numpy as np
from gnuradio import gr

class rephaser(gr.sync_block):
    """
    docstring for block rephaser
    """
    def __init__(self, vlen):
        gr.sync_block.__init__(self,
            name="rephaser",
            in_sig=[(np.complex64,vlen)],
            out_sig=[(np.complex64,vlen)])


    def work(self, input_items, output_items):
        in0 = input_items[0]
        out = output_items[0]
        mean_phase = np.mean(angle(in0))
        # <+signal processing here+>
        out[:] = in0*np.exp(-1j*mean_phase)
        return len(output_items[0])

