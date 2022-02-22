import numpy as np 
from scipy.fft import fft


def use_scipy_fft(t, y, Fs):
    
    """
    
    function
    -----------
    Does a Fast Fourier Transform (FFT) of a time series signal

    parameters
    -----------
    t: time domain
    y: time series signal
    Fs: sampling rate

    returns
    -----------
    fr: frequency domain
    y_m: signal in the frequency domain (the FFT)

    other info
    -----------
    reference that I used to create this function:
    https://medium.com/@khairulomar/deconstructing-time-series-using-fourier-transform-e52dd535a44e

    
    """

    y_fft = fft(y)
    n = np.size(t)
    fr = Fs/2 * np.linspace(0,1,int(n/2))
    y_m = 2/n * abs(y_fft[0:np.size(fr)])

    return fr, y_m
