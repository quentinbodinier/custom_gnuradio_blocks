import numpy as np
from gnuradio import gr

class vector_selector(gr.sync_block):
    """
    This block selects the elements specfied by the selector from the input vector. 
    It can typically be used to extract useful subcarriers from a given signal
    """
    def __init__(self, input_size, selector):
        gr.sync_block.__init__(self,
            name="vector_selector",
            in_sig=[(np.complex64, input_size)],
            out_sig=[(np.complex64, len(selector))])
        self.input_size=input_size
        self.selector=selector


    def work(self, input_items, output_items):
        in0 = input_items[0]
        out = output_items[0]
        # <+signal processing here+>
        out[:,:len(self.selector)] = in0[:,np.asarray(self.selector)]
        return len(output_items[0])

