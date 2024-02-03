import numpy as np
import matplotlib.pyplot as plt

def fourier_plotter(signal, sampling_rate):
    # Calculate the Fourier transform
    n = len(signal)
    frequencies = np.fft.fftfreq(n, d=1/sampling_rate)
    fft_values = np.fft.fft(signal)
    
    # Plot the original signal
    plt.subplot(2, 1, 1)
    plt.plot(np.arange(0, n)/sampling_rate, signal)
    plt.title('Original Signal')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')

    # Plot the Fourier transform (frequency spectrum)
    plt.subplot(2, 1, 2)
    plt.plot(frequencies, np.abs(fft_values))
    plt.title('Fourier Transform (Frequency Spectrum)')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Amplitude')

    plt.tight_layout()
    plt.show()

# Example usage:
sampling_rate = 1000  # Sample rate in Hz
t = np.arange(0, 1, 1/sampling_rate)  # Time vector
signal = 2 * np.sin(2 * np.pi * 5 * t) + 1.5 * np.cos(2 * np.pi * 10 * t) + 0.5 * np.sin(2 * np.pi * 20 * t)

fourier_plotter(signal, sampling_rate)
