import numpy as np
import scipy as sp
import scipy.fftpack as ff


def main():
    np.info(ff.fft)  # Get help on the fft() function

    print('-' * 60)

    np.source(ff.fft)  # View the source of the fft() function

    print('-' * 60)

    np.lookfor('convolve') # search np docs
    print('-' * 60)
    
    sp.lookfor('convolve')

if __name__ == '__main__':
    main()
