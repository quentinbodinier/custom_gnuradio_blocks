import numpy as np
from gnuradio import gr

class OFDM_random_source(gr.sync_block):
    """
    Block that generates 4-QAM symbols and generates an OFDM signal out of it
    """
    def __init__(self, n_subcarriers, allocation_vector, n_cp, preamble_size):
        gr.sync_block.__init__(self,
            name="OFDM_random_source",
            in_sig=None,
            out_sig=[(np.complex64,n_cp+n_subcarriers),(np.complex64,len(allocation_vector))])
        self.constellation=np.array([1+1j, 1-1j, -1-1j, -1+1j])
        self.allocation_vector=allocation_vector
        self.n_cp = n_cp
        self.n_subcarriers = n_subcarriers
        self.preamble_size = preamble_size
        self.in_preamble = True
	self.c=0


    def work(self, input_items, output_items):
        out = output_items[0]
        out1 = output_items[1]
        if self.in_preamble:
        	symbols = np.ones(shape=(out.shape[0],len(self.allocation_vector)),dtype=complex)
        	self.c += out.shape[0]
        else:
			symbols = self.constellation[np.random.randint(4,size=(out.shape[0],len(self.allocation_vector)))]
        x = np.zeros((out.shape[0],self.n_subcarriers), dtype=complex)
        x[:,self.allocation_vector] = symbols
        out[:,self.n_cp:] = np.fft.ifft(x)
        out[:,:self.n_cp] = out[:,-self.n_cp:]
        out1[:,:] = symbols
        return len(output_items[0])

    

