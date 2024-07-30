import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq, fftshift


# Define parameters
amplitude = 1
frequency = 1  # in Hz
sampling_rate = 1000  # samples per second
duration = 5  # seconds
t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)  # time vector


# Generate sine wave
sine_wave = amplitude * np.sin(2 * np.pi * frequency * t)


# Compute Fourier transform
N = len(sine_wave)
yf = fft(sine_wave)
xf = fftfreq(N, 1 / sampling_rate)


# Shift zero frequency component to the center
xf = fftshift(xf)
yf = fftshift(yf)


# Scale by the length of the signal to get the exact theoretical values
yf_scaled = yf * (2 * np.pi / N)


# Extract specific values for verification
expected_frequency_indices = np.where((xf == -1) | (xf == 1))[0]
specific_values = yf_scaled[expected_frequency_indices]


# Plot the sine wave
plt.figure(figsize=(12, 6))


plt.subplot(2, 1, 1)
plt.plot(t, sine_wave)
plt.title('Sine Wave with Amplitude 1 and Frequency 1 Hz')
plt.xlabel('Time (seconds)')
plt.ylabel('Amplitude')
plt.grid(True)


# Plot the real and imaginary parts of the Fourier transform
plt.subplot(2, 1, 2)
plt.stem(xf, np.real(yf_scaled), 'b', markerfmt="bo", basefmt="-b", label='Real Part')
plt.stem(xf, np.imag(yf_scaled), 'r', markerfmt="ro", basefmt="-r", label='Imaginary Part')
plt.title('Fourier Transform of the Sine Wave')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()
plt.xlim(-5, 5)  # Set x-axis limits to focus on the relevant frequency range


plt.tight_layout()
plt.show()


# Print specific values for verification
for freq, value in zip(xf[expected_frequency_indices], specific_values):
    print(f"Frequency: {freq} Hz, Value: {value}")
