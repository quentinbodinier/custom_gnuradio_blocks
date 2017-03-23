import numpy as np
from gnuradio import gr

class input_selector(gr.sync_block):
    """
    docstring for block input_selector
    """
    def __init__(self, num_inputs, selected_input):
        gr.sync_block.__init__(self,
            name="input_selector",
            in_sig=[np.complex64 for i in range(num_inputs)],
            out_sig=[np.complex64])
        self.selected_input = selected_input


    def work(self, input_items, output_items):
        in0 = input_items[self.selected_input]
        out = output_items[0]
        # <+signal processing here+>
        out[:] = in0
        return len(output_items[0])

