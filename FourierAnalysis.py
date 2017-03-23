import numpy as np
import matplotlib.pyplot as plt
from scipy.io import scipy.io.wavfile as sciwav
import numpy.fft as fft
Tr = sciwav.read('trumpet.wav')[1]
Vi = sciwav.read('violin.wav')[1]
fTr = fft.fft(Tr)
fVi = fft.fft(Vi)
