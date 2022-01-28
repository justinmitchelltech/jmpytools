from matplotlib import style
import matplotlib.pyplot as plt 
import numpy as np 
from fft import use_scipy_fft


# Create and plot a signal to test FFT with --------------- \

f1 = 5  # first frequency [Hz]
f2 = 10  # second frequency [Hz]
Fs = 100  # sampling rate [Hz]
t = np.arange(0, 1, 1/Fs)
y = 0.75*np.sin(2*np.pi*f1*t) + 0.5*np.sin(2*np.pi*f2*t)

fig, ax = plt.subplots(1, 2, figsize=(12, 5))

ax[0].plot(t, y, 'g.-')
ax[0].set_xlabel("Time [s]")
ax[0].set_title("Signal in Time Domain")


# Take FFT of signal and plot results --------------------- \

fr, y_m = use_scipy_fft(t, y, Fs)

ax[1].stem(fr, y_m)
ax[1].set_xlabel("Frequency [Hz]")
ax[1].set_title("FFT of Signal, Frequency Domain")

plt.show()
