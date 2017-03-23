import numpy as np
from gnuradio import gr
import itertools as it

class interference_predictor(gr.sync_block):
    """
    docstring for block interference_predictor
    """
    def __init__(self, active_subcarriers, gain, active_sec=range(-16,16)):
        gr.sync_block.__init__(self,
            name="interference_predictor",
            in_sig=None,
            out_sig=[(np.float32,len(active_subcarriers)),(np.float32,len(active_subcarriers))])

        self.active_subcarriers = active_subcarriers
        self.active_sec = active_sec
        self.lMatrix = np.zeros((len(active_sec),len(active_subcarriers)),dtype=int)
        self.IMatrix = np.zeros(self.lMatrix.shape,dtype=float)
        self.Ivec_EVM = np.zeros(len(active_subcarriers),dtype=float)
        self.Ivec_PSD = np.zeros(len(active_subcarriers),dtype=float)
        self.gain = gain
        self.compute_interference()

    def work(self, input_items, output_items):
        out = output_items[0]
        out1 = output_items[1]
        # <+signal processing here+>
        out[:,:] = np.tile(self.gain+self.Ivec_EVM,(out.shape[0],1))
        out1[:,:] = np.tile(self.gain+self.Ivec_PSD,(out.shape[0],1))
        return len(output_items[0])

    def compute_interference(self,WF_tx='FBMC',WF_rx='OFDM'):
    	lMatrixbis = np.zeros(self.lMatrix.shape,dtype=int)
        Itable = np.power(10, np.asarray(
            [-1.3272, -10.1479, -18.3959, -22.2449, -24.8545, -26.8434, -28.4544, -29.8098, -30.9804,
             -32.0106, -32.9310, -33.7627, -34.5214, -35.2190, -35.8645, -36.4652, -37.0270, -37.5545, -38.0518,
             -38.5222, -38.9683,
             -39.3926, -39.7971, -40.1836, -40.5537, -40.9084, -41.2494, -41.5775, -41.8936, -42.1986, -42.4932,
             -42.7781, -43.0541,
             -43.3214, -43.5809, -43.8328, -44.0776, -44.3156, -44.5474, -44.7730, -44.9931, -45.2075, -45.4170,
             -45.6214, -45.8211,
             -46.0164, -46.2073, -46.3941, -46.5772, -46.7562, -46.9318, -47.1038, -47.2725, -47.4380, -47.6004,
             -47.7597, -47.9164,
             -48.0700, -48.2211, -48.3696, -48.5156, -48.6592, -48.8005, -48.9394, -49.0764, -49.2109, -49.3436,
             -49.4742, -49.6029,
             -49.7298, -49.8547, -49.9779, -50.0995, -50.2192, -50.3375, -50.4541, -50.5691, -50.6827, -50.7948,
             -50.9054, -51.0148,
             -51.1226, -51.2292, -51.3345, -51.4385, -51.5413, -51.6429, -51.7433, -51.8427, -51.9407, -52.0378,
             -52.1338, -52.2287,
             -52.3226, -52.4155, -52.5074, -52.5985, -52.6884, -52.7775, -52.8657, -52.9530])/10)
        for (i, j) in it.product(range(len(self.active_sec)), range(len(self.active_subcarriers))):
    	    self.lMatrix[i,j] = min(abs(self.active_sec[i]-self.active_subcarriers[j]),100)
    	    lMatrixbis[i,j] = min(abs(128-self.lMatrix[i,j]),100)
       	self.IMatrix = Itable[self.lMatrix]+Itable[lMatrixbis]
        self.Ivec_EVM = 10*np.log10(np.sum(self.IMatrix,0))
        print self.Ivec_EVM
        Itable_PSD = np.power(10, np.asarray([-0.5859, -12.02, -65., -80., -90.])/10)
        for (i, j) in it.product(range(len(self.active_sec)), range(len(self.active_subcarriers))):
    		self.lMatrix[i,j] = min(abs(self.active_sec[i]-self.active_subcarriers[j]),4)
        IMatrix_PSD = Itable_PSD[self.lMatrix]
        self.Ivec_PSD = 10*np.log10(np.sum(IMatrix_PSD,0))



