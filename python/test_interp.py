
import numpy as np
from gnuradio import gr

class test_interp(gr.interp_block):
    """
    docstring for block test_interp
    """
    def __init__(self):
        gr.interp_block.__init__(self,
            name="test_interp",
            in_sig=[np.int8],
            out_sig=[np.complex64], interp=2090)


    def work(self, input_items, output_items):
        in0 = input_items[0]
        out = output_items[0]
        print len(in0)
  
        for j in range(len(in0)):
        	if in0[j] == 1:
        		out[j*2090:(j+1)*2090-1] = 1
        	else:
        		out[j*2090:(j+1)*2090-1] = 0


        return len(output_items[0])

