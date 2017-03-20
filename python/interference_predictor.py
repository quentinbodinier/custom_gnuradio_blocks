import numpy as np
from gnuradio import gr

class interference_predictor(gr.sync_block):
    """
    docstring for block interference_predictor
    """
    def __init__(self, transmit_signal, n_subcarriers, active_subcarriers):
        gr.sync_block.__init__(self,
            name="interference_predictor",
            in_sig=None,
            out_sig=[(numpy.float,len(active_subcarriers))])


    def work(self, input_items, output_items):
        in0 = input_items[0]
        out = output_items[0]
        # <+signal processing here+>
        out[:,:] = 1/2
        return len(output_items[0])

