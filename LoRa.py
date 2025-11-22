import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('TkAgg')
# Basic LoRa parameters
Fs = 1e6            # Sampling frequency
BW = 125e3          # Bandwidth
SF = 7              # Spreading Factor
Ts = (2**SF) / BW   # Symbol duration

# Create time vector
t = np.linspace(0, Ts, int(Fs * Ts))

# Generate up-chirp
chirp = np.exp(1j * 2 * np.pi * (BW/(2*Ts) * t**2))

# Plot first samples
plt.plot(np.real(chirp[:2000]))
plt.title("LoRa Chirp - Real Part")
plt.xlabel("Samples")
plt.ylabel("Amplitude")
plt.grid()
plt.show()
